"""greydo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from games.views import GameReadOnlyView, get_name_id_by_name
from events.views import GameEndView, GameStartView, BaseEventView

from progression.views import ProgressionView


router = routers.DefaultRouter()
router.register('games', GameReadOnlyView)
router.register('events', BaseEventView)
router.register('game_start', GameStartView)
router.register('game_end', GameEndView)
router.register(r'progression(/(?P<user_id>\d+)/(?P<game_name>\w+))?', ProgressionView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('game_id/<str:name>', get_name_id_by_name),
    path('admin/', admin.site.urls),
#    path('static/', None)
]
