from rest_framework import serializers
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


class SKUSerializers(serializers.ModelSerializer):

    class Meta:
        model = SKU
        fields = ('id', 'name')


