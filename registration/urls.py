from django.urls import path
from registration.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
