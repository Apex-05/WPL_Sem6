from django.shortcuts import render

def page1(request):

    if request.method == "POST":

        brand = request.POST.get("brand")
        items = request.POST.getlist("item")
        qty = int(request.POST.get("qty"))

        price = 0

        if "Mobile" in items:
            price += 10000

        if "Laptop" in items:
            price += 50000

        total = price * qty

        return render(request,"shop/bill.html",{
            "brand":brand,
            "items":items,
            "qty":qty,
            "total":total
        })

    return render(request,"shop/page1.html")