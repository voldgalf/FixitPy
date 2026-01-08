"""FixitPy package."""

import requests

IFIXIT_API_URL = 'https://www.ifixit.com/api/2.0'


def find_guide(guide_id, get_prerequisites=False):
    """
        Retrieve an iFixit guide given the guide ID.

        Parameters:
        guide_id (int): The ID for the guide requested.
        get_prerequisites (bool): Whether to return a guide's prerequisites.

        Returns:
        dict: A dictionary containing the guide's information.
    """

    request_url = f"{IFIXIT_API_URL}/guides/{guide_id}"

    response = requests.get(request_url,allow_redirects=False, timeout=5)

    if response.status_code != 200:
        return None

    if 'application/json' not in response.headers.get('Content-Type', ''):
        return None

    response_json = response.json()

    steps = []

    for _step in response_json.get('steps', []):
        lines = []
        for _line in _step.get('lines', []):
            if _line.get('text_raw'):
                lines.append(_line.get('text_raw'))

        step_instance = {"title": _step.get('title'), "steps": lines}
        steps.append(step_instance)

    prerequisites = []

    if get_prerequisites:

        for _prerequisite in response_json.get('prerequisites', []):
            prerequisites_guide = find_guide(_prerequisite.get('guideid'), get_prerequisites=False)
            prerequisites.append(prerequisites_guide)

    return {"title": response_json.get("title"),
            "steps": steps,
            "conclusion": response_json.get("conclusion_raw"),
            "difficulty": response_json.get("difficulty"),
            "introduction": response_json.get("introduction_raw"),
            "prerequisites": prerequisites,
            "guide_id": response_json.get("guideid")}

if __name__ == "__main__":
    guide = find_guide(6020, get_prerequisites=False)
    if guide:
        print(guide.get("title"))
        print(f"Difficulty: {guide.get('difficulty')}")
        print(f"Introduction: {guide.get('introduction')}")
