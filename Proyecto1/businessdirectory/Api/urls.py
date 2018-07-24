from django.urls import include, path
# from RuteandoApi.views import CitiesList, BusinessList, PostCities, PostBusiness
from Api import views
from django.views.generic import TemplateView


urlpatterns = [
     path('ciudad/', views.CiudadList.as_view()),
    # path('ciudad/', views.CitiesList.as_view()),
    path('usuario/<int:pk>/', views.CiudadDetail.as_view()),    
    # path('empresa/<int:pk>/', views.BusinessDetail.as_view())
    path('tipo/', views.TipoList.as_view()),
    path('empresas/', views.EmpresasList.as_view()),
    path('home/', TemplateView.as_view(template_name='home.html')),
    path('vista2/', TemplateView.as_view(template_name='prueba.html'))

]