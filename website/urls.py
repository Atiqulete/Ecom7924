from django.urls import path
from website.views import index,contact,pro_deta,about,product_search,categories_product,add_to_cart

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('search/',product_search,name='product_search-page'),
    path('pro_deta/<int:pk>/',pro_deta,name='pro_deta'),
    path('categories_product/<int:pk>/',categories_product,name='categories_product_page'),
    path('add_to_cart/<int:product_id>/',add_to_cart, name='add_to_cart'),
]