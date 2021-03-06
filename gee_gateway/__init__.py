from flask import Blueprint

gee_gateway = Blueprint('gee_gateway', __name__, template_folder='templates', static_folder='static', static_url_path='/static/gee_gateway')

from . import gee, web

def gee_initialize(ee_account='', ee_key_path='', ee_user_token=''):
    gee.utils.initialize(ee_account=ee_account, ee_key_path=ee_key_path, ee_user_token=ee_user_token)
