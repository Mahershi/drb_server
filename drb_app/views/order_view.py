from django.http import QueryDict
from ..models import OrderModel, ProductMetaModel, StoreModel, DisposableModel
from ..models import PodModel, JuiceModel, DisposableStockModel, PodStockModel
from ..models import JuiceStockModel
from ..serializers import OrderSerializer
from rest_framework.decorators import action
from rest_framework.request import Request
from ..helper import customResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny



class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
    permission_classes = [AllowAny]


    @action(methods=['POST'], detail=False)
    def place(self, request: Request, *args, **kwargs):
        qp: QueryDict = request.query_params
        if qp.get('store') is None:
            return customResponse(success=False)
        else:
            store = qp.get('store')
            data = request.data
            for inst in data:
                product: ProductMetaModel = ProductMetaModel.objects.get(pk=inst['product'])
                order: OrderModel = OrderModel(
                    product= product,
                    store=StoreModel.objects.get(pk=store),
                    total=inst['total'],
                    subtotal=inst['subtotal'],
                    tax=inst['tax'],
                    qty=inst['qty']
                )
                flavs = []
                counts = []
                for flav in inst['flavours']:
                    if product.category.id == 1:
                        try:
                            dispoStock: DisposableStockModel = DisposableStockModel.objects.get(
                                disposable=DisposableModel.objects.get(pk=flav['flavour_id']),
                                store=StoreModel.objects.get(pk=store)
                            )

                            dispoStock.stock -= int(flav['count'])
                            dispoStock.save()
                        except Exception as e:
                            pass

                    elif product.category.id == 2:
                        try:
                            juiceStock: JuiceStockModel = JuiceStockModel.objects.get(
                                juice=JuiceModel.objects.get(pk=flav['flavour_id']),
                                store=StoreModel.objects.get(pk=store)
                            )

                            juiceStock.stock -= int(flav['count'])
                            juiceStock.save()
                        except Exception as e:
                            pass
                    elif product.category.id == 3:
                        try:
                            podStock: PodStockModel = PodStockModel.objects.get(
                                pod=PodStockModel.objects.get(pk=flav['flavour_id']),
                                store=StoreModel.objects.get(pk=store)
                            )

                            podStock.stock -= int(flav['count'])
                            podStock.save()
                        except Exception as e:
                            pass


                    flavs.append(flav['flavour_id'])
                    counts.append(flav['count'])

                order.flavour = flavs
                order.flav_count = counts
                order.save()
                serializer: OrderSerializer = OrderSerializer(order, many=False)

            return customResponse(success=True, data=serializer.data)