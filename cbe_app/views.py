from django.shortcuts import render
from django.views.generic import View
from .models import Event, Team, Contact
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json


class HomeView(View):
    template_name = 'cbe_app/index.html'

    def get(self, request):
        events = Event.objects.all()
        teams = Team.objects.all()
        return render(request, self.template_name, {"events": events, "teams": teams})


class ContactView(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
        message = data['message']
        exists = Contact.objects.filter(email=email).exists()
        if (exists):
            return JsonResponse({"added": False})
        else:
            contact = Contact()
            contact.email = email
            contact.message = message
            contact.name =name
            contact.save()
            return JsonResponse({"added": True})
        return JsonResponse({})
