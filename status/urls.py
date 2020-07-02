from django.conf.urls import url
from django.urls import path
from status.views import StatusListSearchAPIView

urlpatterns =[
    url(r'^$', StatusListSearchAPIView.as_view()),
    # url(r'^create/$', StatusCreateAPIView.as_view()),
    # url(r'^(?P<id>.*)/$', StatusDetailsAPIView.as_view()),
    # url(r'^(?P<id>.*)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<id>.*)/delete/$', StatusUpdateAPIView.as_view()),
]