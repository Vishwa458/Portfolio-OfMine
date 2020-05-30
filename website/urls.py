import website.views as views
from django.urls import path
from django.views.generic import TemplateView

app_name = 'website'
urlpatterns = [
    path('', views.Skills.as_view(), name='index'),
    path('webappdeveloper', views.WebAppDeveloper.as_view(), name='webappdeveloper'),
    path('softwaredevelopment', views.SoftwareDevelopment.as_view(), name='softwaredevelopment'),

]
