# Install Python with this guide BEFORE coming to the meetup
We will not cover installation during the meetup.

# Installing Anaconda with Python 3
Anaconda is the name of a distribution of Python created by a company with the same name (formerly Continuum Analytics). It is currently the most popular distribution of Python for data science and contains all the popular libraries plus some extra software. 

* Please download [Anaconda with Python 3][1] now. Select all the default installation instructions.

### Reason for Python 3 and not Python 2
Jan 1, 2020 will mark the last day that Python 2 will be officially supported. Python 3 is the present and future and nearly all serious development will use it. 

# Testing for Successful Installation

Let's ensure that you the Anaconda distribution got installed correctly and that you are indeed running the latest version of Python 3.

## Windows Users
Open up the program **`Anaconda Prompt`**. This program will look very similar to the normal **`Command Prompt`** but will place the destination of the latest Python 3 version at the beginning of the path.

## Mac/Linux Users
Open up a terminal

# All Users

1. Type **`python`** at the prompt
1. Ensure that in the header you see Python version 3.X where X >= 6 
![][2]
1. If you don't see this header with the three arrow **`>>>`** prompts and instead see an error, then we need to troubleshoot here.
2. If you are running Python version 2.X, see [these instructions below](#If-you-are-running-Python-version-2.X)
3. Press **`ctrl + d`** to exit Python.

## Troubleshooting

### Windows
The error message that you will see is **`'python' is not recognized as an internal or external command...`**

Make sure you are running the **`Anaconda Prompt`** and not the normal **`Command Prompt`**. 

If you are in **`Anaconda Prompt`** and still getting this message then see the optional installation below.

### Mac/Linux
The error message you should have received is **`python: command not found`**. Let's try and find out where Python is installed on your machine.

1. Run the command: **`$ which -a python`**    
![][4]
1. This outputs a list of all the locations where there is an executable file with the name **`python`**
1. This location must be contained in something called the **path**. The path is a list (separated by colons) containing directories to look through to find executable files
2. Let's output the path with the command: **`echo $PATH`**
![][5]
1. My path contains the directory (**`/Users/Ted/Anaconda/bin`**) from above so running the command **`python`** works for me.
1. If your path does not have the directory outputted from step 1 then we will need to edit a file called **`.bash_profile`** (or **`.profile`** on some linux machines)
1. Make sure you are in your home directory and run the command:
> **`nano .bash_profile`**
1. This will open up the file **`.bash_profile`**, which may be empty
2. Add the following line inside of it: **`export PATH="/Users/Ted/anaconda3/bin:$PATH"`** (use your Anaconda directory)
3. Exit (**`ctrl + x`**) and make sure to save
4. Close and reopen the terminal and execute: **`echo $PATH`**
5. The path should be updated with the Anaconda directory prepended to the front
6. Again, type in **`python`** and you should be good to go
7. **`.bash_profile`** is itself a file of commands that get executed each time you open a new terminal.

### Optional (Advanced) Installation for Windows Users
It is possible to run Python from the **`Command Prompt`** directly in Windows. If you so desire, [manually configure][3] your **Command Prompt**.

### If you are running Python version 2.X
If you have a previously installed Anaconda distribution with Python 2, then you might want to consider removing it from your system. Only take this option if you are removing the Anaconda distribution itself that contains Python 2. Many machines will have Python 2 built-in. Unless you have some legacy project that must be maintained in Python 2, there is no use in keeping it.

# More on the path (all operating systems)
The path is a list of directories that the computer will search in order, from left to right, to find an executable program with the name you entered on the command line. It is possible to have many executables with the same name but in different folders. The first one found will be the one executed.

### Displaying the path
* Windows: **`path`** or **`set %PATH%`**
* Mac/Linux **`echo $PATH`**

### Finding the location of a program
* Windows: **` where program_name`**
* Mac\Linux: **`which program_name`**

### Editing the path
* Windows: Use the [set (or setx)][6] command or from a [GUI][7]
* Mac\Linux: By editing the **`.bash_profile`** as seen in the troubleshooting section above.

# Running IPython
IPython stands for interactive Python and is an enhanced Python environment on the command line. It is superior to the default interactive environment that we first ran above.

Open up a terminal/Anaconda Prompt and execute **`ipython`**. Again, you should see a header that states the exact same information as before. Press **`ctrl + d`** to exit.

# Running a Jupyter Notebook
The Jupyter Notebook is one of the most popular environments for running Python code for data scientists. It allows you to embed text, images, and code altogether in a single document. Let's start a Jupyter Notebook now.

* Open a terminal/Anaconda Prompt execute **`jupyter notebook`**
* Your browser should open with a new tab that shows the contents of the current directory - the location where you ran the command.
* If you did not change directories after opening your terminal/Anaconda Prompt then you should see the contents of your home directory. Mine looks like this:

![][12]

* Click on the **New** button on the top right of the page and you will have started a Jupyter Notebook which you can then run Python commands.
* To exit the Jupyter Notebook, you will need to go back to the terminal/Anaconda Prompt where you launched it and press **`ctrl + c`** twice.

# Starting Python with the Anaconda Navigator GUI
When you install the Anaconda distribution, you will also install a software program named **Anaconda Navigator**. This is a graphical user interface (point and click program) that also allows you to start running a Python environment without the being on the command line.

* Find and open the Anaconda Navigator program to get a screen that looks like this:
![][11]
* Under the Jupyter Notebook section, click **Launch**
* A new terminal/Anaconda Prompt will automatically pop-up and a new browser tab will open up as well showing the contents of the home directory.
* This is the exact same environment that we launched with the command line above.
* To exit, you must again go to the terminal/Anaconda Prompt and press **`ctrl + c`** twice.

# Python vs IPython
**`python`** and **`ipython`** are both executable programs that run Python interactively from the command line. The **`python`** command runs the default interpreter, which comes prepackaged with Python. There is almost no reason to ever run this program. It has been surpassed by **`ipython`** (interactive Python) which you also run from the command line. IPython adds lots of functionality such as syntax highlighting and special commands.

# IPython vs Jupyter Notebook
The Jupyter Notebook is a browser based version of IPython. Instead of being stuck within the confines of the command line, you are given a powerful web application that allows you to intertwine code, text, and images. [See this][8] for more details of the internals.

![][9]

# Jupyter Lab
[Jupyter Lab][11] is yet another interactive browser-based program that allows you to have windows for notebooks, terminals, data previews, and text editors all on one screen.  It is the "next-generation user interface for Project Jupyter".

# Repository Files
 As you can see at the top of this page, there are multiple files in this repository. 

1. The README file that you are reading right now
2. The `.ipynb` files where all the magic happens
3. A resources section with lots of places to get help and learn more

[1]: https://www.anaconda.com/download
[2]: images/pythonterminal.png
[3]: https://medium.com/@GalarnykMichael/install-python-on-windows-anaconda-c63c7c3d1444
[4]: images/which_python.png
[5]: images/path_mac.png
[6]: https://stackoverflow.com/questions/9546324/adding-directory-to-path-environment-variable-in-windows
[7]: https://www.computerhope.com/issues/ch000549.htm
[8]: http://jupyter.readthedocs.io/en/latest/architecture/how_jupyter_ipython_work.html
[9]: images/jupyter_internal.png
[10]: images/windows_anaconda_check.png
[11]: images/anaconda_navigator.png
[12]: images/jupyter_notebook.png

