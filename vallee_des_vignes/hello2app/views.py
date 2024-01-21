from django.shortcuts import render

def Hello(request):
    return render(request, 'a_template_for_pe3.html')