from django.conf.urls import url, include
from usuarios.views import userlogin, LogOut


urlpatterns = [
    url(r'^login/$', include('apps.usuarios.views.userlogin', name="login")),
    url(r'^salir/$', include('apps.usuarios.views.LogOut', name='logout')),

]
