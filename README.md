# Python for (open) Neuroscience

<img align="right" width="400" height="400" src="https://imgs.xkcd.com/comics/python.png">

Python is an **open-source**, **high-level**, **multi-purpose** programming language. It offers tools for fast **manipulation of large matrices** and datasets (as MATLAB) and **powerful data aggregation** and statistics (as R), together with thousands of packages for **machine learning**, **visualizations**, simulations, hardware control, and many others. As a result, **a growing number of labs are adopting it for their workflows**. 

This course will start covering **the basics of Python usage** and build up from there to some **more advanced topics**. The aim is to bring participant up to speed using **Python to solve some of the problems** we face daily in the lab. People with some Python experience are welcome! You can help other students in the first part, and learn something useful in the later modules.

<br/><br/>
<br/><br/>

## Lectures recordings
- [Lecture 2.0](https://youtu.be/ROFbFADkKpU): Local Python installation, demistified
- [Lecture 2.1](https://youtu.be/O_rRMRIJdxc): Jupyter notebooks and working with the filesystem
- [Lecture 2.2](https://youtu.be/BzLIZx4Y-E8): Working with images and imaging data
- [Lecture 3.0](https://youtu.be/UF2rJg5aCYo): Version control using GitHub
- (Lecture 3.1 missing - Imaging data analysis)
- [Lecture 3.2](https://youtu.be/8QhOFkEkhoQ): Introduction to statistics and machine learning
- (Lecture 3.3 missing - Running experiments in Python)
- [Lecture 3.4](https://youtu.be/GjYWyihBAoo): Data visualization


## Additional online resources and exercises
#### Intro level
Those is mostly aimed at people who have never written a line of Python, or have forgot everything about it.

- [Datacamp](https://www.datacamp.com/courses/intro-to-python-for-data-science): requires registration, but offers free intro courses for basic Python usage. Very boring, as drills should be.
- [Codecademy](https://www.codecademy.com/learn/learn-python-3): has same formula, with free account offers some basic Python tutorials.
- [Udacity](http://udacity.com/course/cs101): again the same, more based on videos.


#### Intermediate level

- [Python for neuroscientists](https://pyforneuro.com/)
- [Case Studies in Neural Data Analysis](https://mark-kramer.github.io/Case-Studies-Python/intro.html)
- [Computational Neuroscience in Python textbook](https://mrgreene09.github.io/computational-neuroscience-textbook/)

## Organization of the course

**Structure**: The course will be organized in four modules. Each module comprises three sessions, two hours each, that will mix frontal lectures and hands-on parts to work on in pairs (peer coding). 

A schedule for each module could be:
- Week 0:
    - Lecture x.0 (tentative: 17:00-19:00)
    - Lecture x.1 (tentative: 17:00-19:00)
- Week 1:
    - Lecture x.2. (tentative: 17:00-19:00)
    - Office hours. (tentative: 17:00-19:00)
    

**Framework and requirements**: You will be following the course on your own laptop. The first two modules will be teaching using **Google Colab**, with **no setup required** (you will only need a browser and a working internet connection). In the second part we will move to **Jupyter Notebooks**, to understand how to **set up an real-world Python environment** that can be used in the every day research work. There won't be system requirements, we should be able to set it up on Windows, MacOS, and Linux (you will have instructions and assistance for doing that!).

**Assignments**: At the end of each of the first three modules there will be **a minimal recap assigment**, and a **time slot to ask questions** on the lectures and on the assignment. (Ideally) the assignments will be automatically scored using GitHub Classroom. The last module will not have a test; the final assignment will be a **small Python project of your choice**, ideally related/useful for your work at the lab.

**Material**: The material will consist in jupyter notebooks and python scripts with the lecture content and exercises and it will be made available before the lectures using GitHub. 




## Syllabus
Syllabus for the course. Ideally, its incremental nature should ensure that each core concept that is introduced is then revisited and expanded on in every new lecture.

---


### Module 0: the fundamentals 🏗
A very basic introduction to the basic syntax and structure of Python code, just a smattering: more will come while exploring other modules.

 - **0.0. Introduction to Python variables and statements**
    -  <ins>Theory:</ins> Variable types (numbers, strings) and their operators, data structures (lists, dictionaries), basic clauses (conditionals, while/for  loops, try-except); simple file reading. 
    - <ins>Practicals:</ins>Exercises tba.
  - **0.1. Functions (and modules ?)**
    - <ins>Theory:</ins> Reusing code in Python: functions (definition, argument passing, scope), modules (make a new module, import functions from existing library); installing new libraries with `pip`.
    - <ins>Practicals:</ins> exercises on functions; create a simple module; `pip install` a new library and use it.
  - **0.2. Fundamentals of classes and objects**
    - <ins>Theory:</ins> Definition of classes and their components (methods, attributes, properties); objects and object instantiation.
    - <ins>Practicals:</ins> write a simple custom class. Interact and use previously defined classes, search for their methods and attributes.

**Assignment**: Exercises tba

---


### Module 1: the scientific stack in Python 📚
We introduce the Holy Trinity of data analysis: `numpy`, `pandas`, and `matplotlib`; and we show how they solve almost all our data analysis problems.

 - **1.0. `numpy`**
    - <ins>Theory:</ins> Data types: the `np.array`. initialisation, operators, indexing (numerical and boolean masking); operations with arrays (concatenate, stack, searching extrema, sorting, using sorting indexes). Visualising arrays and matrices with `matplotlib`. Reading and writing `.npy` files.
    - <ins>Practicals:</ins> Exercises tba, ideally with some neuro-related data. Turning `for` loops into vector operations.
 - **1.1. `pandas`**: 
    - <ins>Theory:</ins> `pd.Series` and `pd.DataFrames`; reading and writing `.csv` files. Optimal ways to organize data in dataframes. Working with dataframes: indexing, slicing, selecting, querying, interpolating, mapping. Using `matplotlib` to visualise datasets. 
    - <ins>Practicals:</ins> exercises tba, ideally with some neuro-related data. Important: show how labelled data in `pandas` make operations easier than when using `numpy`.
 - **1.2. More on `pandas`**: 
    - <ins>Theory:</ins> Advanced `pandas`: aggregated operations using `groupby()` and `rolling()`. Group statistics, smoothing, resampling. Mindblowing `pandas` (depending on progress/interest): hierarchical indexing with `MultiIndex`, aggregated operations, dataset alignment. Introduction to `seaborn` for dataset visualization.
    - <ins>Practicals:</ins> show how to easily make aggregate statistics and visualisations using `seaborn`.

**Assignment**: Exercise tba

---


### Module 2: Python for neuroscientific data 🔬
We start using all of the above on some real world scenario and neuroscientific data, trying to find common solutions to problems and tasks from different fields.

- **2.0. Real-world Python for real-world data**
 - <ins>Theory:</ins> Moving from Google Colab from local Python (using Anaconda) and jupyter notebook; understand where things are in a local installation; install new modules with `pip`. Interact with local data: browse and reorganize folders; opening or importing the most common data types that might come from experiments (`.txt`, `.csv`, `.xlsx`, `.mat`, `.tiff`, ...to adjust depending on interest).
    - <ins>Practicals:</ins> Set up a working local Python environment, load some data and make some plots.
- **2.1. Images**
    - <ins>Theory:</ins> Images and stacks data formats. Opening and writing different data formats (`.tiffs`, `.nrrd`, `.nii`). Visualising images with `matplotlib` and videos and stacks with `napari`. Simple image operations (cropping, smoothing, resizing, histogram normalisation...); batch processing of images.
    - <ins>Practicals:</ins> Exercises tba
 - **2.2. Time series**
    - <ins>Theory:</ins>Working with time series using `numpy` and `pandas`. Reading and writing time series data. Resampling, event detection (eg spike detection or artefact identification), event-triggered cropping. Filtering, smoothing (if there is interest/time, introduction to tools for frequency-domain analysis). 
    - <ins>Practicals:</ins> Exercises tba


**Assignment**: Exercise tba

---

### Module 3: Advanced topics in Python for neuroscience ☄️
We see how to bring home the bacon with Python as neuroscientists. Keep your code organised, generate good paper figures, make sure that your code is documented and accessible. Here are some possible topics, but we will choose together and pick up three based on interest.

- **Advanced visualisation and data rendering**
    - <ins>Theory:</ins> Some basic concepts and rules of data visualisation using `matplotlib`, tips for generating paper quality figures. More on `pandas` and `seaborn`. How to create animations with `matplotlib` and `napari`.
    - <ins>Practicals:</ins> Exercises tba.
- **Version control using `git` and GitHub**
    - <ins>Theory:</ins> Advantages and importance of version control systems. Core `git` concepts: `add`, `commit`, `branch`. Synch code with GitHub: `fetch`, `pull`, `push`.
    - <ins>Practicals:</ins> Exercises tba
- **Organising and publishing scientific code.**
    - <ins>Theory:</ins> Best practices for clean and readable scripts and notebooks. Design principles for a data processing pipeline; structure of a pip installable repository. How and where to deposit code for a publication.
    - <ins>Practicals:</ins> Exercises tba
- **Scripting experiments using Python**
    - <ins>Theory:</ins> Use Python to generate visual or auditory stimuli. Brief introduction to Psychopy. Interacting with Arduino and NI boards to read and write digital, analog and serial inputs/outputs
    - <ins>Practicals:</ins> Exercises tba
 - **Fundamentals of statistics and machine learning with Python**
    - <ins>Theory:</ins> Compute basic statistical tests with `scipy.statistics`. The `scikit-learn` package: Dimensionality reduction and clustering. Using Principal Component Analysis (PCA) to reduce dimensionality on a dataset. Introduction to clustering using the K-means algorithm
    - <ins>Practicals:</ins> Exercises tba
- **...**


**Assignment**: You will be ask to complete a small Python project of your choice addressing a problem from your daily work at the lab. Could be anything: count cells from images, perform some data analysis on existing datasets, visualize EEG timeseries or MRI stacks, hack the institute coffee machine card...

---


### Complimentary soft skills
Ideally, the course will also try to convey some more elusive coding-related soft skills, such as:
- **Write good data analysis code**, keeping an eye on reusability, readability, parameterisation... 
- **Learn how not to get stuck** and learn from bugs: find online resources (documentation, StackOverflow, GitHub); and interact with them (asking questions, reporting bugs, raising issues, etc.)
- **Understand the value of open source code** in the scientific endeaviour, and the importance of depositing code and datasets.




