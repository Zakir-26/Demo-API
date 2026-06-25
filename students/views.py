from django.shortcuts import render
from .forms import StudentCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "students/home.html")

def studentsapi(request):
    pass


@login_required
def add(request):

    form = StudentCreationForm()
    message = ""

    if request.method == "POST":
        form = StudentCreationForm(request.POST)

        if form.is_valid():
            form.save()

            message = f"Student added succesfully"
            form = StudentCreationForm()

        else:
            form = StudentCreationForm()


    return render(request, "students/add.html", {"form":form, "messages":message})


def dashboard(request):
    return render(request, "students/dashboard.html")
