import random

from mongoengine import document, fields
from mongoengine.queryset import queryset_manager

class Restaurant(document.Document):
    name = fields.StringField(required=True, max_length=200)

    @queryset_manager
    def random(self, queryset):
        num_entries = queryset.count()
        random_entry_index = random.randint(0, num_entries-1)
        return queryset[random_entry_index]
