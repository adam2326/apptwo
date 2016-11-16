from flask import Flask, render_template, request, url_for, redirect
import datetime
from random import randint

myapp = Flask(__name__)



@myapp.route('/one', methods=['GET', 'POST'])
def first():
	if request.method == 'GET':
		return render_template('main_page.html')
	else:
		return redirect(url_for('second'))


@myapp.route('/two', methods=['GET', 'POST'])
def second():
	if request.method == 'GET':
		# make an api call here and add the variable information to the information passed to the website as in the next step
		current_datetime = datetime.datetime.now()
		return render_template('second_page.html', current_datetime=current_datetime)
	else:
		return redirect(url_for('third'))

@myapp.route('/three', methods=['GET','POST'])
def third():
	if request.method == 'GET':
		return render_template('third_page.html', random_number=randint(0,9))
	else:
		return render_template('main_page.html')


if __name__ == '__main__':
	myapp.run(threaded=True)
