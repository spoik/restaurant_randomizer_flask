import random

from mongoengine import fields
from mongoengine.queryset import queryset_manager

from db import db

class Restaurant(db.Document):
    name = fields.StringField(required=True, max_length=200)

    meta = {
    	"ordering": ["name"]
    }

    @queryset_manager
    def random(self, queryset):
    	"""
    	Returns a random record from the collection.
    	"""
        num_entries = queryset.count()
        random_entry_index = random.randint(0, num_entries-1)
        return queryset[random_entry_index]
