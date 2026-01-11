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