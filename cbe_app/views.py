from django.shortcuts import render
from django.views.generic import View
from .models import Event,Team

class HomeView(View):
    template_name = 'cbe_app/index.html'
    def get(self,request):
        events = Event.objects.all()
        teams= Team.objects.all()
        return render(request,self.template_name ,{"events":events,"teams":teams})