from flask import Flask, Response, request

app = Flask(__name__)

@app.route("/home")
def starting_url():
	status_code = Response(status=200)
	return status_code

@app.route('/number/<num>')
def number(num):
	result = num
	try:
		return Response(result , mimetype='text/html')
	except Exception as ex:
		print(ex)
		return Response(status=500)

if __name__ == '__main__':
	app.run(debug=False, port=8000, host='0.0.0.0')
