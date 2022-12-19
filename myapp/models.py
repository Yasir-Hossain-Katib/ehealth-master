from django.db import models



class patient(models.Model):
    username = models.CharField(max_length=200)

    email = models.CharField(max_length=200)

    password1 = models.CharField(max_length=128)

    password2 = models.CharField(max_length=128)


class doctor(models.Model):
    username = models.CharField(max_length=200)

    email = models.CharField(max_length=200)

    password1 = models.CharField(max_length=128)

    password2 = models.CharField(max_length=128)
   


class Data(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    
    age=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.first_name


class DocProfile(models.Model):
    name=models.CharField(max_length=100)
   
    email=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    op=models.CharField(max_length=100)
    institute=models.CharField(max_length=100)
    specialist=models.CharField(max_length=100)
    fees=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Payment(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    op=models.CharField(max_length=100)
    card=models.PositiveBigIntegerField(default=0)


    def __str__(self):
        return self.name

class Feedback(models.Model):
    name=models.CharField(max_length=100)
    exp=models.TextField()
    
    def __str__(self):
        return self.name



    







