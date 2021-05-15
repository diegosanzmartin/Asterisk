#!/usr/bin/python
# -*- coding: utf-8 -*- 

from flask import Flask, url_for, session, render_template, Response, request, flash, redirect, abort, jsonify
from flask_restful import Resource, Api
from random import randint
import json
import time

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('IROOM_SETTINGS', silent=True)
#export IROOM_SETTINGS=/home/usu/Iroom/config/iroom.cfg
api = Api(app)

@app.route('/')
def main(): 
	return render_template('index.html')
		
@app.route('/sensors')
def sensors():
	return render_template('sensors.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('Has entrado en la sesion')
			return redirect(url_for('sensors'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('Has salido de la sesion')
	return redirect(url_for('main'))

class temperature(Resource):
	def get(self):
		value = randint(18,23)
		return {'temperature': value}

class humidity(Resource):
	def get(self):
		value = randint(29,61)
		return {'humidity': value}

class light(Resource):
	def get(self):
		value = randint(0,100)
		return {'light': value}

class sound(Resource):
	def get(self):
		value = randint(20,80)
		return {'sound': value}

class motion(Resource):
	def get(self):
		value = randint(0,1)
		return {'motion': value}

class red(Resource):
	def put(self, id):
		print ("Color rojo:"+str(id))
		return {'red': id}

class green(Resource):
	def put(self, id):
		print ("Color verde:"+str(id))
		return {'green': id}

class blue(Resource):
	def put(self, id):
		print ("Color azul:"+str(id))
		return {'blue': id}


api.add_resource(temperature, '/temperature')
api.add_resource(humidity, '/humidity')
api.add_resource(light, '/light')
api.add_resource(sound, '/sound')
api.add_resource(motion, '/motion')
api.add_resource(red, '/red/<int:id>')
api.add_resource(green, '/green/<int:id>')
api.add_resource(blue, '/blue/<int:id>')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)