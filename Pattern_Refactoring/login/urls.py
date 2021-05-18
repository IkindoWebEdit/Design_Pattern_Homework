from django.conf.urls import url, patterns

from . import views

# Refactoring: used patterns instead of paths
urlpatterns = patterns(
    'login.views',
    url(r'^$', 'loginPage_GET'),
    url(r'^$', 'loginPage_POST'),
    url(r'^logout/$', 'logoutAction')
)
