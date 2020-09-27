from rest_framework import serializers
from goods.models import SPUSpecification, SPU


class SpecsSerializers(serializers.ModelSerializer):
    """
    规格序列化器
    """
    # 关联嵌套返回spu表的商品名
    spu = serializers.StringRelatedField(read_only=True)
    # 返回关联spu的id值
    spu_id = serializers.IntegerField()

    class Meta:
        model = SPUSpecification
        fields = "__all__"


class SPUSerializer(serializers.ModelSerializer):
    """
    SPU序列化器
    """
    class Meta:
        model = SPU
        fields = ('id', 'name')


