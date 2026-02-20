from django.shortcuts import render

def home(request):
    context = {}

    if request.method == "POST":
        context['title'] = request.POST.get('title')
        context['subtitle'] = request.POST.get('subtitle')
        context['tagline'] = request.POST.get('tagline')
        context['bgcolor'] = request.POST.get('bgcolor')
        context['fontcolor'] = request.POST.get('fontcolor')
        context['fontsize'] = request.POST.get('fontsize')
        context['image'] = request.POST.get('image')

    return render(request, 'cover/home.html', context)
