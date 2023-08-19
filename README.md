# 0x00. AirBnB clone - The console
`Group project` `Python` `OOP`

## Table of Contents
	1. Introduction
	2. Environment
	3. Installation
	4. Testing
	5. Usage

## Introduction

Team project to build a clone of [AirBnB](https://www.airbnb.com/).

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

The console willl perform the following tasks:

	- Create a new object
	- Retrive an object from a file
	- Do operations on objects
	- Destroy an object

### Storage

All file writing and reading is handled by the `FileStorage` Class.

## Environment

- Style guidelines:
	
	- [pycodestyle (version 2.8.0)](https://pypi.org/project/pycodestyle/)

- All the development and testing was done over a system running Ubuntu 20.04 LTS using Python 3.8.5.

- The editor used was VIM 8.1 and Version Control was done using Git 2.25.1.

## Installation
```git
git clone https://github.com/rasatlas/AirBnB_clone.git
```

Move to the AirBnB_clone directory and run the command:
```bash
./console.py
```

### Execution

In interactive mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

In Non-interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Testing

All the test are defined in the tests directory.

### Documentation

* Modules:

```python
python3 -c 'print(__import__("my_module").__doc__)'
```

+ Classes:

```python
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```

* Functions (inside and outside a class):

```python
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```

and

```python
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

### Python Unit Tests
+ unittest module
+ File extension .py
+ Files and directories star with test_
+ Organization:
	- For models/base.py, unit tests in: tests/test_models/test_base.py
+ Execution command: 
```python
python3 -m unittest discover tests
```
+ or: 
```python
python3 -m unittest tests/test_models/test_base.py
```

### Run test in interactive mode

```bash
echo "python3 -m unittest discover tests" | bash
```

### Run test in non-interactive mode
To run the tests in non-interactive mode, and discover all the tests, you can use the command:

```python
python3 -m unittest discover tests
```

## Usage

+ Start the console in interactive mode:
```bash
$ ./console.py
(hbnb)
```
+ Use `help` to see the available commands:
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```
+ Quit the console:
```bash
(hbnb) quit
$
```

### Commands:

+ **create** :
    - Usage: _create &lt;class&gt;_
    - Creates a new instance of BaseModel, saves it to the JSON file and prints the id.
+ **show** : 
    - Usage: _show &lt;class&gt; &lt;id&gt;_ or _&lt;class&gt;.show(&lt;id&gt;)_
    - Prints the string representation of an instance based on the class name and id.
+ **destroy** :
    - Usage: _destroy &lt;class&gt; &lt;id&gt;_ or _&lt;class&gt;.destroy(&lt;id&gt;)_
    - Deletes an instance based on the class name & id and saves the change into the JSON file.
+ **all** :
    - Usage: _all_ or _all &lt;class&gt;_ or _&lt;class&gt;.all()_
    - Prints all string representation of all instances based or not on the class name.
    - If no class is specified, displays all instantiated objects.
+ **count** :
    - Usage: _count &lt;class&gt;_ or _&lt;class&gt;.count()_
    - Retrieves the number of instances of a given class.
+ **update** :
    - Usage: _update &lt;class&gt; &lt;id&gt; &lt;attributename&gt; &lt;attributevalue&gt;_ or <br>
_&lt;class&gt;.update(&lt;id&gt;, &lt;attributename&gt;, &lt;attributevalue&gt;)_ or <br>
_&lt;class&gt;.update(&lt;id&gt;, &lt;dictionary&gt;)_
    - Updates an instance based on the class name and id by adding or updating attribute and saves the changes into the JSON file.
