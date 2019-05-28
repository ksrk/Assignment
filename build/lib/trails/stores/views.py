from functools import partial
from flask import Blueprint, render_template
from trails.stores.models import Stores
from trails.helpers.postcodes import find_the_distance
blueprint = Blueprint('stores', __name__, template_folder='templates')

stores_obj = Stores('stores.json')


@blueprint.route('/', methods=['GET'])
def get_stores():
    return render_template('stores/stores.html',
                           title='Stores',
                           headers=stores_obj.headers,
                           stores=stores_obj.stores)


@blueprint.route('/<string:postcode>/<int:radius>', methods=['GET'])
def get_stores_radius(postcode, radius):
    postcode = postcode.replace(' ', '')
    source = next((store for store in stores_obj.stores
                   if store.get('postcode', None) == postcode), None)
    stores_in_radius = []
    if source:
        distance = partial(find_the_distance, source)
        stores_in_radius = [item for item in stores_obj.stores
                            if radius > distance(item)]
    return render_template('stores/stores.html',
                           title='Stores',
                           headers=stores_obj.headers,
                           stores=stores_in_radius)
