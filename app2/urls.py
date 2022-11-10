from django.urls import path
from app2 import views

app_name='app2'
urlpatterns=[ 
    path('Apple',views.Apple,name='Apple'),
    path('Realme',views.Realme,name='Realme'),
    path('oneplus',views.oneplus,name='oneplus'),
]