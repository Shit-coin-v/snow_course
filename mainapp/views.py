from rest_framework.viewsets import ModelViewSet

from mainapp.models import(
    Category, Course, CourseSchedule, LearningTechnology,
)

from mainapp.serializers import(
    CategorySerializer, CourseSerializer, 
    CourseScheduleSerializer, LearningTechnologySerializer,
)

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()                   
    serializer_class = CategorySerializer


class CourseView(ModelViewSet):
    queryset = Course.objects.all()                   
    serializer_class = CourseSerializer


class CourseScheduleView(ModelViewSet):
    queryset = CourseSchedule.objects.all()                   
    serializer_class = CourseScheduleSerializer


class LearningTechnologyView(ModelViewSet):
    queryset = LearningTechnology.objects.all()                   
    serializer_class = LearningTechnologySerializer