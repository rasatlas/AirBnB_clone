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

+ Create :
    - Usage: create &lt class &gt
    - Creates a new instance of BaseModel, saves it to the JSON file and prints the id.
+ Show : 
    - Usage: show <class> <id> or <class>.show(<id>)
    - Prints the string representation of an instance based on the class name and id.
+ Destroy :
    - Usage: destroy <class> <id> or <class>.destroy(<id>)
    - Deletes an instance based on the class name & id and saves the change into the JSON file.
+ all :
    - Usage: all or all <class> or <class>.all()
    - Prints all string representation of all instances based or not on the class name.
    - If no class is specified, displays all instantiated objects.
+ count :
    - Usage: count <class> or <class>.count()
    - Retrieves the number of instances of a given class.
+ update :
    - Usage: update <class> <id> <attribute_name> <attribute_value> or
<class>.update(<id>, <attribute_name>, <attribute_value>) or
<class>.update(<id>, <dictionary>)
    - Updates an instance based on the class name and id by adding or updating attribute and saves the changes into the JSON file.
