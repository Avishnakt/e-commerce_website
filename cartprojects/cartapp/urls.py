from django.urls import path

from . import views

app_name = "cartapp"

urlpatterns = [

    path('', views.AllProdCat, name='all_productsCat'),
    path('<slug:c_slug>/', views.AllProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='pro_details'),


]
