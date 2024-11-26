"""
URL configuration for sistema_disponibilidad_bomberos_parral project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from aplicacionVoluntarios import views as viewVoluntario
from aplicacionAdministrador import views as viewAdm
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('voluntario/', viewVoluntario.homeVoluntarios, name="voluntario"),
    path('administrador/', viewAdm.homeAdm, name = "administrador"),
    path('actualizar_estado_voluntario/', viewVoluntario.actualizar_estado_voluntario, name='actualizar_estado_voluntario'),
    path('actualizar_disp_cuart/', viewVoluntario.actualizar_disp_cuart, name='actualizar_disp_cuart'),
    path('administrarCuartel/<int:idCuartel>/', viewAdm.homeAdmCuartel, name='administrarCuartel'),
    path('cuartelVoluntarios/<int:idCuartel>/', viewAdm.homeAdmCuartelVoluntarios, name='cuartelVoluntarios'),
    path('administracionVoluntarios/', viewAdm.administracionVoluntarios, name='administracionVoluntarios'),
    path('cuartelUnidades/<int:idCuartel>/', viewAdm.homeAdmCuartelUnidades, name='cuartelUnidades'),
    path('administracionUnidades/', viewAdm.administracionUnidades, name='administracionUnidades'),
    path('agregarVoluntario/', viewAdm.agregarVoluntario, name='agregarVoluntario'),
    path('agregarUnidad/', viewAdm.agregarUnidad, name='agregarUnidad'),
    path('verInfoCuartelActual/<int:idCuartel>/',viewVoluntario.verCuartelActual, name='verInfoCuartelActual'),
    path('login/', viewAdm.CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='/login'), name='logout'),
    path('editar_voluntarioADM/<str:rut>/', viewAdm.editar_voluntarioADM, name='editar_voluntarioADM'),
    path('eliminar_voluntario/<str:rut>/', viewAdm.eliminar_voluntario, name='eliminar_voluntario'),
    path('editar_voluntario/<str:rut>/', viewVoluntario.edit_voluntario, name='editar_voluntario'),
    path('editar_contraseña/<str:rut>/', viewVoluntario.edit_contrasena, name='editar_contraseña'),
    path('cambiar_password_vol/<str:rut>/', viewAdm.cambiar_password_vol, name='cambiar_password_vol'),
    path('editar_unidadADM/<str:nomenclatura>/', viewAdm.editar_unidadADM, name='editar_unidadADM'),
    path('eliminar_unidadADM/<str:nomenclatura>/', viewAdm.eliminar_unidadADM, name='eliminar_unidadADM'),
    path('emergencias/', viewAdm.admEmergencias, name = "emergencias"),
    path('emergenciaInfo/<int:id_emergencia>/', viewAdm.emergenciasDetalle, name='emergenciaInfo'),
    path('emergenciasCompletar/<int:id_emergencia>/', viewAdm.emergenciasCompletar, name='emergenciasCompletar'),
    path('organizarEmergencia/<int:id_emergencia>/', viewAdm.admOrganizarEmergencias, name='organizarEmergencia'),
    path('agregarEmergencia/', viewAdm.admEmergenciaDatos, name = 'agregarEmergencia'),
    path('asignarAUnidades/<str:nomenclatura>/<int:id_emergencia>/', viewAdm.asignarAUnidades, name = 'asignarAUnidades'),
    path('despachar/<int:id_emergencia>/', viewAdm.despachar, name = 'despachar'),
    path('generar_pdf/', viewAdm.generate_pdf, name='generar_pdf'),
    path('emergenciasEliminar/<int:id_emergencia>/', viewAdm.emergenciasEliminar, name='emergenciasEliminar'),

    path('', viewAdm.CustomLoginView.as_view(), name = 'login'),
]
