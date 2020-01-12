from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello_viewset',views.HelloViewSets,base_name='hello_viewset')
router.register('profile',views.UserProfileViewSets)


urlpatterns = [
        path('hello_view/',views.HelloApiView.as_view()),
        path('',include(router.urls))
]
