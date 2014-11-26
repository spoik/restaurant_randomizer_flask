from flask import Flask, render_template
from mongoengine import connect

from documents import Restaurant

connect('randomizer')
app = Flask(__name__)

app.debug = True

# Add jade template support
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route("/")
def hello():
    restaurant = Restaurant.objects.first()

    return render_template('home.jade', restaurant=restaurant)

if __name__ == "__main__":
    app.run()