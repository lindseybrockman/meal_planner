from django.contrib.auth.models import User
from django.db import models

from pantry.models import Pantry

class Chef(models.Model):
    """
    Extends django auth User model
    """
    user = models.OneToOneField(User)
    pantry = models.ForeignKey(Pantry)

    @staticmethod
    def get_chef(user):
        """
        helper method that returns
        takes in a User object and
        returns the Chef object tied
        to that User
        """
        return Chef.objects.get(user=user)
    """
    Notes:
        chefs that share a pantry
        should also share all recipes
        in that pantry.
    """
