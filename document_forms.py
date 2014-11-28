from flask.ext.mongoengine.wtf import model_form

from documents import Restaurant


RestaurantForm = model_form(Restaurant)