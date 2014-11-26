from flask import Flask
from mongoengine import connect

from documents import Restaurant

connect('randomizer')
app = Flask(__name__)

app.debug = True

@app.route("/")
def hello():
    restaurants = Restaurant.objects
    try:
        return restaurants[0].name
    except IndexError:
       return "no restaurants"

if __name__ == "__main__":
    app.run()