from django.urls import path
from .views import LibroList, LibroCreate, LibroUpdate, LibroDelete, LibroDetalle
from .views import EjemplarLibro, EjemplarCreate,  EjemplarUpdate
from .views import ListaPrestamo, PrestamoUpdate, PrestamoDelete

from .views import cargar_inicio, LoginView, LogoutView



urlpatterns = [
    path('', cargar_inicio, name = 'inicio'),

    path('iniciarsesion/', LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('logoutsesion/', LogoutView.as_view(template_name = 'accounts/logout.html'), name = 'logout'),

    path('libros/', LibroList.as_view(), name = 'listar_libros'),
    path('libros/nuevo/', LibroCreate.as_view(), name = 'nuevo_libro'),
    path('libros/editar/<int:pk>', LibroUpdate.as_view(), name = 'editar_libro'),
    path('libros/eliminar/<int:pk>', LibroDelete.as_view(), name = 'borrar_libro'),
    path('libros/detalles/<int:pk>', LibroDetalle.as_view(), name = 'detalle_libro'),

    path('ejemplar/', EjemplarLibro.as_view(), name = 'ejemplar_libro'),    
    path('ejemplar/editar/<int:pk>', EjemplarUpdate.as_view(), name = 'editar_ejemplar'),
    path('ejemplar/nuevo/', EjemplarCreate.as_view(), name = 'nuevo_ejemplar' ),

    path('prestamo/', ListaPrestamo.as_view(), name = 'lista_prestamo'),
    path('prestamo/editar/<int:pk>', PrestamoUpdate.as_view(), name = 'editar_prestamo'),
    path('prestamo/eliminar/<int:pk>', PrestamoDelete.as_view(), name = 'eliminar_prestamo'),

]