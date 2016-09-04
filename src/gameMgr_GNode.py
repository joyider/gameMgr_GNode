from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/api/v1.0/default', methods=['GET'])
def get_nodestatus():
	return


if __name__ == '__main__':
	app.run()
