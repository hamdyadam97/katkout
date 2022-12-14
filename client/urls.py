from django.urls import path
from client import views

app_name = 'client'
urlpatterns = [
    path('', views.ClientView.as_view(), name='create-client'),
    path('<slug:client_slug>/', views.ClientViewDetail.as_view(), name='detail-client'),

]
