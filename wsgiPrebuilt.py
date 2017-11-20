import wsgiserver


def my_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['WSGI server is running!', ' Here is a message.', ' \nHere is an additional message.']


server = wsgiserver.WSGIServer(my_app)
server.start()
