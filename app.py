from flask import Flask, render_template, abort, redirect, url_for
from mongoengine import connect
from mongoengine.errors import ValidationError

from documents import Restaurant

connect('randomizer')
app = Flask(__name__)

app.debug = True

# Add jade template support
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route("/")
def random_restaurant():
	restaurant = Restaurant.random

	return render_template('home.jade', restaurant=restaurant)

@app.route("/restaurant/<restaurant_id>")
def restaurant_details(restaurant_id):
	try:
		restaurant = Restaurant.objects.filter(id=restaurant_id).first()
	except ValidationError:
		restaurant = None

	if restaurant is None:
		abort(404)

	return render_template('restaurant/details.jade', restaurant=restaurant)

if __name__ == "__main__":
    app.run()