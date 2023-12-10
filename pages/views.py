from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import FeedbackForm, ProductForm
from .models import Feedback
# Create your views here.

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class SuccesPageView(TemplateView):
    template_name = "success.html"




def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Submitted.')
            return redirect('success')
    else:
        f = FeedbackForm()
    return render(request, 'contact.html', {'form': f})

def success(request):
    if request.method == 'POST':
        contact = Feedback()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        pass
    return render(request, 'success.html')



def addProduct(request):
    form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'addProduct.html')






