from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from meiduo_admin.serialziers import orders
from orders.models import OrderInfo
from meiduo_admin.utils import UserPageNum


class OrderView(ReadOnlyModelViewSet):
    serializer_class = orders.OrderSerializer
    queryset = OrderInfo.objects.all()
    pagination_class = UserPageNum

    # 重写get_queryset方法，根据前端是否传递keyword值返回不同查询结果
    def get_queryset(self):
        # 获取前端传递的keyword值
        keyword = self.request.query_params.get('keyword')
        # 如果keyword是空字符，则说明要获取所有用户数据
        if keyword == '' or keyword is None:
            return OrderInfo.objects.all()
        else:
            return OrderInfo.objects.filter(order_id__contains=keyword)

    # 在视图中定义status方法修改订单状态
    @action(methods=['put'], detail=True)
    def status(self, request, pk):
        # 获取订单对象
        order = self.get_object()
        # 获取要修改的状态值
        status = request.data.get('status')
        # 修改订单状态
        order.status = status
        order.save()
        # 返回结果
        # ser = self.get_serializer(order)
        return Response({
            'order_id': order.order_id,
            'status': status
        })