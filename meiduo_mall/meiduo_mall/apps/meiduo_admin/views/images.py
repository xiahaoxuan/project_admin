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

    def create(self, request, *args, **kwargs):
        data = request.data
        ser = self.get_serializer(data=data)
        ser.is_valid()
        path = get_tracker_conf(conf_path=settings.FASTDFS_PATH)
        client = Fdfs_client(path)
        file = request.FILES.get('image')
        res = client.upload_by_buffer(file.read())
        if res["Status"] != 'Upload successed.':
            return Response({'error': '图片上传失败'})

        # 获取上传后的路径
        image_url = res['Remote file_id'].decode()

        # 获取sku_id
        sku_id = request.data.get('sku')[0]
        # 保存图片
        img = SKUImage.objects.create(sku_id=sku_id, image=image_url)
        return Response({
            "id": img.id,
            "sku": img.sku_id,
            "image": img.image.url
        })

