from django.conf.urls import url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from meiduo_admin.views import statistical

urlpatterns = [
    # url(r'^', admin.site.urls),
    # 登录
    url(r'^authorizations/$', obtain_jwt_token),
    # ------------------数据统计----------------------
    # 数据统计总量
    url(r'^statistical/total_count/$', statistical.UserCountView.as_view()),
    # 新增用户统计
    url(r'^statistical/day_increment/$', statistical.UserDayCountView.as_view()),
    # 日活跃用户
    url(r'^statistical/day_active/$', statistical.UserActiveCountView.as_view()),
    # 下单用户
    url(r'^statistical/day_orders/$', statistical.UserOrdersCountView.as_view()),
    # 月增用户
    url(r'^statistical/month_increment/$', statistical.UserIncrementCountView.as_view()),
    # 日分类商品访问量
    url(r'^statistical/goods_day_views/$', statistical.GoodsDayView.as_view()),



]
