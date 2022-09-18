from django.urls import path
from AppDictClaro import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('buscar/', views.buscar, name = "Buscar"),
    path('acercadenosotros/', views.acerca_info, name = "Acerca de Nosotros"),
    path('tablaFormulario/', views.tablaFormulario, name = "Formulario Tabla"),
    path('tablacampoFormulario/', views.tablacampoFormulario, name = "Formulario Campo Tabla"),
    path('tablas/list', views.TablaList.as_view(), name='Tablas')
]