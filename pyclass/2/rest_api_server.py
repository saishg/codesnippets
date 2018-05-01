from bottle import route, response, request, run
import time
import algebra
import subprocess

@route('/')
def welcome():
    return '<h1>Howdy!</h1>\n'

@route('/now')
def show_time():
    response.content_type = 'text/plain'
    response.set_header('Cache-Control', 'max-age=100')
    return time.ctime() + '\n'

@route('/interfaces')
def show_netstat():
    response.content_type = 'text/plain'
    result = subprocess.check_output(['netstat', '-i'])
#    result = result.replace("\n", "<br>\n")
    return result

@route('/area/circle')
def circle_area_service():
    radius = float(request.query.get('radius', '0'))
    area = algebra.area_circle(radius)
    return dict(area=area, radius=radius, service=request.path)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
