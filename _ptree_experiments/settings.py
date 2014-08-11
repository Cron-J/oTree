import os
import ptree.settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if os.environ.get('PTREE_PRODUCTION'):
    DEBUG = False
else:
    DEBUG = True

if os.environ.get('IS_PTREE_DOT_ORG'):
    ADMIN_PASSWORD = os.environ['PTREE_ADMIN_PASSWORD']
    SECRET_KEY = os.environ['PTREE_SECRET_KEY']
else:
    ADMIN_PASSWORD = 'ptree'
    # don't share this with anybody.
    # Change this to something unique (e.g. mash your keyboard), and then delete this comment.
    SECRET_KEY = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'

# local database settings
# add: export LOCALDEV=1 to .bashrc
if os.environ.get("PTREE_LOCALDEV"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
# heroku database settings
else:
    import dj_database_url
    DATABASES = {}
    DATABASES['default'] = dj_database_url.config()

settings = {
    'CREATE_DEFAULT_SUPERUSER': True,
    'ADMIN_USERNAME': 'admin',
    'ADMIN_PASSWORD': ADMIN_PASSWORD,
    'AWS_ACCESS_KEY_ID': os.environ.get('AWS_ACCESS_KEY_ID'),
    'AWS_SECRET_ACCESS_KEY': os.environ.get('AWS_SECRET_ACCESS_KEY'),
    'CURRENCY_CODE': 'EUR',
    'LANGUAGE_CODE': 'en-us',
    'DEBUG': DEBUG,
    'DATABASES': DATABASES,
    'INSTALLED_APPS': [
        'ptree',
        '_ptree_experiments',
    ],
    'INSTALLED_PTREE_APPS': [

        'lab_results',
        'lying',
        'prisoner',
        'trust',
        'public_goods',
        'dictator',
        'matching_pennies',
        'traveler_dilemma',
        'survey',
        'bargaining',
        'guessing',

        'matrix_symmetric',
        'matrix_asymmetric',
        'cournot_competition',
        'stackelberg_competition',
        'private_value_auction',
        'volunteer_dilemma',
        'bertrand_competition',
        'principal_agent',
        'coordination',
        'stag_hunt',
        'battle_of_the_sexes',
        'lemon_market',
        'showcase',
        'common_value_auction',
        'tragedy_of_the_commons',
        # lab results: displays lab results in a given session

    ],
    'SECRET_KEY': SECRET_KEY,
    'BASE_DIR': BASE_DIR,
    'WSGI_APPLICATION': '_ptree_experiments.wsgi.application',
    'ROOT_URLCONF': '_ptree_experiments.urls',
}

ptree.settings.augment_settings(settings)
