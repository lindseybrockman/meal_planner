from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'meal_planner.views.home', name='home'),
    url(r'^recipe/', include('recipe.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
