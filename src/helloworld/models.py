from django.db import models

# Create your models here.

class ShowHelloWorld(models.Model):
	id = models.AutoField(primary_key = True)
	strn = models.CharField(max_length = 100, default = 'Hello World')


	class Meta:
		verbose_name = 'testApp'
		verbose_name_plural = 'testApps'

