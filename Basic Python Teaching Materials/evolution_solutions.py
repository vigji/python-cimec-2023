# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:16:43 2021

@author: Łucja
"""

# importing our packages
import numpy as np
import matplotlib.pyplot as plt



#LOADING GENOME ARRAY FROM CSV FILE
genome = np.genfromtxt('D:\\NOL_python\\genom_array_mut.csv', delimiter=',') 
# first argument has to be the full path to the genome file (insert the path that applies on your computer)
# use double '\' to prevent misunderstanding (e.g. Python will understand '\n' as a new line, but '\\n' as '\n')
# the second argument is delimiter - the sign that separates values in the file
# CSV stands for comma-separated values, so the delimiter has to be comma



# EXPLORING DATA 
#plt.matshow(genome[:10]) # plotting first 10 animals

#unique = np.unique(genome) # finding unique values in genome array
#print(unique)




#LOADING EXPRESSION ARRAY
express = np.genfromtxt('D:\\NOL_python\\express_array.csv', delimiter=',') 
# if you are loading multiple files from one folder you can store the path in a variable and then reuse it by just adding strings eg.: 
# path = 'D:\\NOL_python\\'
# express = np.genfromtxt(path + 'express_array.csv', delimiter=',')



# CALCULATING FITNESS
def calc_fitness (genome, express): # function takes the genome and expression array and calculates fitness of each animal
    
    # multiplying genes by weights provided by express array, using broadcasting
    weighted_genome =  genome * express 
    # Express array is 1D array with the lenght of 25 (as the number of genes-columns in our genome array)
    # For each animal (row) numpy will multiply each gene (cell) by corresponding value in express array
    
    # adding together values in weighted_genome for each row
    fitness = np.sum(weighted_genome, axis = 1) 
    # Axis argument specifies over each dimention to sum (here 1 means to sum values in each row-animal)
    # Thus fitness will store one value for each animal (it will be 1D array with the length of 1000 
    
    return fitness



# CALCULATING THE PROBABILITY OF REPRODUCTION
def calc_repr_chance (fitness, min_fit): # the function takes fitness array and minimal fitness that allows animal to reproduce
    
    # filtering out animals with to low fitness
    filtered_fitness = np.where(fitness >= min_fit, fitness, 0) 
    # First argument in where function is a boolean array with True for fitness values higher or equal to the minimal
    # and False for fitness values lower than minimal.
    # Second argument is the fitness array. For Trues in boolean array we are taking unchanged fitness values
    # Third argument is 0 - for Falses in boolean array we are taking 0 
    
    #calculating reproduction probability for each animal
    repr_chance = filtered_fitness / np.sum(filtered_fitness) 
    # Each value in filtered_fitness array is divided by the sum of all values in this array
    
    return repr_chance



# SIMULATING CROSSING-OVER PROCESS
def crossing_over (genome, ind_parent_1, ind_parent_2): # this function takes genome array and two parents indexes
    
    # first we are randomly selecting the crossing over point 
    point = np.random.randint(1, genome.shape[1])
    # It is just a number between 1 and the width of genome array (the length of genetic sequence we have for each animal)
    
    # generating the offspring
    offspring = np.hstack((genome[ind_parent_1, :point], genome[ind_parent_2, point:]))
    # An offspring is 1D array with the length of 25 (genetic sequence)
    # From first parent we are taking genes from 0 up to crossing-over point (excluding)
    # From second parent we are taking genes from the crossing-over point (including) to the end of the sequence
    # hstack stands for horizontal stack - it glues arrays horizontally (one next to the other)
    
    return offspring




# CREATING GENOME ARRAY OF NEW GENERATION
def create_new_gen (genome, repr_chance): # here we are taking an old genome and an array with reproduction probabilities
    
    # initialazing new genome array (so far filled with zeros)
    new_gen = np.zeros(genome.shape) # it has the same size as old genome array as we shoud keep the number of animals constant
    
    # to fill new_gen with new animals we have to conduct reproduction multiple times
    for i in range(new_gen.shape[0]): # (exactly as many times as many rows-animals we have in new_gen)
        
        # selecting animals for reprduction
        parents = np.random.choice(np.arange(genome.shape[0]), size = 2, p = repr_chance) 
        # First argument of random.choice function is 1D array with numbers from 0 to 999 
        # These are simply indexes of animals from which we will choose parents
        # Second argument specifies how many elements we want to choose from the array
        # (note that by default the choice function will draw without replacement so parents will be two different indexes)
        # Third argument is an array of reproduction probabilities - each index will be drawn with corresponding probability
        
        # overwriting i'th row in new gen with a new offspring generated via our crossing-over function
        new_gen[i] = crossing_over(genome, parents[0], parents[1])
        # parents are stored in an array, and our function takes them as separate arguments, so we have to provide them separately
        
    return new_gen



# INTRODUCING MUTATIONS TO THE GENOME ARRAY
def intr_mutations(genome, ord_mut_prob, rare_mut_prob): # it takes genome array and probabilities od each of two mutation types
    
    # first we are creating an array (mask) that has zeros at places in which genome array has ones and ones where genome has zeros
    ord_mut_mask = np.select([genome == 0, genome == 1, genome == -4],[1, 0, -4])
    # First argument is a list of boolean arrays with the size of genome array
        # first array in the list has True values on cells in which the genome array has zeros
        # second array has Trues when genome has ones
        # third array has Trues when genome has -4
    # second argument is a list of values from which to take in case of True value in a corresponding boolean array
    # so when a particular cell of genome array contains 0, 
    # we will have True value in the corresponding cell of the first boolean array  
    # and we will take the 1 - the first value from a list to put in the corresponding cell of our ord_mut_mask array
    # *Notice that -4 in genome will be changed to -4 
    
    # Now we are peaking cells of genome array on which the ordinary mutation will occur
    ord_mut_places = np.random.choice([True, False], size = (genome.shape), p = [ord_mut_prob, 1 - ord_mut_prob]) 
    # we are randomly selecting True and False values (first argument) with given probabilities (argument p) 
    # and putting them on the array with the size od genome array (argument size)
    # Trues will occur with probability ord_mut_prob, and they will mark cells on which mutation occurs
    # * notice that we are choosing the places of mutations for whole array (including deleterious mutations). 
    #   However itt will not affect the probability of valid ordinary mutations (which can affect only 0 and 1 values),
    #   That is because the chances of mutations of paricular genes (cells) are independent
    
    # conducting mutation and creating new genome array
    ord_mut_genome = np.where(ord_mut_places, ord_mut_mask, genome)
    # where function takes a boolean ord_mut_places array, ord_mut_mask from which we will take values in case of mutation
    # and genome array from which we will take values in case of the lack of mutation
    # * notice that mutations will change 0 to 1 and 1 to 0 and keep -4 unchanged
    
    # we are using the same method to prepare the boolean array with places of rare mutations
    rare_mut_places = np.random.choice(a = [True, False], size = (genome.shape), p = [rare_mut_prob, 1 - rare_mut_prob]) 
    
    # and again we are conducting mutation
    mut_genome = np.where(rare_mut_places, -4, ord_mut_genome)
    # now we can use -4 as mask because in case of mutation the outcome value will always be -4

    return mut_genome



# SIMULATING ONE GENERATION AND CREATING A NEW ONE
def one_generation_sim (genome, express, ord_mut_prob, rare_mut_prob, min_fit): # we are passing all arguments that are used inside
    # so later on we can access and change them from outside the one_generation_sym function
    
    # first we are introducing mutations
    mut_genome = intr_mutations(genome, ord_mut_prob, rare_mut_prob)
    
    # then we are calculatig fitness
    fitness = calc_fitness(mut_genome, express)
    
    # quickly calculating the mean fitness
    mean_fitness = fitness.mean()
    
    # calculating the probabilities of reproguction
    repr_chance = calc_repr_chance (fitness, min_fit)
    
    # finally we are creating the new generation
    new_gen_array = create_new_gen(mut_genome, repr_chance)
    
    # we are returning two values
    return mean_fitness, new_gen_array




#############################################################################################################
# FINAL SIMULATION!
    
# first we can specify the parameters of your simulation (they can be changed any time)
ord_mut_prob = 0.02
rare_mut_prob = 0.0001
min_fit = 2

no_gen = 100 # how many generations we want to simulate

# lets create the container for mean fitness values
mean_fitness_array = np.zeros(no_gen)


# and simulate our population in for loop
for i in range(no_gen):
    
    # in each iteration of a loop we are creating a new generation and overwriting the old one
    mean_fitness, genome = one_generation_sim (genome, express, ord_mut_prob, rare_mut_prob, min_fit)
    # this function returns two values so we have to assign them to two variables
    # we can do that by typing:  var1, var2 = func()
    
    # now we are adding the mean fitness to the array
    mean_fitness_array[i] = mean_fitness


# now we can plot the evolution of our population :)
plt.plot(mean_fitness_array)
    