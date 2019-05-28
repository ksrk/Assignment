from http import HTTPStatus
import json
import math
from typing import Dict
import requests

url = 'https://api.postcodes.io/postcodes/{}'


def get_details(postcode: str) -> Dict:
    '''
    Get postcode data from postcode.io
    '''
    response = requests.get(url.format(postcode))
    if response.status_code == HTTPStatus.OK:
        try:
            res_dict = json.loads(response.text)
        except json.JSONDecodeError:
            return {}
        return res_dict.get('result', {})
    return {}


def find_the_distance(source: Dict, target: Dict) -> float:
    '''
    Find the distance between two coordinates
    '''
    d_lat = math.radians(target.get('latitude', 0) - source.get('latitude', 0))
    d_lng = math.radians(target.get('longitude', 0)
                         - source.get('longitude', 0))
    lat1 = math.radians(source.get('latitude', 0))
    lat2 = math.radians(target.get('latitude', 0))
    temp = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * \
           math.sin(d_lng / 2) ** 2
    return 6373.0 * (2 * math.atan2(math.sqrt(temp), math.sqrt(1 - temp)))
