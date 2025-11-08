# contacts/urls.py
from rest_framework import routers
from django.urls import path, include
from .views import ContactViewSet, search_contact

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
    path('search_contact/', search_contact, name='search_contact'),
]
