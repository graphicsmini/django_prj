from django.db import models

# Create your models here.
class Dates(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class JobTitle(models.Model):
    name = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class Summary(models.Model):
    name = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

class Pros(models.Model):
    name = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

class Cons(models.Model):
    name = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=128)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    dates = models.ForeignKey(Dates, on_delete=models.CASCADE)
    jobtitle = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    summary = models.ForeignKey(Summary, on_delete=models.CASCADE)
    pros = models.ForeignKey(Pros, on_delete=models.CASCADE)
    cons = models.ForeignKey(Cons, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
