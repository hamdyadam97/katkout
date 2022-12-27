from django.urls import path
from bill import views

app_name = 'bill'
urlpatterns = [
    path('', views.BillView.as_view(), name='create-bill'),
    path('purchase-of-goods/', views.purchase_of_goods, name='purchase_of_goods'),
    path('<slug:slug>/', views.BillUpdateDestroy.as_view(), name='detail-bill-destroy-update'),


]
