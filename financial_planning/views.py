from django.shortcuts import render

def financial_planning(request):
    return render(request, 'financial_planning/index.html')