from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, SuccesPageView
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path(r'', HomePageView.as_view(), name="index"),
    path(r'^about/$', AboutPageView.as_view(), name="about"),
    path(r'^contact/$', ContactPageView.as_view(), name="contact"),
    path(r'^success/$', SuccesPageView.as_view(), name="success"),
    path('success/', views.success, name='success'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

