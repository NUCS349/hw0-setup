# HW0: Environment setup for EECS 349 @ NU

In this assignment, the goals are:
- to set up a working programming environment using either `conda` or `virtualenv` environments.
- to get acclimated to the "pull, commit, push" development cycle for git. All assignments in this course will be submitted via Github.
- to see how the autograder works for this class. We use [Travis-CI](http://travis-ci.com) for autograding.

## Setup

This course uses **Python 3**. Python 2 will not work for these assignments and all assignments will be graded with Python 3 on our end. Python 2 is [leaving the data science programming stack](https://pythonclock.org/) on Jan 1 2020.

The easiest way to get setup is to use [**miniconda**](https://conda.io/miniconda.html). 

Install the appropriate version of miniconda for your operating system (take care to select the Python 3 version). After miniconda is installed, you should be able to run `conda`. If you get an error (e.g. `-bash: conda: command not found`), make sure to source your bash file afterwards (`source ~/.bash_profile` worked for me). 

Now let's create a virtual environment. Virtual environments are a simple way to isolate all the dependencies for a particular project, making it easy to work on multiple projects at once without them interfering with each other (e.g. conflicting versions of libraries between projects). To make sure your environment matches the testing environment that we use for grading exactly, it's best to make a new environment for each assignment in this course. Here's the command:

``conda create -n hw0-setup python``

`hw0-setup` is the name for the environment and it can be replaced for each assignment (e.g. for the next homework, this would be hw1-decision-tree or something similar). The name can be whatever you want, just make sure to remember it!

Once the environment is created you can activate it with:

``conda activate hw0-setup``

Your shell might look something like `(hw0-setup) stark:nucs349 prem`. The environment name is in parenthesis, indicating that it is active. Now let's install the requirements for this assignment. Do this by navigating to the top root of this folder on the terminal and running, with an activated conda environment:

``pip install -r requirements.txt``

Great! Your environment is all set up. Do this for every assignment in the course.

## Github development cycle

## Testing LaTeX integration

$f_X \left({x}\right) = \dfrac 1 {\sigma \sqrt{2 \pi} } \, \exp \left({-\dfrac { \left({x - \mu}\right)^2} {2 \sigma^2} }\right)$

## Getting automatic feedback on push
