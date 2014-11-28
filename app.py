from flask import Flask, render_template, abort, redirect, request, url_for

from mongoengine.errors import ValidationError

from db import db
from documents import Restaurant

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'randomizer'
}

app.debug = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

db.init_app(app)

# Add jade template support
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route("/")
def random_restaurant():
	restaurant = Restaurant.random

	return render_template('home.jade', restaurant=restaurant)

# Restaurant details page
@app.route("/restaurant/<restaurant_id>")
def restaurant_details(restaurant_id):
	restaurant = Restaurant.objects.get_or_404(id=restaurant_id)

	return render_template('restaurant/details.jade', restaurant=restaurant)

# Restaurant create page
@app.route("/restaurant/create/", methods=['GET', 'POST'])
def restaurant_create():
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


if __name__ == "__main__":
    app.run()