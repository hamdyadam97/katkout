from django.urls import path
from bill import views

app_name = 'bill'
urlpatterns = [
    path('', views.BillView.as_view(), name='create-bill'),
    # path('<slug:client_slug>/', views.ClientViewDetail.as_view(), name='detail-client'),

]
