from django.shortcuts import render

def home(request):
    return render(request, 'library/home.html')

def metadata(request):
    return render(request, 'library/metadata.html')

def reviews(request):
    return render(request, 'library/reviews.html')

def publisher(request):
    return render(request, 'library/publisher.html')
