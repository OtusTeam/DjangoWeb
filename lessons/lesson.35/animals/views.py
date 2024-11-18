import time
from rest_framework.viewsets import ModelViewSet
from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import Animal
from .serializers import AnimalSerializer

# Create your views here.
class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class IndexView(TemplateView):
    template_name = 'animals/index.html'

    def get(self, *args, **kwargs):
        time.sleep(1)
        print('POST', self.request.is_post)
        return super().get(*args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['api_info'] = 'API V1. Animals'
    #     return context

# class AboutView(TemplateView):
#     template_name = 'animals/about.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['api_info'] = 'API V1. Animals'
    #     return context
def about_view(request):
    # if request.method == 'GET':
    if request.is_get:
        return render(request, "animals/about.html")
    elif request.is_post:
        raise Exception

# def other_view(request):
#     context = dict()
#     context['api_info'] = 'API V1. Animals'
#     return render(request, 'animals/other.html', context=context)