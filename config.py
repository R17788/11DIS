import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '"SECRET STRING'

    MONGODB_SETTINGS = { 'db' : 'SPS_Enrolment' }
