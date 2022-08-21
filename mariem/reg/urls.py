from django.urls import path 
from . import views
#from views import registviews
urlpatterns = [
 
  path('add/',views.registviews.as_view(),name='add'),
  path('get/',views.getviews.as_view(),name='get'),
  path('auth/',views.LoginView.as_view(),name='auth'),
  path('addproduct/',views.addpviews.as_view(),name='addproduct'),
  path('getproduct/',views.getpviews.as_view(),name='getproduct'),
  path('updateproduct/<int:pk>',views.updatepviews.as_view(),name='updateproduct'),
  path('deleteproduct/<int:pk>',views.deletepviews.as_view(),name='deleteproduct'),
  path('showdetails/<int:pk>',views.getidp.as_view(),name='showdetails'),
  path('addtocart/<int:pk>',views.addtocart.as_view(),name='addtocart'),
  path('search/',views.searchp.as_view(),name='search'),
  path('getorders/',views.getordersviews.as_view(),name='getorders'),
  path('deleteit/<int:pk>',views.deleteitviews.as_view(),name='deleteit'),
  
  
 

]
