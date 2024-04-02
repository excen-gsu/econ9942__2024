from os import environ


SESSION_CONFIGS = [
    dict(
        name='regroup',
        display_name='group matrix manipulation',
        num_demo_participants=12,
        app_sequence=['regroup'],
    ),

    dict(
        name='sliders',
        display_name='example using UI sliders',
        num_demo_participants=1,
        app_sequence=['sliders'],
    ),

    dict(
        name='drawing_shapes',
        display_name='drawing simple geometric shapes',
        num_demo_participants=2,
        app_sequence=['geoms'],
    ),
    dict(
        name='rock_paper_scissors',
        display_name='rock paper scissors (2024)',
        num_demo_participants=2,
        app_sequence=['rps'],
    ),
    dict(
        name='pub_goods_test',
        display_name='my pub goods',
        num_demo_participants=2,
        app_sequence=['my_pub_goods'],
    ),
    dict(
        name='pub_goods_test_2',
        display_name='my NEW pub goods',
        num_demo_participants=2,
        app_sequence=['my_pub_goods'],
    ),    dict(
            name='second_price_auction',
            display_name='second price auction',
            num_demo_participants=3,
            app_sequence=['second_price_auction'],
        ),

    dict(
        name='input_examples',
        display_name='examples of different inputs',
        num_demo_participants=1,
        app_sequence=['input_examples'],
    ),
    dict(
        name='livepage1',
        display_name='our first live page example',
        num_demo_participants=2,
        app_sequence=['baby_livepage'],
    ),
    dict(
        name='live_pages',
        display_name='simple live pages demo',
        num_demo_participants=2,
        app_sequence=['live_pages_demo'],
    ),
    dict(
        name='images_1',
        display_name='randomizing image sequences',
        num_demo_participants=3,
        app_sequence=['parameters_example'],
        images=['duck.png', 'fish.jpg', 'pinguin.jpg']
    ),
    dict(
        name='circle',
        display_name='circle demo',
        num_demo_participants=1,
        app_sequence=['circle_example']

    ),
    dict(
        name='mpl_1',
        display_name='multiple price list example',
        num_demo_participants=1,
        app_sequence=['mpl_example'],
    ),

    dict(
        name='video_demo',
        display_name='video demo',
        num_demo_participants=2,
        app_sequence=['video'],
    ),
    dict(
        name='template_looping',
        display_name='template looping',
        num_demo_participants=1,
        app_sequence=['template_looping'],
    ),
    dict(
        name='check_time',
        display_name='check time',
        num_demo_participants=1,
        app_sequence=['check_time'],
    ),
    dict(
        name='custom_waitpage',
        display_name='custom waitpage example',
        num_demo_participants=2,
        app_sequence=['custom_waitpage'],
    ),
    dict(
        name='auction2024',
        display_name='2024 class example',
        num_demo_participants=3,
        app_sequence=['auction2024'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    dict(
        name='econ9942',
        display_name='Econ 9942 class',
        participant_label_file='_rooms/econ9942.txt',
        use_secure_urls=True,
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""



SECRET_KEY = '7267278848110'

INSTALLED_APPS = ['otree']

# use_browser_bots = True


