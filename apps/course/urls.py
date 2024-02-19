from django.urls import path

from apps.course.api_endpoints import course

urlpatterns = [
    # course list
    path('course_lists/', course.CourseListsAPIView.as_view(), name='course_lists'),
    path('course_categorylits/', course.CourseCategoryListApiView.as_view(), name='course_categorylits'),
    path('course_detail/<int:pk>/', course.CourseDetailAPIView.as_view(), name='course_detail'),
    path('favourite/course/', course.FavouriteCourseAPIListView.as_view(), name='favourite_course'),
    path('videouserviewcreate/', course.CourseVideoLessonAPIView.as_view(), name='video_userviewcreate'),
]
