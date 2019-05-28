import json
import os
from trails.helpers.postcodes import get_details
from trails.helpers.singleton import Singleton


class Stores(metaclass=Singleton):
    def __init__(self, filename):
        self._filename = filename
        self._stores = []
        self._headers = ('name', 'postcode', 'latitude', 'longitude')

    @property
    def stores(self):
        if self._stores:
            return self._stores
        else:
            return self.get_stores_locations()

    @property
    def headers(self):
        return self._headers

    def _get_stores(self):
        stores = []
        directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(directory, 'data', self._filename)) as fh:
            stores = json.load(fh)
            stores = sorted(stores, key=lambda item: item['name'])

        return stores

    def get_stores_locations(self):
        print('getting stores data')
        self._stores = self._get_stores()
        for store in self._stores:
            postcode_data = get_details(store.get('postcode'))
            postcode_data['postcode'] = store.get('postcode').replace(' ', '')
            store.update(**postcode_data)
        return self._stores
