import os
import django
import configparser
from mongoengine import connect, Document, ReferenceField, CASCADE, StringField, ListField
from datetime import datetime

config = configparser.ConfigParser()
config_file = os.path.join(os.path.dirname(__file__), 'config.ini')

if not config.read(config_file):
    raise FileNotFoundError(f"Could not find or read the configuration file: {config_file}")

if 'MongoDB' not in config:
    raise KeyError("The 'MongoDB' section is missing in the configuration file.")

MONGO_USER = config['MongoDB']['USER']
MONGO_PASS = config['MongoDB']['PASS']
MONGO_DB_NAME = config['MongoDB']['DB_NAME']
MONGO_DOMAIN = config['MongoDB']['DOMAIN']

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes.settings')
django.setup()

from quoteapp.models import Author as DjangoAuthor, Tag as DjangoTag, Quote as DjangoQuote
from django.contrib.auth.models import User

mongo_uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_DOMAIN}/{MONGO_DB_NAME}?retryWrites=true&w=majority"
connect(host=mongo_uri)

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True, reverse_delete_rule=CASCADE)
    quote = StringField(required=True)

default_user = User.objects.first()  # Заміна на потрібного користувача

for mongo_author in Author.objects:
    try:
        born_date_converted = datetime.strptime(mongo_author.born_date, '%B %d, %Y').strftime('%Y-%m-%d')
    except ValueError as e:
        print(f"Error parsing date for author {mongo_author.fullname}: {e}")
        born_date_converted = None
    
    django_author, created = DjangoAuthor.objects.get_or_create(
        fullname=mongo_author.fullname,
        born_date=born_date_converted,
        born_location=mongo_author.born_location,
        description=mongo_author.description
    )

for mongo_quote in Quote.objects:
    tags = []
    for tag_name in mongo_quote.tags:
        tag, created = DjangoTag.objects.get_or_create(name=tag_name)
        tags.append(tag)

    quote = DjangoQuote.objects.create(
        quote=mongo_quote.quote,
        author=DjangoAuthor.objects.get(fullname=mongo_quote.author.fullname),
        user=default_user
    )
    quote.tags.set(tags)
    quote.save()

print("DB is successfully migrated")
