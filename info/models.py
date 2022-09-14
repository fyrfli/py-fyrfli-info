from django.db import models

# Create your models here.


class quotes(models.Model):
    the_quote = models.CharField(max_length=800)
    the_author = models.CharField(max_length=50)
    the_source = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.the_author


class links(models.Model):
    the_url = models.URLField(max_length=200)
    the_desc = models.CharField(max_length=200)
    the_icon = models.CharField(max_length=20)

    def __str__(self):
        return self.the_desc


# class names(models.Model):
#     gender = models.CharField(max_length=20)
#     givenname = models.CharField(max_length=20)
#     middlename = models.CharField(max_length=20)
#     surname = models.CharField(max_length=20)
#     streetaddress = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=22)
#     zipcode = models.CharField(max_length=15)
#     emailaddress = models.EmailField(max_length=100)
#     username = models.CharField(max_length=25, blank=True, null=True)
#     password = models.CharField(max_length=25, blank=True, null=True)
#     telephone = models.CharField(max_length=25)
#     birthday = models.DateField
#     age = models.IntegerField
#     bloodtype = models.CharField(max_length=4)

#     def __str__(self):
#         return self.givenname + " " + self.surname
