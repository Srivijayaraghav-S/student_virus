from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('academics/', views.academics, name='academics'),
    path('past/', views.past, name='past'),
    path('contact/', views.contact, name='contact'),
    path('studentprofile/',views.studentprofile,name='studentprofile'),
    path('logout/',views.logout,name='logout'),
]
