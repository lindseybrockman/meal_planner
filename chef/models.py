from django.contrib.auth.models import User
from django.db import models

from pantry.models import Pantry

class Chef(models.Model):
    """
    Extends django auth User model
    """
    user = models.OneToOneField(User)
    pantry = models.ForeignKey(Pantry)

    """
    Notes:
        chefs that share a pantry
        should also share all recipes
        in that pantry.
    """
