from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quickstart import views
from snippets import views

# views대신에 viewset을 사용하기 때문에, 자동적으로 URL을 설정할 수 있음.
'''
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('snippets.urls'))
]

'''
잘못된 형식의 json을 보내거나 뷰가 처리하지 않는 방법으로 요청할 경우
500 서버 오류 반환
'''