from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=264 , unique=True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length = 264 , unique = True)
