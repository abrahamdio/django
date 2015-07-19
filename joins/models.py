from django.db import models

# Create your models here.

class Join(models.Model):
	firstname = models.CharField(max_length = 20, default = 'firstname')
	lastname = models.CharField(max_length = 20, default = 'lastname')
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return self.firstname + ' ' + self.lastname