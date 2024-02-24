from django.urls import path
from myhome import views

app_name = 'myhome'

urlpatterns = [
    path("user_login/", views.user_login, name="user_login"),
    path("register/", views.register, name="register"),
    path ('customer/', views.form_customer_view,name='cusotmer'),
    path ('formpage/', views.form_name_view,name='formpageformpage'),
    path ('services/', views.services, name='services'),
    path ('prices/', views.prices, name='prices'),

]