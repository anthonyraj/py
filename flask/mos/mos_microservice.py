#http://flask.pocoo.org/docs/0.12/quickstart/

from flask import Flask,request,json
from mos import MOS

app = Flask(__name__)
mos = MOS()

# Utility methods
# HTML Entity conversion    
html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

def _extract_post_param(request,params):
    request_data = {}

    for k,v in params.items():
        if k in request.form:
            request_data[k] = html_escape(request.form[k])
        else:
            if v == 'str':request_data[k] = ''
            elif v == 'json':request_data[k] = []

    return request_data

def _extract_get_param(request,params):
    # Parse the prams and check if the required parameters are present in the request object
    # If the parameters are present, then extract them and add to request_data object
    request_data = {}

    for k,v in params.items():
        if k in request.args:
            if v == 'str': request_data[k] = html_escape(request.args.get(k))
            elif v == 'int': request_data[k] = request.args.get(k, 0, type=int)
            elif v == 'json': request_data[k] = json.loads(request.args.get(k))
        else:
            if v == 'str':request_data[k] = ''
            elif v == 'int':request_data[k] = 0
            elif v == 'json':request_data[k] = []

    return request_data

def _request_parser(request,params):
    #params = {'project_id':'int','task_id':'int','entity_type':'str','entity_name':'str'}
    if request.method == 'POST':
        request_data = _extract_post_param(request,params)

    if request.method == 'GET':
        request_data = _extract_get_param(request,params)

    return request_data  

# MOS APIs
@app.route('/create_process')
def create_process():
	params = {'process_name':'str'}
	r = _request_parser(request,params)
	return mos.create_process(r['process_name'])

@app.route('/create_flow')
def create_flow_for_process():
	params = {'process_name':'str','flow_name':'str'}
	r = _request_parser(request,params)
	return mos.create_flow_for_process(r['process_name'],r['flow_name'])

@app.route('/delete_flow')
def delete_flow():
	params = {'flow_name':'str'}
	r = _request_parser(request,params)
	return mos.delete_flow(r['flow_name'])

@app.route('/create_flowstep')
def create_flow_step_for_flow():
	params = {'flow_name':'str','flowstep_name':'str'}
	r = _request_parser(request,params)
	return mos.create_flow_step_for_flow(r['flow_name'],r['flowstep_name'])

@app.route('/delete_flowstep')
def delete_flow_step_for_flow():
	params = {'flow_name':'str','flowstep_name':'str'}
	r = _request_parser(request,params)
	return mos.delete_flow_step_for_flow(r['flow_name'],r['flowstep_name'])

@app.route('/get_process_info')
def get_process_info():
	params = {'process_name':'str'}
	r = _request_parser(request,params)
	return json.dumps(mos.get_process_info(r['process_name']))

@app.route('/get_flow_info')
def get_flow_info():
	params = {'flow_name':'str'}
	r = _request_parser(request,params)
	return json.dumps(mos.get_flow_info(r['flow_name']))

@app.route('/update_flow')
def update_flow():
	params = {'flow_name':'str','order':'json'}
	r = _request_parser(request,params)
	return mos.update_flow(r['flow_name'],r['order'])

# Test cases
@app.route('/test')
def test():
	params = {'process_name':'str','flow_name':'str'}
	r = _request_parser(request,params)
	return json.dumps(r)
