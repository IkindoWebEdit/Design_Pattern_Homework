
from django.contrib import admin
from django.urls import include
from django.conf.urls import patterns

# Refactoring: used patterns instead of paths
urlpatterns = patterns(
    '',
    (r'^', include('login.urls')),
    (r'^adminpage/', include('adminpage.urls')),
    (r'^admin/', admin.site.urls)
)
