"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from api.views import MemberListAPI, TeamListAPI, LectureListAPI, LectureAPI, CourseAPI, CourseListAPI, MemberAPI, TeamAPI, TakenAPI, TakenListAPI, SyncAPI

urlpatterns = [
    path('admin/', admin.site.urls),
	path('api/member/', MemberListAPI.as_view()),
	path('api/member/<int:id>', MemberAPI.as_view()),
	path('api/team/', TeamListAPI.as_view()),
	path('api/team/<int:id>', TeamAPI.as_view()),
    path('api/lecture/', LectureListAPI.as_view()),
    path('api/lecture/<int:id>', LectureAPI.as_view()),
    path('api/course/', CourseListAPI.as_view()),
	path('api/course/<int:id>', CourseAPI.as_view()),
    path('api/taken', TakenListAPI.as_view()),
	path('api/taken/<int:id>', TakenAPI.as_view()),
    path('api/sync', SyncAPI.as_view()),
]
