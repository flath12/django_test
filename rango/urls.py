from django.conf.urls import url
from django.conf.urls.static import static
from rango import views

app_name = 'rango'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'', views.AboutView.as_view(), name='about'),
]