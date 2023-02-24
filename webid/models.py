from django.db import models
from django.contrib.auth.models import User



class AddID(models.Model):
	#user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name=models.CharField(max_length=250,null=True)
	last_name=models.CharField(max_length=250,null=True)
	midle_initial = models.CharField(max_length=250,null=False)
	id_pic = models.ImageField(null=True,blank=True,upload_to="images/picture")
	signature = models.ImageField(null=True,blank=True,upload_to="images/signature")
	contact_person = models.CharField(max_length=250, null=False)
	contact_person_no = models.CharField(max_length=250,null=False)
	address = models.TextField(null=False)
	sss_no = models.CharField(max_length=250,null=False)
	tin = models.CharField(max_length=250,null=False)
	#philhealth_no = models.CharField(max_length=250,null=False)
	employee_no = models.CharField(max_length=250,null=False)
	birth_date = models.DateField(null=True)
	disignation = models.CharField(max_length=250,null=True)
	id_code = models.CharField(max_length=250,null=False,default='',blank=True)
	contact_person_address = models.TextField(null=True)
	blood_type = models.CharField(max_length=250,null=True,blank=True)
	name_extension = models.CharField(max_length=250, null= False,default='',blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	id_status = {
		('Pending','Pending'),
		('For Edit','For Edit'),
		('Completed','Completed'),
	}
	status = models.CharField(max_length=150,choices=id_status,default='Pending')
	transaction_no=models.CharField(max_length=250,null=True)

class Employee(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name=models.CharField(max_length=250,null=True)
	last_name=models.CharField(max_length=250,null=True)
	midle_initial = models.CharField(max_length=250,null=False)
	id_pic = models.ImageField(null=True,blank=True,upload_to="images/picture")
	signature = models.ImageField(null=True,blank=True,upload_to="images/signature")
	contact_person = models.CharField(max_length=250, null=False)
	contact_person_no = models.CharField(max_length=250,null=False)
	address = models.TextField(null=False)
	sss_no = models.CharField(max_length=250,null=False)
	tin = models.CharField(max_length=250,null=False)
	philhealth_no = models.CharField(max_length=250,null=False)
	employee_no = models.CharField(max_length=250,null=False)
	birth_date = models.DateField(null=True)
	disignation = models.CharField(max_length=250,null=True)
	id_code = models.CharField(max_length=250,null=False,default='',blank=True)
	contact_person_address = models.TextField(null=True)
	blood_type = models.CharField(max_length=250,null=True,blank=True)
	name_extension = models.CharField(max_length=250, null= False,default='',blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering=['disignation']

		

class ID(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='+')
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='+',null=True)
	
	id_status = {
		('Pending','Pending'),
		('For Edit','For Edit'),
		('Completed','Completed'),
	}
	status = models.CharField(max_length=150,choices=id_status,default='Pending')
	date_printed =models.DateField(null=True)
	remarks = models.CharField(max_length=250,null=True)
	transaction_no = models.CharField(max_length=250,null=True)
	created_at = models.DateTimeField(auto_now_add=True)

class Forclaim(models.Model):
	user =  models.CharField(max_length=250,null=False)
	transaction_no = models.CharField(max_length=250,null=True)
	date_printed = models.DateField(null=True)


class ForclaimAdmin(models.Model):
	employee =  models.CharField(max_length=250,null=False)
	transaction_no = models.CharField(max_length=250,null=True)
	date_printed = models.DateField(null=True)


class Idcode(models.Model):
	user =models.ForeignKey(User, on_delete=models.CASCADE)
	department = models.CharField(max_length=250,null=False)
	id_code = models.CharField(max_length=250,null=False)

class DeptandDesignation(models.Model):
	fullname=models.CharField(max_length=250,null=True)
	designation=models.CharField(max_length=250,null=True)
	idcode=models.CharField(max_length=250,null=True)

class Idapplication(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	transaction_no=models.CharField(max_length=250,null=True)
	created_at = models.DateField(auto_now_add=True,null=True)
