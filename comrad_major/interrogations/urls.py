from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('interrogations', views.InterrogationView, 'interrogations')
router.register('active_interrogations', views.ActiveInterrogationView, 'active_interrogations')

urlpatterns = [
    path('', include(router.urls), name='api_root')
]