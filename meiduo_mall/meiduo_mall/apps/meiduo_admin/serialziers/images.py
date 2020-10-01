from django.conf import settings
from fdfs_client.client import Fdfs_client, get_tracker_conf
from rest_framework import serializers
from rest_framework.response import Response
from celery_tasks.static_file.tasks import get_detail_html


from goods.models import SKUImage, SKU


class ImageSerializers(serializers.ModelSerializer):
    """
    商品图片序列化器
    """
    # sku = serializers.StringRelatedField(read_only=True)
    # sku_id = serializers.IntegerField()

    class Meta:
        model = SKUImage
        fields = "__all__"

    def create(self, validated_data):
        path = get_tracker_conf(conf_path=settings.FASTDFS_PATH)
        client = Fdfs_client(path)
        request = self.context["request"]
        file = request.FILES.get('image')
        res = client.upload_by_buffer(file.read())
        if res["Status"] != 'Upload successed.':
            raise serializers.ValidationError({'error': '图片上传失败'})
        # 获取上传后的路径
        image_url = res['Remote file_id'].decode()
        # 获取sku_id
        sku_id = request.data.get('sku')[0]
        # 保存图片
        img = SKUImage.objects.create(sku_id=sku_id, image=image_url)
        # get_detail_html.delay(img.sku_id)
        return img

    def update(self, instance, validated_data):
        path = get_tracker_conf(conf_path=settings.FASTDFS_PATH)
        client = Fdfs_client(path)
        request = self.context["request"]
        file = request.FILES.get('image')
        res = client.upload_by_buffer(file.read())
        if res["Status"] != 'Upload successed.':
            raise serializers.ValidationError({'error': '图片上传失败'})
        # 获取上传后的路径
        image_url = res['Remote file_id'].decode()
        # 获取sku_id
        sku_id = request.data.get('sku')[0]
        # 更新图片
        instance.image = image_url
        instance.save()
        # get_detail_html.delay(sku_id)
        # img = SKUImage.objects.update(sku_id=sku_id, image=image_url)
        return instance


class SKUSerializers(serializers.ModelSerializer):

    class Meta:
        model = SKU
        fields = ('id', 'name')


