from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from . import services


class ClassCourse(APIView):

    permission_classes = []

    def get(self, request, class_id):
        course = services.get_class_course(class_id)
        if not course:
            raise NotFound

        return Response(course)


class ClassCourseOptionsView(APIView):

    permission_classes = []

    @method_decorator(cache_page(60 * 60 * 1))
    def get(self, request):
        return Response(services.get_class_course_options())
