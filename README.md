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

	- __Create a new object__
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


