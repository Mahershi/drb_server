from django.urls import path
from rest_framework import routers
from .views import TestViewSet, UserViewSet, CreateExistingToken, ProductMetaViewset, CategoryViewSet
from .views import BrandViewSet, ParameterViewSet, StoreViewSet, DiscountViewSet
from .views import DisposableViewSet, PodViewSet, JuiceViewSet, OrderView

router = routers.DefaultRouter()
router.register('test', TestViewSet)
router.register('user', UserViewSet)
router.register('product_meta', ProductMetaViewset)
router.register('category', CategoryViewSet)
router.register('brand', BrandViewSet)
router.register('parameters', ParameterViewSet)
router.register('stores', StoreViewSet)
router.register('discount', DiscountViewSet)
router.register('disposable', DisposableViewSet)
router.register('pod', PodViewSet)
router.register('juice', JuiceViewSet)
router.register('orders', OrderView)



urlpatterns = [
    path('tokens', CreateExistingToken.as_view(), name='gentoken_existing'),
    # path('login', ObtainAuthTokenViewSet.as_view(), name='login'),

]

urlpatterns += router.urls
