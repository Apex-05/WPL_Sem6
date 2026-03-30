from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Human

def human_manage(request):
    humans = Human.objects.all()
    
    if request.method == "POST":
        human_id = request.POST.get('human_id')
        if not human_id:
            return redirect('human_manage')
            
        human = get_object_or_404(Human, id=human_id)
        
        if 'update' in request.POST:
            human.first_name = request.POST.get('first_name')
            human.last_name = request.POST.get('last_name')
            human.phone = request.POST.get('phone')
            human.address = request.POST.get('address')
            human.city = request.POST.get('city')
            human.save()
            
        elif 'delete' in request.POST:
            human.delete()
            
        return redirect('human_manage')

    return render(request, 'shop/human_manage.html', {'humans': humans})

# AJAX View to send data to the textboxes
def get_human_details(request, human_id):
    human = get_object_or_404(Human, id=human_id)
    data = {
        'first_name': human.first_name,
        'last_name': human.last_name,
        'phone': human.phone,
        'address': human.address,
        'city': human.city,
    }
    return JsonResponse(data)