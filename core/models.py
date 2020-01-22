from django.db import models

class Person(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	day = models.DateField()
	mobile = models.IntegerField()
	land = models.IntegerField()
	Mild = models.IntegerField(default=0)
	Startdate = models.DateField()
	Enddate = models.DateField()
	DateofGrant = models.DateField()
	PRP = models.IntegerField()
	Mineralname = models.CharField(max_length=100)
	District = models.CharField(max_length=100)
	GrantedArea = models.IntegerField()
	DateofAuction = models.DateField()
	HighestBid = models.IntegerField()
	NoofInstallments = models.IntegerField()
	DueDate = models.DateField()
	AmountofInstallments = models.IntegerField()

	def __str__(self):
		return f'{self.firstname} {self.lastname}'