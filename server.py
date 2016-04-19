# server.py
from flask import Flask, render_template, request
from worker import mytask

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/runtask', methods=['POST'])
def runtask():
    clientid = request.form.get('clientid')
    mytask.delay(clientid=clientid)
    return 'running task...', 202

# vim: set ai ts=4 sw=4 et sts=4
