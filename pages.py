import requests
from typing import Optional
from decors import timer


@timer
def get_response(url: str, auth: Optional[tuple] = None):
    response = requests.get(url=url, auth=auth)
    return response
