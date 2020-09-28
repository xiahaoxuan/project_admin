from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from rest_framework_jwt.views import obtain_jwt_token
from meiduo_admin.views import statistical, users, specs, images
from rest_framework.routers import DefaultRouter

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

    # ------------------用户管理----------------------
    # 用户的查询获取/(?P<keyword>\d+)/(?P<page>\d+)/(?P<pagesize>\d+)/
    url(r'^users/$', users.ClassView.as_view()),
    # ------------------规格表路由----------------------
    # url(r'^goods/specs/(?P<pk>\d+)/$', specs.SaveSpecsView.as_view({'get': "retrieve", "put": "update"})),
    url(r'^goods/simple/$', specs.SpecsView.as_view({'get': "simple"})),
    url(r'^skus/simple/$', images.ImagesView.as_view({'get': "simple"})),
]
# ------------------规格表路由----------------------
router = DefaultRouter()
router.register(r'goods/specs', specs.SpecsView)
# ------------------图片表路由----------------------
router.register(r'goods/images', images.ImagesView)
urlpatterns += router.urls






