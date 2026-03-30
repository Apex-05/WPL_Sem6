from django.shortcuts import render, redirect
from .models import Works, Lives
from .forms import WorksForm, CompanySearchForm


def home(request):
    return render(request, 'directory/home.html')


def add_work(request):
    form = WorksForm()
    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'directory/add_work.html', {'form': form})


def search_company(request):
    form = CompanySearchForm()
    results = []

    if request.method == 'POST':
        form = CompanySearchForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company_name']

            works_people = Works.objects.filter(company_name__iexact=company)

            for work in works_people:
                lives = Lives.objects.filter(person_name=work.person_name).first()
                if lives:
                    results.append({
                        'person': work.person_name,
                        'city': lives.city
                    })

    return render(request, 'directory/search_company.html', {
        'form': form,
        'results': results
    })