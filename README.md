# fixitPy

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
