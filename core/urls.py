from garden_center.api.v1.views.garden_center_view import Garden_centerViewSet
from garden_center.api.v1.views.plant_view import PlantViewSet
from garden_center.api.v1.views.category_view import CategoryViewSet
from garden_center.api.v1.views.founder_view import FounderViewSet
from purchaser.api.v1.views.balance_view import BalanceViewSet
from purchaser.api.v1.views.purchaser_view import PurchaserViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'plant', PlantViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'garden_center', Garden_centerViewSet)
router.register(r'founder', FounderViewSet)
router.register(r'balance', BalanceViewSet)
router.register(r'purchaser', PurchaserViewSet)

urlpatterns = router.urls