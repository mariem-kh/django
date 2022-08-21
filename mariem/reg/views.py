from itertools import product
import queue
from tokenize import Number
from urllib.parse import uses_params
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer

from rest_framework import generics

#from mariem.reg import serializers
from reg.models import it 
from reg.serializers import itSerializer
from reg.serializers import addproductSerializer
from reg.models import createc
from reg.models import addproduct
from reg.serializers import createcSerializer

#**************part of SIGN UP
class registviews (generics.CreateAPIView):
    queryset=createc.objects.all()
    serializer_class=createcSerializer
    print ("added successfully")
class getviews(generics.ListAPIView):
    queryset=createc.objects.all()
    serializer_class=createcSerializer
    print("list succefully")

#*********************** part of add , get ,update and delete product 
class addpviews (generics.CreateAPIView):
    queryset=addproduct.objects.all()
    serializer_class=addproductSerializer
    #print ("added successfully")
class getpviews(generics.ListAPIView):
    queryset=addproduct.objects.all()
    serializer_class=addproductSerializer
    print("list succefully")
#******************
class getidp(generics.RetrieveAPIView):
       queryset=addproduct.objects.all()
       serializer_class=addproductSerializer

#******** SIGN IN*************************
class LoginView(APIView):
    def post(self, request):
      #  if request.method=='POST':
        email=request.data['email']
        password=request.data['password']
            
        #user = createc.objects.filter(email=email).first()
        user = createc.objects.filter(email=email,password=password).first()
        if user is None:
         raise AuthenticationFailed('check your password or your email is wrong !')
      
        if(user.email==email and  user.password==password):
           return HttpResponse('yeeeeeeeeeeeeeees')
      
class updatepviews(generics.UpdateAPIView):
     queryset=addproduct.objects.all()  
     serializer_class=addproductSerializer
class deletepviews(generics.DestroyAPIView):
    queryset=addproduct.objects.all()
    serializer_class=addproductSerializer
#************************ search of product by categorie or name 
class searchp(APIView):
   def post(self,request):
    name=request.data['name']
    data=addproduct.objects.filter(name=name).first()
    if(data.name==name):
      return HttpResponse('trouve')
    if data is None :
      return HttpResponse("non trouve")
     
#******** add to cart 
class addtocart(generics.CreateAPIView):
    #product_id=getidp()
    queryset=it.objects.all()
    serializer_class=itSerializer
#****** list orders
class getordersviews(generics.ListAPIView):
    queryset=it.objects.all()
    serializer_class=itSerializer
    print("list succefully")
#************** delete from orders
class deleteitviews(generics.DestroyAPIView):
    queryset=it.objects.all()
    serializer_class=itSerializer



# Create your views here.
