from flask import Flask
from flask import request,jsonify, make_response,abort
from astropy.io import ascii
from astropy.table import Table,vstack
import io
import importlib


"""
Aplication flask for Freya, name FreyaAPI.
"""


app = Flask(__name__)

"""
Base rute
"""
@app.route('/')
def hello():    
    return 'Hello, New World Falling Into Darkness'

"""
Rute that gets light curve data from catalogs,
use specific area in degrees.
--------------------------------------

Parameters

catalogs (string) : string with contains the names of catalogs separated with coma.
ra (float): (degrees) Right Ascension
dec (float): (degrees) Declination
radius (float): Search radius
format (string): csv,

"""
@app.route('/get_lc_original')
def get_lc_original():
    ra = request.args.get('ra')
    dec = request.args.get('dec')
    radius = request.args.get('radius')
    format = request.args.get('format')
    data = {}
    for catalog in request.args.get('catalogs').split(","):
        module = f'resources.{catalog}_resource.resource'
        mod = importlib.import_module(module)
        my_class = getattr(mod, f'Resource_{catalog}')
        my_instance = my_class(ra=ra,dec=dec,radius=radius,format=format).get_lc_deg_all()
        data[f'{catalog}'] = my_instance
    return make_response(data)


@app.route('/get_lc')
def get_lc_all():
    ra = request.args.get('ra')
    dec = request.args.get('dec')
    radius = request.args.get('radius')
    format = request.args.get('format')
    first = True
    data = ''
    for catalog in request.args.get('catalogs').split(","):
        module = f'resources.{catalog}_resource.resource'
        print(module)
        mod = importlib.import_module(module)
        my_class = getattr(mod, f'Resource_{catalog}')
        my_instance = my_class(ra=ra,dec=dec,radius=radius,format=format).get_lc_deg_all()
        # who read csv in astropy
        if format == 'csv':
            if first :
                my_instance_ = ascii.read(my_instance)
                my_instance_.add_column(f'{catalog}',name='catalogue')
                results_ = my_instance_
                first = False
            else :
                my_instance_ = ascii.read(my_instance)
                my_instance_.add_column(f'{catalog}',name='catalogue')
                results_ = vstack([results_,my_instance_])
    #
    if format == 'csv':
        buf = io.StringIO()
        ascii.write(results_,buf,format='csv')
        # make responde data with headers
        data =  make_response(buf.getvalue())
        data.headers["Content-Disposition"] = "attachment; filename=.csv"
        data.headers["Content-type"] = "text/csv"
        return data
"""
Rute that get the light curve data most close to specific area in degrees
from catalogs indicateds,
--------------------------------------

Parameters

catalogs (string) : string with contains the names of catalogs separated with coma.
ra (float): (degrees) Right Ascension
dec (float): (degrees) Declination
radius (float): Search radius
format (string): csv,

"""
@app.route('/get_lc_nearest')
def get_lc_nearest():
    ra = request.args.get('ra')
    dec = request.args.get('dec')
    radius = request.args.get('radius')
    format = request.args.get('format')
    first = True
    data = ''
    for catalog in request.args.get('catalogs').split(","):
        module = f'resources.{catalog}_resource.resource'
        print(module)
        mod = importlib.import_module(module)
        my_class = getattr(mod, f'Resource_{catalog}')
        my_instance = my_class(ra=ra,dec=dec,radius=radius,format=format).get_lc_deg_nearest()
        # who read csv in astropy
        if format == 'csv':
            if first :
                my_instance_ = ascii.read(my_instance)
                my_instance_.add_column(f'{catalog}',name='catalogue')
                results_ = my_instance_
                first = False
            else :
                my_instance_ = ascii.read(my_instance)
                my_instance_.add_column(f'{catalog}',name='catalogue')
                results_ = vstack([results_,my_instance_])
    #
    if format == 'csv':
        buf = io.StringIO()
        ascii.write(results_,buf,format='csv')
        # make responde data with headers
        data =  make_response(buf.getvalue())
        data.headers["Content-Disposition"] = "attachment; filename=.csv"
        data.headers["Content-type"] = "text/csv"
        return data

"""
Rute that get the light curve data most close to specific area in
format hh:mm:ss from catalogs indicateds,
--------------------------------------

Parameters

catalogs (string) : string with contains the names of catalogs separated with coma.
hms (string): format hh:mm:ss
radius (float): Search radius
format (string): csv,

"""
@app.route('/get_lc_hms')
def get_lc_hms_all():
    hms = request.args.get('hms')
    radius = request.args.get('radius')
    format = request.args.get('format')
    first = True
    data = ''
    for catalog in request.args.get('catalogs').split(","):
        module = f'resources.{catalog}_resource.resource'
        print(module)
        mod = importlib.import_module(module)
        my_class = getattr(mod, f'Resource_{catalog}')
        my_instance = my_class(ra=ra,dec=dec,radius=radius,format=format).get_lc_hms_all()
        # who read csv in astropy
        if format == 'csv':
            if first :
                my_instance_ = ascii.read(my_instance)
                my_instance_.add_column(f'{catalog}',name='catalogue')
                results_ = my_instance_
                first = False
            else :
                my_instance_ = ascii.read(my_instance)
                my_instance_.add_column(f'{catalog}',name='catalogue')
                results_ = vstack([results_,my_instance_])
    #
    if format == 'csv':
        buf = io.StringIO()
        ascii.write(results_,buf,format='csv')
        # make responde data with headers
        data =  make_response(buf.getvalue())
        data.headers["Content-Disposition"] = "attachment; filename=.csv"
        data.headers["Content-type"] = "text/csv"
        return data

"""
Rute that gets light curve data from catalogs,
use specific area in format hh:mm:ss.
--------------------------------------

Parameters

catalogs (string) : string with contains the names of catalogs separated with coma.
hms (string): format hh:mm:ss
radius (float): Search radius
format (string): csv,

"""
@app.route('/get_lc_hms_nearest',methods=['POST'])
def get_lc_hms_nearest():
    hms = request.args.get('hms')
    radius = request.args.get('radius')
    format = request.args.get('format')
    first = True
    data = ''
    for catalog in request.args.get('catalogs').split(","):
        module = f'resources.{catalog}_resource.resource'
        print(module)
        mod = importlib.import_module(module)
        my_class = getattr(mod, f'Resource_{catalog}')
        my_instance = my_class(hms=hms,radius=radius,format=format).get_lc_hms_nearest()
        # who read csv in astropy
        if format == 'csv':
            if first :
                my_instance_ = ascii.read(my_instance)
                my_instance_.add_column(f'{catalog}',name='catalogue')
                results_ = my_instance_
                first = False
            else :
                my_instance_ = ascii.read(my_instance)
                my_instance_.add_column(f'{catalog}',name='catalogue')
                results_ = vstack([results_,my_instance_])
    #
    if format == 'csv':
        buf = io.StringIO()
        ascii.write(results_,buf,format='csv')
        # make responde data with headers
        data =  make_response(buf.getvalue())
        data.headers["Content-Disposition"] = "attachment; filename=.csv"
        data.headers["Content-type"] = "text/csv"
        return data


if __name__ == '__main__':
    app.run('0.0.0.0',5000,debug=True)