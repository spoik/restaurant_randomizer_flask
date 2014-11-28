from flask import Flask, render_template, abort, redirect, url_for

from mongoengine.errors import ValidationError

from db import db
from documents import Restaurant

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'randomizer'
}

app.debug = True

db.init_app(app)

# Add jade template support
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route("/")
def random_restaurant():
	restaurant = Restaurant.random

	return render_template('home.jade', restaurant=restaurant)

@app.route("/restaurant/<restaurant_id>")
def restaurant_details(restaurant_id):
	restaurant = Restaurant.objects.get_or_404(id=restaurant_id)

	return render_template('restaurant/details.jade', restaurant=restaurant)

if __name__ == "__main__":
    app.run()