from django.urls import path
from home.views import home
from financial_planning.views import financial_planning

urlpatterns = [
    path('', home),
]
