# fixitPy

![Static Badge](https://img.shields.io/badge/github-PyFixit-blue%3Flogo%3Dgithub?link=https%3A%2F%2Fgithub.com%2Fvoldgalf%2Ffixitpy)
![Static Badge](https://img.shields.io/badge/license-MIT-blue?link=https%3A%2F%2Fgithub.com%2Fvoldgalf%2FPyFixit)

Interface with the iFixit API through Python, easily.

### Current Features

- Guide Retrieval

### WIP Features

- Guide image retrieval
- text based searching for guides

## Installation

To install fixitPy

````bash
pip install fixitpy
````

### Import the library

````py
from fixitpy import find_guide
````

### Using the library

#### Getting a guide

````py
found_guide = find_guide(123) # call the find_guide function which returns a dict

print(found_guide.get("title")) # get various dict members
print(found_guide.get("difficulty"))
````

#### Getting a guide *with prerequisites*

````py
found_guide = find_guide(123, get_prerequisites=True) # call the find_guide function which returns a dict

print(found_guide.get("title")) # get various dict members
print(found_guide.get("difficulty"))
````

## Full example

````py
from fixitpy import find_guide

found_guide = find_guide(123) # call the find_guide function which returns a dict

print(found_guide.get("title")) # get various dict members
print(found_guide.get("difficulty"))
````
---
