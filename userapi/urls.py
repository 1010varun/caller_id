from .views import *
from django.urls import path

urlpatterns = [
    path('mark_spam', MarkSpam.as_view(), name='mark_spam'),
    path('search/name/<str:name>', SearchByName.as_view(), name='search_by_name'),
    path('search/phone/<str:phone_number>/', SearchByPhoneNumber.as_view(), name='search_by_phone_number'),
]