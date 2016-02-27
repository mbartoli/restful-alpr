from flask import Flask, request
from flask_restful import Resource, Api
import ner
import subprocess
import os
import re

app = Flask(__name__)
api = Api(app)

todos = {}

class alprAPI(Resource):
    def alpr(url):
	ext = url.split(".")[-1]
	os.popen('curl -o image.'+ext+' '+url)
	proc = subprocess.Popen(["alpr", "image."+ext], stdout=subprocess.PIPE, shell=True)
	(output, err) = proc.communicate()
	return output
    
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
	url = request.form['data']
	return alprAPI(url)

api.add_resource(alprAPI, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
