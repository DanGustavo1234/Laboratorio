from rest_framework import routers 
from .api import EstudianteViewSet,LaboratorioViewSet, DocenteViewSet, CarreraViewSet, HorarioViewSet, MateriaViewSet, BibliotecaViewSet, SalasdelecturaViewSet, Reserva_laboratorioViewSet, Reserva_bibliotecaViewSet, Reserva_salasdelecturaViewSet

router = routers.DefaultRouter()

router.register('api/estudiantes', EstudianteViewSet, 'estudiantes')
router.register('api/laboratorios', LaboratorioViewSet, 'laboratorios')
router.register('api/docentes', DocenteViewSet, 'docentes')
router.register('api/carreras', CarreraViewSet, 'carreras')
router.register('api/horarios', HorarioViewSet, 'horarios')
router.register('api/materias', MateriaViewSet, 'materias')
router.register('api/bibliotecas', BibliotecaViewSet, 'bibliotecas')
router.register('api/salasdelecturas', SalasdelecturaViewSet, 'salasdelecturas')
router.register('api/reserva_laboratorios', Reserva_laboratorioViewSet, 'reserva_laboratorios')
router.register('api/reserva_bibliotecas', Reserva_bibliotecaViewSet, 'reserva_bibliotecas')
router.register('api/reserva_salasdelecturas', Reserva_salasdelecturaViewSet, 'reserva_salasdelecturas')

urlpatterns = router.urls