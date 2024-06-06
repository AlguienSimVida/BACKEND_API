from rest_framework import routers
from .api import PineappleViewSet

router=routers.DefaultRouter()

router.register('api/pineapple', PineappleViewSet, 'pineapple')

urlpatterns=router.urls