from django.db import models
import json


# Create your models here.
class Attraction(models.Model):
    attraction_name = models.CharField(max_length=255)
    reviews_count = models.IntegerField()
    general_info = models.JSONField(null=True)
    summary = models.TextField(null=True)
    reviews = models.JSONField(null=True)
    star_ratings = models.JSONField(null=True)
    location = models.JSONField(null=True)
    reviews_time = models.JSONField(null=True)
    
    class Meta:
        db_table = "attractions"

    
    def load_from_json(self, json_data):
        datas = json.loads(json_data)
        # print(data)
        for data in datas:
            self.attraction_name = data["attraction_name"]
            self.general_info = data["general_info"]
            self.reviews_count = len(data["reviews"])
            self.summary = data["attraction_summary"]
            self.reviews = data["reviews"]
            self.star_ratings = data["star_ratings"]
            self.location = data["location"]         
            self.reviews_time = data["reviews_time"]
            self.save()
