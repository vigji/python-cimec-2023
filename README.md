<img align="right" width="400" height="400" src="https://imgs.xkcd.com/comics/python.png">

# Python for open neuroscience

Python is a open-source, high-level, multi-purpose programming language. 

Thanks to its flexibility it has been widely adopted and it is used in thousands of applications. It offers tools for fast manipulation of large matrices and datasets (as MATLAB) and powerful data aggregation and statistics (as R), together with thousands of packages for machine learning, visualizations, simulations, hardware control, and many others.

In this course, we aim at covering the basics of Python usage and show how it can be used to solve many of the day-to-day problems we face as scientists. 
<br/><br/>

## Syllabus (draft)
Temptative syllabus for the course. Ideally, its incremental nature should ensure that each core concept that is introduced is then revisited and expanded on in every new lecture.


---


### Module 0: the fundamentals
A very basic introduction to the basic syntax and structure of Python code, just a smattering: more will come while exploring other modules.

 - **0.0. Introduction to Python variables and statements**
    -  <ins>Theory:</ins> Variable types (numbers, strings) and their operators, data structures (lists, dictionaries), basic clauses (conditionals, while/for  loops, try-except); simple file reading. 
    - <ins>Practicals:</ins> Setting up Python and the basic IDEs (Anaconda, PyCharm and Jupyter notebooks). Find documentation searching and online resources. Exercises tba.
  - **0.1. Functions and modules**
    - <ins>Theory:</ins> Reusing code in Python: functions (definition, argument passing, scope), modules (make a new module, import functions from existing library); installing new libraries with `pip`.
    - <ins>Practicals:</ins> exercises on functions tba; create a simple module; `pip install` a new library (ideally, something to achieve simply something complex) and use it.
  - **0.2. Fundamentals of classes and objects**
    - <ins>Theory:</ins> Definition of classes and their components (methods, attributes, properties); objects and object instantiation.
    - <ins>Practicals:</ins> write a simple custom class. Interact and use previously defined classes, search for their methods and attributes.

**Assignment**: Exercise tba

---


### Module 1: the scientific stack in Python
We introduce the Holy Trinity of data analysis: `numpy`, `pandas`, and `matplotlib`; and we show how they solve almost all our data analysis problems.

 - **1.0. `numpy`**
    - <ins>Theory:</ins> Data types: the `np.array`. initialisation, operators, indexing (numerical and boolean masking); operations with arrays (concatenate, stack, searching extrema, sorting, using sorting indexes). Visualising arrays and matrices with `matplotlib`. Reading and writing `.npy` files.
    - <ins>Practicals:</ins> Exercises tba, ideally with some neuro-related data. Important: practice turning for loops into vector operations.
 - **1.1. `pandas`**: 
    - <ins>Theory:</ins> `pd.Series` and `pd.DataFrames`; reading and writing `.csv` files. Optimal ways to organize data in dataframes. Working with dataframes: indexing, slicing, selecting, querying, interpolating, mapping. Using `matplotlib` to visualise datasets. 
    - <ins>Practicals:</ins> exercises tba, ideally with some neuro-related data. Important: show how labelled data make operations easier than numpy.
 - **1.2. More on `pandas`**: 
    - <ins>Theory:</ins> Advanced `pandas`: aggregated operations using `groupby` and `rolling`. Group statistics, smoothing, resampling. Mindblowing `pandas` (depending on progress): hierarchical indexing with MultiIndex, aggregated operations, dataset alignment. Introduction to `seaborn`.
    - <ins>Practicals:</ins> show how to easily make aggregate statistics and visualisations using `seaborn`.

**Assignment**: Exercise tba

---


### Module 2: Python for neuroscientific data
We start using all of the above on some real neuroscientific data, trying to find common solutions to problems and tasks from different fields.

- **2.0. Images**
    - <ins>Theory:</ins> Images and stacks data formats. Opening and writing different data formats (`.tiffs`, `.nrrd`, `.nii`). Visualising images with `matplotlib` and videos and stacks with `napari`. Simple image operations (cropping, smoothing, resizing, histogram normalisation...); batch processing of images.
    - <ins>Practicals:</ins> Exercises tba
 - **2.1. Time series**
    - <ins>Theory:</ins>Working with time series using `numpy` and `pandas`. Reading and writing time series data. Resampling, event detection (eg spike detection or artefact identification), event-triggered cropping. Filtering, smoothing (if there is interest/time, introduction to tools for frequency-domain analysis). 
    - <ins>Practicals:</ins> Exercises tba
 - **2.2. Fundamentals of statistics and machine learning with Python**
    - <ins>Theory:</ins> Compute basic statistical tests with `scipy.statistics`. The `scikit-learn` package: Dimensionality reduction and clustering. Using Principal Component Analysis (PCA) to reduce dimensionality on a dataset. Introduction to clustering using the K-means algorithm
    - <ins>Practicals:</ins> Exercises tba


**Assignment**: Exercise tba

---

### Module 3: Advanced topics in Python data analysis 
We see how to bring home the neuroscientific bacon with Python. Keep your code organised, generate good paper figures, make sure that your code is documented and accessible (this session is open to be adjusted based on requests and interests to make some space to deepen on some of the previous topics.)

- **3.0. Advanced visualisation and data rendering**
    - <ins>Theory:</ins> Some basic concepts and rules of data visualisation using `matplotlib`, tips for generating paper quality figures. More on `pandas` and `seaborn`. How to create animations with `matplotlib` and `napari`.
    - <ins>Practicals:</ins> Exercises tba.
- **3.1. Version control using `git` and GitHub**
    - <ins>Theory:</ins> Advantages and importance of version control systems. Core `git` concepts: `add`, `commit`, `branch`. Synch code with GitHub: `fetch`, `pull`, `push`.
    - <ins>Practicals:</ins> Exercises tba
- **3.2. Organising and publishing scientific code.**
    - <ins>Theory:</ins> Best practices for clean and readable scripts and notebooks. Design principles for a data processing pipeline; structure of a pip installable repository. How and where to deposit code for a publication.
    - <ins>Practicals:</ins> Exercises tba


**Assignment**: Exercise tba

---


### Complimentary soft skills
Ideally, the course will also try to convey some more elusive coding-related soft skills, such as:
- Write good data analysis code, keeping an eye on reusability, readability, parameterisation... 
- Learn how not to get stuck and learn from bugs: find online resources (documentation, StackOverflow, GitHub); and interact with them (asking questions, reporting bugs, raising issues, etc.)
- Understand the value of open source code in the scientific endeaviour, and the importance of depositing code and datasets.


## Schedule of the course (draft)

The course will be organized in 4 modules. Each module comprises three lectures, two hours each, that will mix theory and hands-on parts. At the end of each module there will be an assigment, and a time slot to ask questions on the lectures and the assignment. A temptative schedule for each module could be:

- Week 0:
    - Lecture x.0 (Monday 17:00-19:00)
    - Lecture x.1 (Thursday 17:00-19:00)
- Week 1:
    - Lecture x.2. (Monday 17:00-19:00)
    - Office hours. (Thursday 17:00-19:00)



