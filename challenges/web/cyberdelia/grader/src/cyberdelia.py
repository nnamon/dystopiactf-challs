#!/usr/bin/env python

from bottle import error, request, route, run, static_file, template
from calendar import timegm
from datetime import datetime

timeslots = [datetime(2015, 6, day, hour, 0)
             for day in range(13, 16)
             for hour in range(18, 23)]

timeslots = [[slot.strftime('%d %B %Y'), slot.strftime('%H:%M'), timegm(slot.timetuple())]
             for slot in timeslots]

@error(404)
@error(500)
def error500(error):
        return template('wtf')

@route('/images/<filename>')
def send_image(filename):
        return static_file(filename, root='views/resources/')

@route('/')
def select_booking():
    return template('booking', timeslots=timeslots)

@route('/booking', method='POST')
def perform_booking():
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    email = request.forms.get('email')
    epoch = int(request.forms.get('timeslot'))

    flag = ''

    if epoch == 1434135600:
        flag = 'flag{4ll_R3aDY_2_p4rt4y_yAy}'

    selected = datetime.fromtimestamp(epoch)
    confirm_slot = [selected.strftime('%d %B %Y'), selected.strftime('%H:%M')]

    return template('confirmation',
                    timeslot=confirm_slot,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    flag=flag)

run(host='localhost', port=8080, debug=True)
