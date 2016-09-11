from django.conf.urls import url
from simplemooc.courses.views import index

urlpatterns = [
     url(r'^$', index, name='index'),
]
