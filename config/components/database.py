from config.settings import env, root


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': env.db_url(),
}

FIXTURE_DIRS = [
    root('db', 'fixture'),
]
