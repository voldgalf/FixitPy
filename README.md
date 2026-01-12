<div align="center">
<img src="logo.png" alt="Alt Text" width=50%>
</div>

[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/voldgalf/fixitpy)
![PyPI - License](https://img.shields.io/pypi/l/fixitpy)
[![PyPI](https://img.shields.io/badge/PyPI-3775A9?logo=pypi&logoColor=fff)](https://pypi.org/project/fixitpy/)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/voldgalf)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/50calibursword)
[![Static Badge](https://img.shields.io/badge/Documentation-blue)](https://fixitpy.readthedocs.io/en/latest/)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/fixitpy)

FixitPy is an uncomplicated Python library for interfacing with iFixit's API.

Allowing repair guides to be programmatically retrieved.
## Installation

````bash
pip install fixitpy
````

## Usage

### Guide retrieval

````py
import fixitpy

# Call 'retrieve_guide' returns the guide's dictionary
found_guide = fixitpy.retrieve_guide(123)

# As any regular dictionary, you can retrieve specific values from it
print(f"Title: {found_guide.get("title")}")
print(f"Difficulty: {found_guide.get("difficulty")}")
print(f"Conclusion: {found_guide.get("conclusion")}")

# The dictionary returned from 'retrieve_guide' contains a list refered to as 'steps'
# Each list item contains a dictionary with the properties 'title', which is self explanatory and 'text', the process itself.
for step in found_guide.get("steps"):
    print(step.get("title"))
    print(step.get("text"))

````

### Media retrieval

````py
import fixitpy

# Call 'retrieve_media', returns the media's dictionary
found_guide = fixitpy.retrieve_media(123)

# As any regular dictionary, you can retrieve specific values from it
print(found_guide.get("width"))
print(found_guide.get("height"))

# The dictionary returned from 'retrieve_media' contains a sub-dictionary under 'sizes'
# Which contains all the sizes of the media and their corresponding URLs.
sizes = found_guide.get("sizes")

# 'thumbnail' is a very common size for iFixit Media
print(sizes.get("thumbnail"))

````

# License

MIT License
