from django.urls import path, include
from . import views
app_name = 'shop'
urlpatterns = [
    path('', views.allproductCat, name='allproductCat'),
    path('<slug:c_slug>/', views.allproductCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='proCatDetail'),
]