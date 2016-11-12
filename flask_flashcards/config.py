import os

#define base directory for sqlalchemy adapter
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    ADMIN_EMAIl = "kakosi69@gmail.com"

    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    APP_NAME = 'flashcard programming'
    LISTINGS_PER_PAGE = 50

    #SECURITY
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    SECURITY_PASSWORD_SALT = 'add_salt_123_hard_one'
    SECURITY_CONFIRMABLE = True

    #WTF
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'

    # SendGrid example.
    #MAIL_SERVER = 'smtp.sendgrid.net'
    #MAIL_PORT = 587
    #MAIL_USE_SSL = False
    #MAIL_USE_TLS = True
    #MAIL_USERNAME = 'username'
    #MAIL_PASSWORD = 'password'
    #DEFAULT_MAIL_SENDER = 'notifications@your_website.com'
    #SECURITY_EMAIL_SENDER = 'notifications@your_website.com'

    #RECAPTCHA_SITE_KEY = "6Ldzx_Exxxxxxxxxxxxxxxxxxxxxxx"
    #RECAPTCHA_SECRET = "6Ldzx_ESAAAxxxxxxxxxxxxxxxxxxxxxxxx"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False