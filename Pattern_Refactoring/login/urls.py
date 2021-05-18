from django.conf.urls import url, patterns

from . import views

# Refactoring: used patterns instead of paths
urlpatterns = patterns(
    'login.views',
    # Refactoring: included POST and GET into the same function
    url(r'^$', 'loginPage'),
    url(r'^logout/$', 'logoutAction')
)
