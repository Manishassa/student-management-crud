from django.shortcuts import render,get_object_or_404
from .models import Student
from django.shortcuts import redirect

# Create your views here.
# READ - List Students
def student_list(request):
    students=Student.objects.all()
    return render(request,'students/list.html',{'students':students})


# CREATE - Add Student


# render() = "Show this page right here." (Stay on same page)

# redirect() = "Go to another page (browser makes a new request)."

def create_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')      
        email = request.POST.get('email')     
        # age = request.POST.get('age')         
        Branch = request.POST.get('Branch') 

        Student.objects.create(name=name,email=email,Branch=Branch)
        return redirect('student_list')
    return render(request,'students/create.html')


# UPDATE - Edit Student

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email'] #branch = request.POST['Branch']
        # student.age = request.POST['age']
        student.Branch = request.POST['Branch']
        student.save()
        return redirect('student_list')
    return render(request, 'students/update.html', {'student': student})

# DELETE - Remove Student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')









#  When the user visits the page (GET request)

# Example: The user clicks "Add Student" link → Browser sends a GET request to /create/.

# At this time, we want to show the blank form to the user so they can enter details.

# Hence:

# return render(request, 'students/create.html')


# renders the template with the form.

# 2) When the user submits the form (POST request)

# After filling the form and clicking submit → Browser sends a POST request to /create/.

# Now, we take the form data, create the student in DB, and then:

# return redirect('student_list')