from flask import abort, Flask, redirect, render_template, Response, request, url_for

from mongoengine.errors import ValidationError

# from db import db
# from documents import Restaurant


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'randomizer'
}

app.debug = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Initialize flask-mongoengine
# db.init_app(app)

# Add jade template support
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


@app.route("/")
def random_restaurant():
	return "hello world"
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
		form = RestaurantForm()

	return render_template('restaurant/create.jade', form=form, message=message)


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