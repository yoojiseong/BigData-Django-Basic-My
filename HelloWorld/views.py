from django.http import HttpResponse

#MVC패턴에서 C(Controller)의 역할은 장고의 MVT에서 V가 역할을 맡음
def django_view(request):
    return HttpResponse("Django View")