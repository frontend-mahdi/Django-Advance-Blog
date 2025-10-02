"""core URL Configuration

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

from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "api-v1"

router = DefaultRouter()
router.register("post", viewset=views.PostModelViewSet, basename="post")
router.register("category", viewset=views.CategoryModelViewSet, basename="category")

urlpatterns = router.urls

# urlpatterns = [
#     path("post/", views.PostViewSet.as_view({'get':'list'}), name="post-list"),
#     path("post/<int:pk>/", views.PostViewSet.as_view({'get':'retrive','delete':'destroy','put':'update'}), name="post-detail"),
# ]
