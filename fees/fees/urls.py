from django.urls import path, include
from rest_framework import routers

from fees.fees import views

router = routers.DefaultRouter()

router.register('fees', views.FeeViewSet, basename='fees')
urlpatterns = [
    path('', include(router.urls)),
]
