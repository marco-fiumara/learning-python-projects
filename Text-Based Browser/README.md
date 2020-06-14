## [learning-python-projects](https://github.com/marco-fiumara/learning-python-projects)

# Text-Based Browser: Hard

Sometimes you need to read online documentation or find something on the Internet from the command line or terminal. So, let's use Python to create a text-based browser! Of course, making a real, full-blown browser is a very difficult task. In this project, you'll create a very simple browser that will ignore JavaScript and CSS, won't have cookies, and will only process a limited set of tags. Still, it will be useful and, most importantly, fun to program!

### The Tic-Tac-Toe activity helped to reinforce the basic concepts, such as:

- Computer programing theory
- Introduction to operating systems
- Computer algorithms
- Big O notation
- Data structures
- Stack
- Functional decomposition
- World Wide Web theory
- HTTP protocol
- HTTP URL
- HTTP messages
- HTML
  - Basics
  - Tags and attributes
  - Page structure
- Create module
- Packages
- Requests library (Retrieving data only)
- Parsing HTML with BeautifulSoup4

### Instructions:

Open up terminal and enter the following command:
(NOTE: this command is if you are in the Text-Based Browser directory in the terminal, if you aren't, you can also do this by putting the full path to (and including) the main.py file)

(NOTE: the `[folder_name]` can be named whatever you would like. This folder will be created and will store .txt files of parsed HTML content.)

`python [file path / filename (incl. extension) i.e. main.py] [folder_name]`

This command will only have to be run once to start the program.

From here, you can enter a URL to be parsed. URLs should only be the domain.
i.e. _docs.python.org_ or _google.com_.

Once the domain has been entered once successfully and the file for it has been created, you may refer to it by just the name, without the .com or .org.
i.e. _docs.python_ or _google_.

To go back to previous entries, you may enter the `back` command to have the previous entry printed. There isn't however a forward command.

To exit the program, simply type `exit`.

### Examples:

The following is an example interaction of a user using the program.

(NOTE: The `>` you see is not included in the program, but indicates where the user has inputted information)

```
> python browser.py dir-for-files
> docs.python.org
index
modules
Python
Documentation
Python 3.7.4 documentation
Welcome! This is the documentation for Python 3.7.4.
Parts of the documentation:
What's new in Python 3.7? or all "What's new" documents since 2.0
Tutorial start here
Library Reference keep this under your pillow
Language Reference describes syntax and language elements
Python Setup and Usage how to use Python on different platforms
Python HOWTOs in-depth documents on specific topics
Installing Python Modules installing from the Python Package Index & other sources
Distributing Python Modules publishing modules for installation by others
Extending and Embedding tutorial for C/C++ programmers
Python/C API reference for C/C++ programmers
FAQs frequently asked questions (with answers!)
Indices and tables:
Global Module Index quick access to all modules
General Index all functions, classes, terms
Glossary the most important terms explained
Search page search this documentation
Complete Table of Contents lists all sections and subsections
Meta information:
Reporting bugs
About the documentation
History and License of Python
Copyright
> exit
```

```
> python browser.py dir-for-files
> docs.python.org
index
modules
Python
Documentation
Python 3.7.4 documentation
Welcome! This is the documentation for Python 3.7.4.
Parts of the documentation:
What's new in Python 3.7? or all "What's new" documents since 2.0
Tutorial start here
Library Reference keep this under your pillow
Language Reference describes syntax and language elements
Python Setup and Usage how to use Python on different platforms
Python HOWTOs in-depth documents on specific topics
Installing Python Modules installing from the Python Package Index & other sources
Distributing Python Modules publishing modules for installation by others
Extending and Embedding tutorial for C/C++ programmers
Python/C API reference for C/C++ programmers
FAQs frequently asked questions (with answers!)
Indices and tables:
Global Module Index quick access to all modules
General Index all functions, classes, terms
Glossary the most important terms explained
Search page search this documentation
Complete Table of Contents lists all sections and subsections
Meta information:
Reporting bugs
About the documentation
History and License of Python
Copyright

> google.com
Images
Maps
Play
YouTube
News
Gmail
Drive
More »
Web History
Settings
Sign in
Advanced search
Advertising Programmes
Business Solutions
About Google
Google.com.au
© 2020 - Privacy - Terms
Privacy
Terms

> docs.python
index
modules
Python
Documentation
Python 3.7.4 documentation
Welcome! This is the documentation for Python 3.7.4.
Parts of the documentation:
What's new in Python 3.7? or all "What's new" documents since 2.0
Tutorial start here
Library Reference keep this under your pillow
Language Reference describes syntax and language elements
Python Setup and Usage how to use Python on different platforms
Python HOWTOs in-depth documents on specific topics
Installing Python Modules installing from the Python Package Index & other sources
Distributing Python Modules publishing modules for installation by others
Extending and Embedding tutorial for C/C++ programmers
Python/C API reference for C/C++ programmers
FAQs frequently asked questions (with answers!)
Indices and tables:
Global Module Index quick access to all modules
General Index all functions, classes, terms
Glossary the most important terms explained
Search page search this documentation
Complete Table of Contents lists all sections and subsections
Meta information:
Reporting bugs
About the documentation
History and License of Python
Copyright

> back
Images
Maps
Play
YouTube
News
Gmail
Drive
More »
Web History
Settings
Sign in
Advanced search
Advertising Programmes
Business Solutions
About Google
Google.com.au
© 2020 - Privacy - Terms
Privacy
Terms

> exit
```
