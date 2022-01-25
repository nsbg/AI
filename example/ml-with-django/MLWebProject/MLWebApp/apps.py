from django.apps import AppConfig
from .vectorizer import vect

import pickle
import os
import numpy as np

class MlwebappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MLWebApp'

