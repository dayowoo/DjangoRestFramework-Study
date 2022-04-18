from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quickstart import views

# views대신에 viewset을 사용하기 때문에, 자동적으로 URL을 설정할 수 있음.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
