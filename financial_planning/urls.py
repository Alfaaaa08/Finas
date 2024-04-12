from django.urls import path
from financial_planning.views import financial_planning

app_name = 'financial_planning'

urlpatterns = [
    path('', financial_planning, name='financial_planning')
]
