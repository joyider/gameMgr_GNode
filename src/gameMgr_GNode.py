from flask import Flask, jsonify, abort, make_response, request

import time
import socket
import psutil as PU
from functools import wraps
from NoJoy_DI.di import DI
from NoJoy_DI.patterns import SingletonPattern

app = Flask(__name__)


def fn_timer(function):
	"""

	:param function:
	:return:
	"""

	@wraps(function)
	def function_timer(*args, **kwargs):
		t0 = time.time()
		result = function(*args, **kwargs)
		t1 = time.time()
		print("Total time running %s: %s seconds" %
		      (function.func_name, str(t1 - t0))
		      )
		return result

	return function_timer


def get_system_info():
	cpu_percent = PU.cpu_percent(interval=3, percpu=False)
	mem_percent = PU.virtual_memory().percent
	disk_percent = PU.disk_usage('/')
	if socket.gethostname().find('.') >= 0:
		hostname = socket.gethostname()
	else:
		hostname = socket.gethostbyaddr(socket.gethostname())[0]
	ip = PU.net_if_addrs()
	return {'ip' : ip, 'hostname' : hostname, 'cpu' : cpu_percent, 'memory' : mem_percent, 'disk_usage' : disk_percent.__str__().replace("sdiskusage(", "").replace(")", "").split('percent=')[-1]}

@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/api/v1.0/default', methods=['GET'])
def get_nodestatus():
	return jsonify({'sysinfo' : get_system_info()})


if __name__ == '__main__':
	app.run()
