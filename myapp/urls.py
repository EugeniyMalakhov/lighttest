from django.conf.urls import url, patterns, include

urlpatterns = [
    url(r'^office/$', "myapp.views.office", name='office'),
    url(r'^login/$', "myapp.views.login", name='login'),
    url(r'^logout/$', "myapp.views.logout", name='logout'),
    url(r'^registr/$', "myapp.views.registr", name='registr'),
    url(r'^contact/$', "myapp.views.contact", name='contact'),
    url(r'^delete/$', "myapp.views.delete", name='delete'),

    url(r'^$', "myapp.views.home", name='home'),
]
