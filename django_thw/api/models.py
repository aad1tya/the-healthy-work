from django.db import models

# Create your models here.

class Card(models.Model):
    #If the card body is empty don't show or create that card.
    heading = models.CharField(max_length=300)
    bulletBody = models.TextField(null=False, blank=False)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "Card " + str(self.id) + ": "+ self.heading[0:50]
    
    class Meta:
        ordering = ['created']
    