from django.shortcuts import render

# Grocery items dictionary
ITEMS = {
    "Wheat": 40,
    "Rice": 50,
    "Dal": 80,
    "Sugar": 45,
    "Jaggery": 60
}

def grocery_page(request):
    selected_items = []

    if request.method == "POST":
        checked_items = request.POST.getlist('items')

        for item in checked_items:
            selected_items.append({
                "name": item,
                "price": ITEMS[item]
            })

    context = {
        "items": ITEMS,
        "selected_items": selected_items
    }

    return render(request, "grocery.html", context)