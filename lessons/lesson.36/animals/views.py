from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from django.views.generic.base import ContextMixin
from .models import Animal
from .serializers import AnimalSerializer


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class SomeMessageMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['some_message'] = 'Same message'
        return context

class AnimalListView(ListView):
    model = Animal

class AboutTemplateView(TemplateView):
    template_name = 'animals/about.html'


def about_view(request):
    if request.is_get:
        return render(request, 'animals/about.html')
    else:
        raise Http404
