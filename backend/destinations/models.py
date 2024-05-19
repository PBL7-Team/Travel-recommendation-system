from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255,blank=True,null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'destinations'
    
    
