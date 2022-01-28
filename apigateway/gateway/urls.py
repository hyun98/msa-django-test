from django.urls import path, include

from .views import Testview

urlpatterns = [
    path('', Testview.as_view()),
    
]
