from django.db import models

# Create your models here.

class cbt(models.Model):
	age = models.IntegerField()
	name = models.CharField(max_length = 100)
	country = models.CharField(max_length = 100)
	gender = models.CharField(max_length = 1)

	def __str__(self):
		return self.name


class Feedback(models.Model):
	message = models.TextField()