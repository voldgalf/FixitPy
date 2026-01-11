# fixitPy
[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/voldgalf/fixitpy)
![PyPI - License](https://img.shields.io/pypi/l/fixitpy)
[![PyPI](https://img.shields.io/badge/PyPI-3775A9?logo=pypi&logoColor=fff)](https://pypi.org/project/fixitpy/)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/voldgalf)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/50calibursword)

Python iFixit API interface.

Currently, you can retrieve guides and their prerequisite guides
## Installation

````bash
pip install fixitpy
````

## Using the library

### Retrieving a guide *without prerequisites*

This returns a dict that contains information pertaining to the guide

````py
import fixitpy

found_guide = fixitpy.retrieve_guide(123) # call the retrieve_guide function which returns a dict

print(found_guide.get("title"))
print(found_guide.get("difficulty"))
````

### Retrieving a guide *with prerequisites*

A prerequisite is an optional guide that the retrieved guide recommends you start with before. The prerequisite guide is the same dict structure of what returns from `fixitpy.retrieve_guide`

````py
import fixitpy

found_guide = fixitpy.retrieve_guide(123, get_prerequisites=True) # call the retrieve_guide function which returns a dict

print(found_guide.get("title"))
print(found_guide.get("difficulty"))

first_prerequisite = found_guide.get("prerequisites")[0]
print(first_prerequisite.get("title"))
````

### Getting Guide Steps

What makes a repair guide, a *guide* is the inclusion of steps to follow.

````py
import fixitpy

found_guide = fixitpy.retrieve_guide(123) # call the retrieve_guide function which returns a dict

print(found_guide.get("title"))
print(found_guide.get("difficulty"))

for step in found_guide.get("steps"):
    print(step.get("title")) # this is the title of each step
    print(step.get("steps")) # this is a list of each sentence of the current step
````

# License

MIT License
