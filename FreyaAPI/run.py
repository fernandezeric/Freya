#poner todo junto por mientras la aplicacion flask sencilla

"""

"""
from flask import Flask
from flask import request,send_file,jsonify, make_response,abort
import importlib

app = Flask(__name__)

def call_resource(names_resources,ra,dec,radius,format):
    data = {}
    for catalog in names_resources:
        module = f'resources.{catalog}_resource.resource_name' # importa el archivo
        mod = importlib.import_module(module) # importa el archivo
        my_class = getattr(mod, 'resource') # llama a la clase
        my_instance = my_class(catalog=catalog,ra=ra,dec=dec,radius=radius,format=format).get_lc_deg_all()# llama al metodo de la clase
        data[f'{catalog}'] = my_instance
    return data

@app.route('/')
def hello():    
    return 'Hello, World!'

@app.route('/Get_Lc')
def get_lc_all():
    #request.form['XXX'] para post
    ra = request.args.get('ra')
    dec = request.args.get('dec')
    radius = request.args.get('radius')
    format = request.args.get('format')
    data = {}
    for catalog in request.args.get('catalogs').split(","):
        module = f'resources.{catalog}_resource.resource'
        mod = importlib.import_module(module)
        my_class = getattr(mod, 'resource')
        my_instance = my_class(catalog=catalog,ra=ra,dec=dec,radius=radius,format=format).get_lc_deg_all()
        data[f'{catalog}'] = my_instance
    return data

@app.route('/Get_LC_Nearest') #methods=['POST']
def get_lc_nearest():
    data = {}
    ra = request.args.get('ra')
    dec = request.args.get('dec')
    radius = request.args.get('radius')
    format = request.args.get('format')
    for catalog in request.args.get('catalogs').split(","):
        module = f'resources.{catalog}_resource.resource'
        mod = importlib.import_module(module)
        my_class = getattr(mod, 'resource')
        my_instance = my_class(catalog=catalog,ra=ra,dec=dec,radius=radius,format=format).get_lc_deg_nearest()
        data[f'{catalog}'] = my_instance
    return data

@app.route('/Get_LC_Hms')#methods=['POST']
def get_lc_hms_all():
    data = {}
    hms = request.args.get('hms')
    radius = request.args.get('radius')
    format = request.args.get('format')
    for catalog in request.args.get('catalogs').split(","):
        module = f'resources.{catalog}_resource.resource'
        mod = importlib.import_module(module)
        my_class = getattr(mod, 'resource')
        my_instance = my_class(catalog=catalog,hms=hms,radius=radius,format=format).get_lc_hms_all()
        data[f'{catalog}'] = my_instance
    return data

@app.route('/Get_LC_Hms_Nearest')#methods=['POST']
def get_lc_hms_nearest():
    data = {}
    hms = request.args.get('hms')
    radius = request.args.get('radius')
    format = request.args.get('format')
    for catalog in request.args.get('catalogs').split(","):
        module = f'resources.{catalog}_resource.resource'
        mod = importlib.import_module(module)
        my_class = getattr(mod, 'resource')
        my_instance = my_class(catalog=catalog,hms=hms,radius=radius,format=format).get_lc_hms_nearest()
        data[f'{catalog}'] = my_instance
    return data


if __name__ == '__main__':
    app.run('0.0.0.0',5000,debug=True)

"""
export FLASK_APP=run
"""