from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .models import About
from .forms import ContactForm


class CreateContact(CreateView):
    form_class = ContactForm
    success_url = '/'


class AboutView(View):
    def get(self, request):
        about = About.objects.last()
        form = ContactForm()
        return render(request, 'contact/about.html', {"about": about, "form": form})

