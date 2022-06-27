from django.conf.urls import include, url
import HelloDjangoApp.views
import Soma.views
# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^home$', HelloDjangoApp.views.index, name='home'),
    url(r'^soma$', Soma.views.soma, name='soma'),

]
