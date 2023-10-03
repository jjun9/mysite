from django.http import HttpResponse
# from.models import Question


def index(request):
      return HttpResponse("Hello World.")

