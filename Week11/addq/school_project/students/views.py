from django.shortcuts import render, redirect
from .models import Student

def student_entry(request):
    if request.method == "POST":
        # Get data from the form
        sid = request.POST.get('student_id')
        sname = request.POST.get('name')
        scourse = request.POST.get('course')
        sdob = request.POST.get('dob')

        # Save to Database
        Student.objects.create(
            student_id=sid,
            name=sname,
            course=scourse,
            dob=sdob
        )
        # Redirect to the same page to see the updated list
        return redirect('student_entry')

    # Fetch all students to display in the table
    all_students = Student.objects.all()
    return render(request, 'students/entry.html', {'students': all_students})