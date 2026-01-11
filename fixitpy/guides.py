"""FixitPy package."""

from typing import Optional

import requests

IFIXIT_API_URL = 'https://www.ifixit.com/api/2.0'

def retrieve_media(media_id: int) -> Optional[dict]:
    """Example function with types documented in the docstring.

    Parameters
    ----------
    media_id : int
        The ID for the media requested.

    Returns
    -------
    dict
        Contains information about the media.

    """

    request_url = f"{IFIXIT_API_URL}/media/images/{media_id}"

    response = requests.get(request_url, allow_redirects=False, timeout=5)

    if response.status_code != 200:
        return {}

    if 'application/json' not in response.headers.get('Content-Type', ''):
        return {}

    response_json = response.json()

    size_json = {}

    for size in response_json.get('image', {}).items():
        if not size[0] in ["id", "guid"]:
            size_json[size[0]] = size[1]

    return {
        'media_id': response_json.get('image', {}).get('id'),
        'width': response_json.get('width'),
        'height': response_json.get('height'),
        'sizes' : size_json,
    }

def retrieve_guide(guide_id: int) -> Optional[dict]:
    """Example function with types documented in the docstring.

    Parameters
    ----------
    guide_id : int
        The ID for the guide requested.
    Returns
    -------
    dict
        Contains information about the guide.

    """

    request_url = f"{IFIXIT_API_URL}/guides/{guide_id}"

    response = requests.get(request_url, allow_redirects=False, timeout=5)

    if response.status_code != 200:
        return {}

    if 'application/json' not in response.headers.get('Content-Type', ''):
        return {}

    response_json = response.json()

    steps = []

    for _step in response_json.get('steps', []):
        lines = []
        for _line in _step.get('lines', []):
            if _line.get('text_raw'):
                lines.append(_line.get('text_raw'))

        step_instance = {"title": _step.get('title'), "text": " ".join(lines)}
        steps.append(step_instance)


    return {
        "title": response_json.get("title"),
        "steps": steps,
        "conclusion": response_json.get("conclusion_raw"),
        "difficulty": response_json.get("difficulty"),
        "introduction": response_json.get("introduction_raw"),
        "guide_id": response_json.get("guideid")
    }

if __name__ == "__main__":

    found_media = retrieve_media(14)
    print(found_media)

    found_guide = retrieve_guide(123)  # call the retrieve_guide function which returns a dict

    print(found_guide.get("title"))
    print(found_guide.get("difficulty"))

    for step in found_guide.get("steps"):
        print(step.get("title"))
        print(step.get("text"))
