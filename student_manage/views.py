# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect
# from . models import Student
# from .forms import StudentForm
# # Create your views here.

# def list_student(request):
#     student = Student.objects.all()
#     context = {
#         'student': student
#     }
#     return render(request, 'student_manage/show.html', context)



# def update_student(request, pk):
#     if request.method == "POST":
        
#         student = Student.objects.get(pk=pk)
#         form = StudentForm(instance= student)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         student = Student.objects.get(pk=pk)
#         form = StudentForm(instance= student)
#     context = {
#         'student': student,
#         'form': form
#     }
#     return render(request, 'student_manage/adddata.html', context)


# def deletedata(request, pk):
#     if request.method == 'post':
#         student = Student.objects.get(pk=pk)
#         student.delete()
#         return HttpResponseRedirect("/")
    
    
# def searchstudent(request):
#     if request.method == 'POST':
#         n1 = request.POST.get('output')
#         print(n1)
#         student = Student.objects.all()
#         std = None  # Initialize the variable
#         if n1:
#             std = student.filter(
#                 Q(fname__icontains=n1) |
#                 Q(lname__icontains=n1) |
#                 Q(email__icontains=n1) |
#                 Q(phone__icontains=n1) |
#                 Q(branch__icontains=n1)
#             )
#             print( std.count())
#         return render(request, "student_manage/show.html", {'student': std})
#     else:
#         return HttpResponse('An Exception Occurred')


from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .models import Student
from .forms import StudentForm
from django.db.models import Q


def show (request):
    student=Student.objects.all()
    return render (request, "student_manage/show.html",{'student':student})



def adddata(request):
    if request.method == "POST":
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm=StudentForm()
    return render (request,"student_manage/adddata.html",{'form':fm})



def updatedata(request ,id):
    if request.method=="POST":
        student=Student.objects.get(pk=id)
        fm=StudentForm(request.POST,instance=student)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect("/")
    else:
        student=Student.objects.get(pk=id)
        fm=StudentForm(instance=student)
    return render (request, "student_manage/update.html",{'form':fm})


def deletedata(request ,id):
    if request.method=="POST":
        student=Student.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect("/")


def searchstudent(request):
    if request.method == 'POST':
        n1 = request.POST.get('output')
        print(n1)
        student = Student.objects.all()
        std = None  # Initialize the variable
        if n1:
            std = student.filter(
                Q(fname__icontains=n1) |
                Q(lname__icontains=n1) |
                Q(email__icontains=n1) |
                Q(phone__icontains=n1) |
                Q(branch__icontains=n1)
            )
            print( std.count())
        return render(request, "student_manage/show.html", {'student': std})
    else:
        return HttpResponse('An Exception Occurred')