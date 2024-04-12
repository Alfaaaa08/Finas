from django.contrib import admin
from django.urls import path, include
import financial_planning.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('financial_planning/', include((financial_planning.urls, 'financial_planning'))),
    path('', include('home.urls')),
]