from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from datetime import date, timedelta

from goods.models import GoodsVisitCount
from meiduo_admin.serialziers.statistical import GoodsSerializer
from users.models import User


class GoodsDayView(APIView):
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当天日期
        now_date = date.today()
        # 获取当天访问的商品分类数量信息
        data = GoodsVisitCount.objects.filter(date=now_date)
        # 序列化返回分类数量
        ser = GoodsSerializer(data, many=True)
        return Response(ser.data)


class UserIncrementCountView(APIView):
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当前日期
        now_date = date.today()
        # 获取一个月前日期
        # 获取第一天
        first = now_date.replace(day=1)
        # 获取前一天
        last_month = first - timedelta(days=1)
        # 获取前一个月的天数
        num_date = last_month.day
        # 获取一个月之前的日期
        start_date = now_date - timedelta(days=num_date)

        date_list = []

        for i in range(num_date+1):
            index_date = start_date + timedelta(days=i)
            cur_date = start_date + timedelta(days=i+1)
            count = User.objects.filter(date_joined__gte=index_date, date_joined__lt=cur_date).count()
            date_list.append({
                'count': count,
                'date': index_date
            })
        return Response(date_list)


class UserOrdersCountView(APIView):
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当前日期
        now_date = date.today()
        # 获取当日下单用户数量  orders__create_time 订单创建时间
        count = User.objects.filter(orders__create_time__gte=now_date).count()
        return Response({
            "count": count,
            "date": now_date
        })


class UserActiveCountView(APIView):
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当前日期
        now_date = date.today()
        # 获取当日登录用户数量  last_login记录最后登录时间
        count = User.objects.filter(last_login__gte=now_date).count()
        return Response({
            "count": count,
            "date": now_date
        })


class UserCountView(APIView):
    # 权限指定
    permission_classes = [IsAdminUser]

    def get(self, request):
        now_date = date.today()
        count = User.objects.all().count()
        return Response({
            "date": now_date,
            "count": count,
        })


class UserDayCountView(APIView):
    # 权限指定
    permission_classes = [IsAdminUser]

    def get(self, request):
        now_date = date.today()
        count = User.objects.filter(date_joined__gte=now_date).count()
        return Response({
            "count": count,
            "date": now_date
        })






