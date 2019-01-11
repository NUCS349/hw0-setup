# HW0: Environment setup for EECS 349 @ NU

In this assignment, the goals are:
- to set up a working programming environment using either `conda` or `virtualenv` environments.
- to get acclimated to the "pull, commit, push" development cycle for git. All assignments in this course will be submitted via Github.
- to see how the autograder works for this class. We use [Travis-CI](http://travis-ci.com) for autograding.

## Clone this repository

First, let's clone this repository. We'll use `git` for all submissions in this class. New to `git`? Not to worry, it's quite easy! Here's a [helpful guide](https://guides.github.com/activities/hello-world/). To clone this repository run the following command in some repository once you have git installed on your computer:

``git clone https://github.com/nucs349/hw0-setup-[your_username]``

`[your_username]` is replaced in the above link by your Github username. Alternatively, just look at the link in your address bar if you're viewing this README in your submission repository in a browser. Once cloned, `cd` into the cloned repository and continue on to environment setup.

## Environment setup

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

All assignments are submitted via Github in this class. Once you've accepted this assignment via the Github classroom link, it made a repository of the form https://github.com/nucs349/hw0-setup-\[your github username\]. In the first part of this README, you cloned the repository to your local machine to develop on.

To make changes, simply open or create some file in your local version. If you created a file, you have to do:

``git add [new_file_name]`` 

to make `git` track the file. If you edited an already tracked file, you don't have to add it. Then:

``git commit -am [commit_message]``

will commit the change. `commit_message` is something that describes the type of change you made. Good commit messages are descriptive, easy to understand, and correspond well with the actual changes made. Finally:

``git push origin master``

will push the commit to the repository on Github. This triggers testing code which checks your program for errors and compares it with the solution.

## Running the test cases



## Getting automatic feedback on push

## Testing LaTeX integration

<img src="/tex/dda1a54eef33ca00cb79041e7eedb95b.svg?invert_in_darkmode&sanitize=true" align=middle width=248.8305501pt height=57.53473439999999pt/>



## Questions? Problems? Issues?

Use the 
