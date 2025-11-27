from rest_framework import routers
from .views import AutorViewSet, LibroViewSet, ResenaViewSet

router = routers.DefaultRouter()
router.register('autores', AutorViewSet)
router.register('libros', LibroViewSet)
router.register('resenas', ResenaViewSet)

urlpatterns = router.urls