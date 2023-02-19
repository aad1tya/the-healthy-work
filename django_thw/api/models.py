from django.db import models

# Create your models here.

class Card(models.Model):
    #If the card body is empty don't show or create that card.
    bulletBody = models.TextField(null=False, blank=False)
    