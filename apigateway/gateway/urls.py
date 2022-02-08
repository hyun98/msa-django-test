from django.urls import path, include

from .views import Testview, Gateway

urlpatterns = [
    path('', Testview.as_view()),
    path("gateway", Gateway.as_view()),
]
