from django.shortcuts import render, redirect
from .forms import EntryForm
from .models import Entry
from django.db.models import Avg

# HOME
def home(request):
    return render(request, 'home.html')

# FORM PAGE
def add_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suggestions')
    else:
        form = EntryForm()
    return render(request, 'suggestions.html', {'form': form})

# DISPLAY PAGE
def display(request):
    data = Entry.objects.all().order_by('-id')
    avg = Entry.objects.exclude(rating__isnull=True).aggregate(Avg('rating'))['rating__avg']
    return render(request, 'viewsuggestions.html', {'data': data, 'avg': avg})

# CONDITIONAL REDIRECT PAGE (for price > 200)
def detail(request, id):
    obj = Entry.objects.filter(id=id).first()
    data = Entry.objects.all().order_by('-id')
    
    if not obj:
        return render(request, 'viewsuggestions.html', {'error': 'Entry not found.', 'data': data})
    
    if obj.price and obj.price > 200:
        request.session['name'] = obj.name
        request.session['price'] = obj.price
        return redirect('final')
    
    return render(request, 'viewsuggestions.html', {'error': 'Price must be >= 200', 'data': data})

def final_page(request):
    return render(request, 'final.html')