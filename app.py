from flask import Flask, render_template
from mongoengine import connect

from documents import Restaurant

connect('randomizer')
app = Flask(__name__)

app.debug = True

@app.route("/")
def hello():
    restaurant = Restaurant.objects.first()

    return render_template('home.html', restaurant=restaurant)

if __name__ == "__main__":
    app.run()