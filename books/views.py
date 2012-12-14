#!/usr/bin/env python
from django.core.mail import send_mail
from reportlab.pdfgen import canvas
from books.forms import ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from books.models import Book
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template 
from django.http import HttpResponse 

def search(request):
    errors = [] 
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.') 
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.') 
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject':'I love you site!'}) 
    return render_to_response('contact_form.html',{'form':form})


def thanks(request):
    return render_to_response('thanks.html')

def about_pages(request,page):
    try:
        return direct_to_template(request,template="about/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404()

def my_image(request):
    image_data = open("/tmp/1.jpg","rb").read()
    return HttpResponse(image_data,mimetype="image/jpg")

def hello_pdf(request):
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    p = canvas.Canvas(response)
    p.drawString(100, 100, "Hello world.")
# Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
    
