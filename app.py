import os

from flask import abort, Flask, redirect, render_template, Response, request, url_for

from mongoengine.errors import ValidationError

from db import db
from documents import Restaurant


app = Flask(__name__)

mongodb_settings = {
    'db': 'randomizer'
}

# Try to get the mongolab connection information from the environment.
try:
	mongodb_settings['host'] = os.environ['MONGOLAB_URI']
except KeyError:
	pass

app.config['MONGODB_SETTINGS'] = mongodb_settings
app.debug = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Initialize flask-mongoengine
db.init_app(app)

# Add jade template support
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


@app.route("/")
def random_restaurant():
	"""
	Shows a random restaurant to the user
	"""
	restaurant = Restaurant.random

	return render_template('home.jade', restaurant=restaurant)


@app.route("/restaurant/<restaurant_id>")
def restaurant_details(restaurant_id):
	"""
	Restaurant details page
	"""
	restaurant = Restaurant.objects.get_or_404(id=restaurant_id)

	return render_template('restaurant/details.jade', restaurant=restaurant)


@app.route("/restaurant/create/", methods=['GET', 'POST'])
def restaurant_create():
	"""
	Restaurant create page
	"""
	from document_forms import RestaurantForm

	form = RestaurantForm(request.form)
	message = ''

	# If the user has submitted data and the data is valid
	if request.method == 'POST' and form.validate():
			# Save the new restaurant
			form.save()
			message = 'Restaurant added!'
			
			return redirect(url_for('restaurant_list'))

	return render_template('restaurant/create.jade', form=form, message=message)


@app.route('/restaurants/')
def restaurant_list():
	restaurants = Restaurant.objects

	return render_template('restaurant/list.jade', restaurants=restaurants)

@app.route('/restaurant/delete/<restaurant_id>')
def restaurant_delete(restaurant_id):
	restaurant = Restaurant.objects.get_or_404(id=restaurant_id)

	restaurant.delete()

	return redirect(url_for('restaurant_list'))


@app.route("/api/restaurants/")
def api_restaurants():
	"""
	Returns a JSON object with all the restaurant data.
	"""
	response = Response(Restaurant.objects.to_json(),
		status=200, mimetype="application/json")

	return response


if __name__ == "__main__":
    app.run()