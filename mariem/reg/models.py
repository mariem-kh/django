from django.db import models

# Create your models here.

#create registration_model

class createc(models.Model):
   username=models.CharField(max_length=50)
   email=models.CharField(max_length=50)
   password=models.CharField(max_length=50)
   cpassword=models.CharField(max_length=50)


#create addproduct_model

class addproduct(models.Model):
   
    name  = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=100,decimal_places=2, null=False, blank=False)
    countinstock = models.DecimalField(max_digits=100,decimal_places=2,null=True,blank=False)
    imgurl = models.ImageField(upload_to='uploads/images', null=True, blank=True)
    category= models.CharField(max_length=15)
    description=models.CharField(max_length=50)
  
#create cart_model 

class Cart(models.Model):
    customer = models.ForeignKey(createc, on_delete=models.CASCADE)
    cart_id = models.UUIDField( unique=True, editable=False)
  


    @property
    def get_cart_total(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.get_total for item in cartitems])
        return total
    
    
#create cartitem_model 

class it(models.Model):
   
   email=models.CharField(max_length=50)
   pname  = models.CharField(max_length=100, null=False, blank=False)
   pprice= models.DecimalField(max_digits=100,decimal_places=2, null=False, blank=False)
   pcategory= models.CharField(max_length=15)
   pquantity = models.IntegerField(default=0)


   @property
   def get_total(self):
        total = self.quantity * self.product.price
        if total == 0.00:
            self.delete()
        return total