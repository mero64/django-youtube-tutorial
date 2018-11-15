from django.urls import path, re_path
from home.views import HomeView, change_friends


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', change_friends, name='change_friends'),
]
