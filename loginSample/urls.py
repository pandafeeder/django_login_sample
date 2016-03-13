from django.conf.urls import url, include
from login import views
from django.conf import settings
from django.views.generic import TemplateView

settings.LOGIN_REDIRECT_URL = '/login_redirect_page/'
urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^some_page/', views.SomePage.as_view(template_name="registration/some_page.html")),
    url(r'^login_redirect_page/', TemplateView.as_view(template_name="registration/login_redirect_page.html")),
]
