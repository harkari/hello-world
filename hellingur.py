from bottle import run, route, template

@route('/string')
def strengurinn():
	return "Hello world!"

@route('/html')
def htmlsida():
	return "<h1>Hello world!</h1>"

@route('/temp')
def templateskjal():
	return template('temper')

@route('/send')
def sending():
	name="Thorarinn"
	setning="How are you today  "

	return template('sending', n=name, s=setning)

run(host='localhost', port=8080, debug=True , reloader=True)
