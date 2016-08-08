from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER_CHOICES = (
	(u'M',u'Male'),
	(u'F',u'Female'),
	)

POSITION_CHOICES = (
	(u'Chair',u'Chair'),
	(u'ViceChair',u'ViceChair'),
	)

SLIDE_CHOICES = (
	(u'Y',u'Yes'),
	(u'N',u'No'),
	)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 120)
	email = models.EmailField()
	mobile = models.CharField(max_length = 10)
	institute = models.CharField(max_length = 120)
	gender = models.CharField(max_length = 1, choices=GENDER_CHOICES)
	dob = models.DateField(auto_now_add = True, auto_now = False)
	city = models.CharField(max_length = 120)
	updatedtime = models.DateTimeField(auto_now_add = False, auto_now = True)
	settime = models.DateTimeField(auto_now_add = True, auto_now = False)

	def __str__(self):
		return self.name

class Delegate(models.Model):
	position = models.CharField(max_length = 20, choices=POSITION_CHOICES)
	previous_mun_exp = models.TextField(blank = False, null = False)
	previous_org_com_exp = models.TextField(blank = True, null = True)
	previous_exe_board_exp = models.TextField(blank = False, null = False)
	other_exp = models.TextField(blank = True, null = True)
	slide_position = models.TextField(max_length = 1, choices = SLIDE_CHOICES)

	def __str__(self):
		return self.name