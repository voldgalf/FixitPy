# fixitPy
![Static Badge](https://img.shields.io/badge/github-fixitpy-blue%3F?link=https%3A%2F%2Fgithub.com%2Fvoldgalf%2Ffixitpy)
![PyPI - License](https://img.shields.io/pypi/l/fixitpy)
![Static Badge](https://img.shields.io/badge/coverage-100%25-orange)

Python iFixit API interface.

Currently you can retrieve guides and their prerequisite guides
## Installation

To install fixitPy

````bash
pip install fixitpy
````

### Using the library

#### Retrieving a guide *without prerequisites*

This returns a dict that contains information pertaining to the guide

````py
import fixitpy

found_guide = fixitpy.retrieve_guide(123) # call the retrieve_guide function which returns a dict

print(found_guide.get("title"))
print(found_guide.get("difficulty"))
````

#### Retrieving a guide *with prerequisites*

A prerequisite is an optional guide that the retrieved guide recommends you start with before. The prerequisite guide is the same dict structure of what returns from `fixitpy.retrieve_guide`

````py
import fixitpy

found_guide = fixitpy.retrieve_guide(123, get_prerequisites=True) # call the retrieve_guide function which returns a dict

print(found_guide.get("title"))
print(found_guide.get("difficulty"))

first_prerequisite = found_guide.get("prerequisites")[0]
print(first_prerequisite.get("title"))
````

# License

MIT License
