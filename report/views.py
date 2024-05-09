from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        render(request,'report_form.html')
    else:
        redirect()