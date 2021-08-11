from django.urls import path, include
from rest_framework import routers

from fees.player_fees import views

router = routers.DefaultRouter()

router.register('player_fees', views.PlayerFeesViewSet, basename='player_fees')
urlpatterns = [
    path('', include(router.urls)),
]
