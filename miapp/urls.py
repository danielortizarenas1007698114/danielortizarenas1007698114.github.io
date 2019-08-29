from django.urls import path
from .views import cargar_inicio, LibroList, LibroCreate, LibroUpdate, LibroDelete, LibroDetalle, EjemplarLibro
from .views import EjemplarCreate,  EjemplarUpdate, ListaPrestamo, PrestamoUpdate, PrestamoDelete



urlpatterns = [
    path('', cargar_inicio, name = 'inicio'),
    path('libros/', LibroList.as_view(), name = 'listar_libros'),
    path('libros/nuevo/', LibroCreate.as_view(), name = 'nuevo_libro'),
    path('libros/editar/<int:pk>', LibroUpdate.as_view(), name = 'editar_libro'),
    path('libros/eliminar/<int:pk>', LibroDelete.as_view(), name = 'borrar_libro'),
    path('libros/detalles/<int:pk>', LibroDetalle.as_view(), name = 'detalle_libro'),
    path('ejemplar/', EjemplarLibro.as_view(), name = 'ejemplar_libro'),    
    path('ejemplar/editar/<int:pk>', EjemplarUpdate.as_view(), name = 'editar_ejemplar'),
    path('ejemplar/nuevo', EjemplarCreate.as_view(), name = 'nuevo_ejemplar' ),
    path('prestamo', ListaPrestamo.as_view(), name = 'lista_prestamo'),
    path('prestamo/editar/<int:pk>', PrestamoUpdate.as_view(), name = 'editar_prestamo'),
    path('prestamo/eliminar/<int:pk>', PrestamoDelete.as_view(), name = 'eliminar_prestamo'),
]