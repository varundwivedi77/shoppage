from django.db import models

# Create your models here.

class product(models.Model):
    p_id=models.AutoField
    p_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField( max_length=200)
    p_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self) -> str:
        return self.p_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name
    
class Orders(models.Model):
    o_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=500)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class orderstatus(models.Model):
    update_id=models.AutoField(primary_key=True)
    orderid=models.IntegerField(default='')
    updatedesc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.updatedesc[0:7] + '...'
    
