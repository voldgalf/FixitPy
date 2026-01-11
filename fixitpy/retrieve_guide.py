"""FixitPy package."""

from typing import Optional

import requests

IFIXIT_API_URL = 'https://www.ifixit.com/api/2.0'

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
        image_ids = []
        for _line in _step.get('lines', []):
            if _line.get('text_raw'):
                lines.append(_line.get('text_raw'))

        step_data_type = _step.get('media').get('type')

        if step_data_type and step_data_type == 'image':
            for _data in _step.get('media').get('data', []):
                image_ids.append(_data.get('id'))

        step_instance = {"title": _step.get('title'),
                         "text": " ".join(lines),
                         "image_id": image_ids}

        steps.append(step_instance)


    return {
        "title": response_json.get("title"),
        "steps": steps,
        "summary": response_json.get("summary"),
        "type": response_json.get("type"),
        "conclusion": response_json.get("conclusion_raw"),
        "difficulty": response_json.get("difficulty"),
        "introduction": response_json.get("introduction_raw"),
        "image_id": response_json.get("image").get("id"),
        "guide_id": response_json.get("guideid")
    }
