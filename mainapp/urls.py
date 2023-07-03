from rest_framework.routers import DefaultRouter as DR

from mainapp.views import(
   CategoryView, CourseView, CourseScheduleView, LearningTechnologyView
)

router = DR()

router.register('category', CategoryView)
router.register('course', CourseView)
router.register('CourseSchedule', CourseScheduleView)
router.register('LearningTechnology', LearningTechnologyView)


urlpatterns = []

urlpatterns += router.urls