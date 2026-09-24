from mongoengine import Document, StringField, ListField, ReferenceField, BooleanField


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    meta = {
        "collection": "authors"
    }


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)
    meta = {
        "collection": "quotes"
    }


class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    phone = StringField()
    preferred_method = StringField(
        choices=["email", "sms"],
        default="email"
    )
    sent = BooleanField(default=False)
