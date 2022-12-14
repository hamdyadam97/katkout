from django.urls import path
from client import views

app_name = 'bill'
urlpatterns = [
    path('', views.bill.as_view(), name='create-bill'),
    path('<slug:client_slug>/', views.ClientViewDetail.as_view(), name='detail-client'),

]
