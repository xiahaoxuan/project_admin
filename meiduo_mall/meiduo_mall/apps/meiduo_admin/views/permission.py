from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Permission, ContentType
from meiduo_admin.serialziers import permission
from meiduo_admin.utils import UserPageNum
from rest_framework.response import Response


class PermissionView(ModelViewSet):
    serializer_class = permission.PermissionSerializer  # 指定序列化器
    queryset = Permission.objects.all()  # 指定查询集
    pagination_class = UserPageNum   # 指定分页器

    def content_types(self, request):
        content = ContentType.objects.all().order_by("id")
        ser = permission.ContentTypeSerializer(content, many=True)
        return Response(ser.data)

