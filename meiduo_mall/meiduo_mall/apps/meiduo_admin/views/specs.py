from rest_framework.viewsets import ModelViewSet
from goods.models import SPUSpecification, SPU
from meiduo_admin.serialziers import specs
from meiduo_admin.utils import UserPageNum
from rest_framework.response import Response


class SpecsView(ModelViewSet):
    """
    商品规格的增删改查
    """
    # 指定查询集
    queryset = SPUSpecification.objects.all()
    # 指定序列化器
    serializer_class = specs.SpecsSerializers

    pagination_class = UserPageNum

    def simple(self, request):
        """
        获取规格所关联的商品
        """
        spus = SPU.objects.all()
        ser = specs.SPUSerializer(spus, many=True)
        return Response(ser.data)

    # def destroy(self, request, *args, **kwargs):
    #     spec = self.get_object()
    #     spec.is_delete = True
    #     spec.save()










