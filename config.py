import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL


SQLALCHEMY_DATABASE_URI = 'postgresql://kydldmkjsweamo:59e8b179cf22b0bc4b300832b210b572ac7f8083bcae23fb60581cdae639af72@ec2-44-193-178-122.compute-1.amazonaws.com:5432/d4l6832532p8pi' 

SQLALCHEMY_TRACK_MODIFICATIONS = False