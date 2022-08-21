from rest_framework import serializers
from reg.models import it 
from reg.models import createc 
from reg.models import addproduct
from reg.models import Cart


#create a createcSerializer
class createcSerializer(serializers.ModelSerializer):
   class Meta:
     model=createc
     fields=('username','email','password','cpassword')
#create a addproductSerializer

class addproductSerializer(serializers.ModelSerializer):
    class Meta:
        model=addproduct
        fields=('name','price','countinstock','imgurl','category','description')
#create a cartserializer
class cartserializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=('customer','cart_id')

   
#***********

class itSerializer(serializers.ModelSerializer):
   class Meta:
        model=it
        fields=('email','pname','pprice','pcategory','pquantity')

