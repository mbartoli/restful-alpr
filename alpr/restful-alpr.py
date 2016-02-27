from flask import Flask, request
from flask_restful import Resource, Api
import subprocess
import os
import json

app = Flask(__name__)
api = Api(app)

todos = {}

class alprAPI(Resource):
    def alpr(self, url):
	ext = url.split(".")[-1]
	os.popen('curl -o input.'+ext+' '+url)
	output = os.popen('alpr -j input.'+ext).read().rstrip("\n")
	return output
    
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
	url = request.form['data']
	raw = self.alpr(url)
	formatted_json = json.loads(raw)
	return formatted_json


api.add_resource(alprAPI, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
