from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from goods.models import SKUImage, SKU
from meiduo_admin.serialziers import images
from meiduo_admin.utils import UserPageNum
from rest_framework.response import Response
from fdfs_client.client import Fdfs_client, get_tracker_conf


class ImagesView(ModelViewSet):
    serializer_class = images.ImageSerializers  # 指定序列化器
    queryset = SKUImage.objects.all().order_by("id")  # 指定查询集
    pagination_class = UserPageNum

    def simple(self, request):
        """
        获取规格所关联的商品图片
        """
        spus = SKU.objects.all()
        ser = images.SKUSerializers(spus, many=True)
        return Response(ser.data)

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     ser = self.get_serializer(data=data)
    #     ser.is_valid()
    #     ser.save()
    #     return Response(ser.data, status=201)

