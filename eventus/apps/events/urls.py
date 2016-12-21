"""eventus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from .views import IndexView, MainPanelView, CreateEvent, EventDetail, MainRegistroPanelView, CrearRegistro
urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),

    url(r'^panel/$', MainPanelView.as_view(), name='panel'),
    url(r'^panel/evento/nuevo/$', CreateEvent.as_view(), name='nuevo'),
    url(r'^panel/evento/(?P<pk>\d+)/$', EventDetail.as_view(), name='detalle'),

    url(r'^registro/$', MainRegistroPanelView.as_view(), name='registropanel'),
    url(r'^registro/asistente/nuevo$', CrearRegistro.as_view(), name='nueva_asistencia'),


]