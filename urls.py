from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from .views import send_json

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendjson/', send_json, name='send_json'),
    path('', views.CitiesIndex, name="Cities"),
    path(r'<IATA>', views.CitiesSearch, name="Cities"),
    
]