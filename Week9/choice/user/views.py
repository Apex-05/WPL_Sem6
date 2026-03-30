from django.shortcuts import render

votes = {
    "good":0,
    "satisfactory":0,
    "bad":0
}

def vote_page(request):

    if request.method == "POST":

        choice = request.POST.get("rating")

        if choice in votes:
            votes[choice] += 1

        total = sum(votes.values())

        result = {
            "good": round((votes["good"]/total)*100),
            "satisfactory": round((votes["satisfactory"]/total)*100),
            "bad": round((votes["bad"]/total)*100)
        }

        return render(request,"user/result.html",result)

    return render(request,"user/vote.html")