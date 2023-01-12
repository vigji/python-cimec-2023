# python-CIMeC

# # Structure of the course (draft)

The course will be organized in 4 modules. Each module comprises three lectures, two hours each, that will mix theory and hands-on parts. At the end of each module there will be an assigment, and a time slot to ask questions on the lectures and the assignment. A temptative schedule could be:

Week 0 (Module 0):
 - Lecture 0
 - Lecture 1
Week 1 (Module 0):
 - Lecture 2
 - Office hours


## Syllabus (draft)
Temptative syllabus for the course. Ideally, its incremental nature should ensure that each new concept that is introduced is constantly revisited and expanded on in every new lecture.

### Module 0: the fundamentals of Python.
A very basic introduction to the basic syntax and structure of Python code. Just a smattering: more will come with usage in other modules.

 - **0.0 Introduction to Python variables and statements**
    -  <ins>Theory</ins> Variable types (numbers, strings) and their operators, data structures (lists, dictionaries), basic clauses (conditionals, while/for  loops, try-except); simple file reading. 
    - <ins>Practicals</ins> Setting up Python and the basic IDEs (Anaconda, PyCharm and Jupyter notebooks). Find documentation searching and online resources. Exercises tba
  - **0.1: Functions and modules**
    - <ins>Theory</ins> Reusing code in Python: functions (definition, argument passing, scope), modules (make a new module, import functions from existing library); installing new libraries with pip
    - <ins>Practicals</ins> exercises on functions tba; create a simple module; `pip install` a new library (ideally, something to achieve simply something complex) and use it.
  - **0.2: Fundamentals of classes and objects**
    - <ins>Theory</ins> Definition of classes and their components (methods, attributes, properties); objects and object instantiation; 
    - <ins>Practicals</ins> write a simple custom class. Interact and use previously defined classes, search for their methods and attributes.

**Assignment**: Exercise tba


### Module 1: the scientific stack in Python
We introduce the Holy Trinity of data analysis: `numpy`, `pandas`, and `matplotlib`; and we show how they solve almost all our data analysis problems.

## Lecture 3:
`Numpy`: <ins>Theory</ins>data types (array, matrices), array initialisation, operators, indexing (numerical and boolean masking); operations with arrays (concatenate, stack, searching extrema, sorting, using sorting indexes). Visualising arrays and matrices with matplotlib. Reading and writing .npy files.
<ins>Practicals</ins> exercises tba, ideally with some neuro-related data. Important: practice turning for loops into vector operations


## Lecture 4
Pandas: <ins>Theory</ins>Series and DataFrames; reading and writing .csv files. Optimal ways to organize data in DataFrames. Working with DataFrames: indexing, slicing, selecting, querying, interpolating, mapping. Using Matplotlib to visualise pandas datasets. 
<ins>Practicals</ins> exercises tba, ideally with some neuro-related data. Important: show how labelled data make operations easier than numpy

## Lecture 5
Advanced pandas: <ins>Theory</ins>aggregated operations using groupby and rolling. Group statistics, smoothing, resampling. Mindblowing pandas (depending on progress): hierarchical indexing with MultiIndex, aggregated operations, dataset alignment. Introduction to seaborn.
<ins>Practicals</ins> show how to easily make aggregate statistics and visualisations using seaborn

## Assignment


# Module 2: Python for neuroscientific data
We start using all of the above on some real neuroscientific data, trying to find common solutions to problems and tasks from different fields.

## Lecture 6
Images. <ins>Theory</ins>Images and stacks data formats. Opening and writing different data formats (tiffs, nerd, NIfTI). Visualising images with matplotlib and videos and stacks with napari. Image operations (cropping, smoothing, resizing, histogram normalisation...); batch processing of images.
<ins>Practicals</ins> Exercises tba


## Lecture 7
Time series. <ins>Theory</ins>Working with time series using numpy and pandas. Reading and writing time series data. Resampling, event detection (eg spike detection or artefact identification), event-triggered cropping. Filtering, smoothing (upon interest/time, introduction to tools for frequency-domain analysis). 
<ins>Practicals</ins> Exercises tba


## Lecture 8
Fundamentals of statistics with Python. <ins>Theory</ins> Compute basic statistical tests with scipy.statistics. The scikit-learn package: Dimensionality reduction and clustering. Using Principal Component Analysis (PCA) to reduce dimensionality on a dataset. Introduction to clustering using the K-means algorithm
<ins>Practicals</ins> Exercises tba


## Assignment

# Module 3 Advanced topics in Python data analysis 
We see how to bring home the neuroscientific bacon with Python. Keep your code organised, generate good paper figures, make sure that your code is documented and accessible (this session is open to be adjusted based on requests and interests to make some space to deepen on some of the previous topics.)
<ins>Practicals</ins> Exercises tba

## Lecture 9
Advanced visualisation and data rendering. <ins>Theory</ins>Some basic concepts and rules of data visualisation using matplotlib, tips for generating paper quality figures. More on pandas and seaborn. How to create animations with matplotlib and napari.
<ins>Practicals</ins> Exercises tba

## Lecture 10
Version control using git and GitHub. <ins>Theory</ins> Advantages and importance of version control. Core git concepts: add, commit, branch. Synch code with GitHub: fetch, pull, push.
<ins>Practicals</ins> Exercises tba


## Lecture 11
Organising scientific code. <ins>Theory</ins> Best practices for clean and readable scripts and notebooks. Design principles for a data processing pipeline; structure of a pip installable repository. How and where to deposit code for a publication.
<ins>Practicals</ins> Exercises tba



## Assignment


### Soft skills
Ideally, the course will also try to convey some more elusive coding-related soft skills, such as:
- Write good data analysis code, keeping an eye on reusability, readability, parameterisation... 
- Learn how not to get stuck and learn from bugs: find online resources (documentation, StackOverflow, GitHub); and interact with them (asking questions, reporting bugs, raising issues, etc.)
- Understand the value of open source code in the scientific endeaviour, and the importance of depositing code and datasets.



