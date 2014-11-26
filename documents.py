from mongoengine import document, fields

class Restaurant(document.Document):
    name = fields.StringField(required=True, max_length=200)