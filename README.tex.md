# HW0: Environment setup for EECS 349 @ NU

In this assignment, the goals are:
- to set up a working programming environment using either `conda` or `virtualenv` environments.
- to get acclimated to the "pull, commit, push" development cycle for git. All assignments in this course will be submitted via Github.
- to see how the autograder works for this class. We use [Travis-CI](http://travis-ci.com) for autograding.

## Clone this repository

First, let's clone this repository. We'll use `git` for all submissions in this class. New to `git`? Not to worry, it's quite easy! Here's a [helpful guide](https://guides.github.com/activities/hello-world/). To clone this repository run the following command in some repository once you have git installed on your computer:

``git clone https://github.com/nucs349/hw0-setup-[your_username]``

`[your_username]` is replaced in the above link by your Github username. Alternatively, just look at the link in your address bar if you're viewing this README in your submission repository in a browser. Once cloned, `cd` into the cloned repository. Every assignment has some files that you edit to complete it. 

## Files you edit

The following files are to be edited in this assignment:

```
code.py
problems.tex.md
```

Do not edit anything in the `tests` directory. Files can be added to `tests` but files that exist already cannot be edited. Do not edit `.travis.yml`. This is used by Travis to test your code! 

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

```
git pull origin master
git push origin master
```

will pull the remote code and then push the commit to the repository on Github. This triggers testing code which checks your program for errors and compares it with the solution.

## Running the test cases

Every assignment comes with a *testing suite* that is used for autograding. The way the grading of every assignment works is that it compares every function you implement with the output of the solution (made by the course instructors). The test cases are transparent in input/output and can be inspected in the `tests` directory in the assignment's repository. If you pass all the test cases, you will get 100% on the autograded portion of the assignment. If you pass 9/10 test cases, you will get 90% on the autograded portion. 8/10 = 80%. And so on. 

The test cases can be run with:

``python -m pytest``

at the root directory of the assignment repository. This gives output that looks something like:

```
========== test session starts ===========
platform darwin -- Python 3.7.2, pytest-4.1.0, py-1.7.0, pluggy-0.8.1
rootdir: /Users/prem/teaching/nucs349/hw0-setup-pseeth, inifile:
collected 1 item

tests/test_assignment.py F         [100%]

================ FAILURES ================
____________ test_sum_numbers ____________

    def test_sum_numbers():
        from code import sum_numbers
>       assert sum_numbers(3, 5) == 8
E       assert None == 8
E        +  where None = <function sum_numbers at 0x10f62de18>(3, 5)

tests/test_assignment.py:3: AssertionError
======== 1 failed in 0.04 seconds ========
```

Parsing this output we see we have failed one test: `test_sum_numbers`. Let's try to make this test pass by implementing the related function. 

**Do that now by editing "code.py".**

Then re-run the tests to see if they passed! If they did, you'll see something like this: 

```
========== test session starts ===========
platform darwin -- Python 3.7.2, pytest-4.1.0, py-1.7.0, pluggy-0.8.1
rootdir: /Users/prem/teaching/nucs349/hw0-setup-pseeth, inifile:
collected 1 item

tests/test_assignment.py .         [100%]

======== 1 passed in 0.03 seconds ========
```

Next, let's get acquainted with the Travis-CI output which automatically runs the tests for you! For rapid development, it's better to run the tests on your own machine.

## Getting automatic feedback on push

For peace of mind, it's good to know that your code also works on a different machine. Travis-CI will initialize a fresh machine, install all of the requirements needed for the assignment, and run the tests. It then gives a check or a cross depending on if the tests all passed or if some or all failed, respectively.

To view the output of travis, follow these steps:
1. Navigate to https://github.com/NUCS349/hw0-setup-[your_username]/commits/master
2. Here you'll see all of your commits. Next to each commit you will see an icon of either a green checkmark or a red X. Click the icon of the commit you wish to inspect.
3. A pop-up appears. Click through to 'Details'.
4. On this page you'll see the information given by Github regarding this commit and its corresponding run on Travis-CI. To inspect it further (and actually read the output of the test cases), click the link labeled `View more details on Travis CI` at the bottom of the page.
5. Scroll down and you'll see the output of the build process and of `python -m pytest`. If your local environment is set up properly, the output of `python -m pytest` on your machine will match perfectly with the run on Travis-CI.

## Free response questions

In the assignments, written responses are sometimes required. These are graded by hand. In some questions, you will be asked to write out math. To write out math, we request you use LaTeX code ([tutorial here](https://www.latex-tutorial.com/tutorials/amsmath/)). Every student repository has [Texify](https://github.com/apps/texify) installed in this class. Texify looks at any files in the repository of the form `*.tex.md`. These files have Tex run on them and the math expressions in those files are rendered. This happens automaticaly when you push to Github. For example, this document has some LaTeX code written out (check the corresponding `README.tex.md` in the top-level folder.) The tex corresponding to the following:

$$f_X \left({x}\right) = \dfrac 1 {\sigma \sqrt{2 \pi} } \, \exp \left({-\dfrac { \left({x - \mu}\right)^2} {2 \sigma^2} }\right)$$

can be seen, enclosed in double dollar signs. Now that that is clear, look in `problems.tex.md`  to answer the free response question.

## Questions? Problems? Issues?

Please make sure first that something in this document doesn't already address your issue! If you still have problems, simply open an issue on the starter code repository for this assignment [here](https://github.com/NUCS349/hw0-setup/issues). Someone from the teaching staff will get back to you through there!

That's all! The workflow for every assignment in this class will work something like this.