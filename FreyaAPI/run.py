from flask import Flask
from flask import request,jsonify, make_response,abort
import importlib


"""
 Aplication flask for Freya, name FreyaAPI 
"""


app = Flask(__name__)

@app.route('/')
def hello():    
    return 'Hello, New World Falling Into Darkness'

"""
Rute 
"""
@app.route('/Get_Lc',methods=['POST'])
def get_lc_all():
    ra = request.form['ra']
    dec = request.form['dec']
    radius = request.form['radius']
    format = request.form['format']
    data = {}
    for catalog in request.form['catalogs'].split(","):
        module = f'resources.{catalog}_resource.resource'
        print(module)
        mod = importlib.import_module(module)
        my_class = getattr(mod, f'Resource_{catalog}')
        my_instance = my_class(ra=ra,dec=dec,radius=radius,format=format).get_lc_deg_all()
        data[f'{catalog}'] = my_instance
    return make_response(data)

@app.route('/Get_LC_Nearest',methods=['POST'])
def get_lc_nearest():
    data = {}
    ra = request.form['ra']
    dec = request.form['dec']
    radius = request.form['radius']
    format = request.form['format']
    for catalog in request.form['catalogs'].split(","):
        module = f'resources.{catalog}_resource.resource'
        mod = importlib.import_module(module)
        my_class = getattr(mod, f'Resource_{catalog}')
        my_instance = my_class(ra=ra,dec=dec,radius=radius,format=format).get_lc_deg_nearest()
        data[f'{catalog}'] = my_instance
    return make_response(data)

@app.route('/Get_LC_Hms',methods=['POST'])
def get_lc_hms_all():
    data = {}
    hms = request.form['hms']
    radius = request.form['radius']
    format = request.form['format']
    for catalog in request.form['catalogs'].split(","):
        module = f'resources.{catalog}_resource.resource'
        mod = importlib.import_module(module)
        my_class = getattr(mod, f'Resource_{catalog}')
        my_instance = my_class(hms=hms,radius=radius,format=format).get_lc_hms_all()
        data[f'{catalog}'] = my_instance
    return make_response(data)

@app.route('/Get_LC_Hms_Nearest',methods=['POST'])
def get_lc_hms_nearest():
    data = {}
    hms = request.form['hms']
    radius = request.form['radius']
    format = request.form['format']
    for catalog in request.form['catalogs'].split(","):
        module = f'resources.{catalog}_resource.resource'
        mod = importlib.import_module(module)
        my_class = getattr(mod, f'Resource_{catalog}')
        my_instance = my_class(hms=hms,radius=radius,format=format).get_lc_hms_nearest()
        data[f'{catalog}'] = my_instance
    return make_response(data)


if __name__ == '__main__':
    app.run('0.0.0.0',5000,debug=True)