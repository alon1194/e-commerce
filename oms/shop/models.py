from django.db import models
class User(models.Model): 
    UserId = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 50)
    Email = models.EmailField(max_length = 50)
    Phone = models.IntegerField()
  

    def __str__(self):
        return self.Name
    class meta:
        ordering =['Name']





class Address(models.Model):
    Address_ID = models.AutoField(primary_key=True)
    Street = models.CharField(max_length = 50)
    City = models.CharField(max_length = 50 )
    State = models.CharField(max_length = 50)
    Zip_code = models.CharField(max_length = 10)
    Country = models.CharField()
    User = models.ForeignKey('User', on_delete = models.CASCADE, null = True , blank = True)

    def __str__(self): 
        return f"{self.Street},{self.City} {self.Country}"
    
    class meta: 
        ordering = ['User', 'City']
        




 