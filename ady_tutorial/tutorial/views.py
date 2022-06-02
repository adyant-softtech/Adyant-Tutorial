from dataclasses import fields
from multiprocessing import context
from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render
from tutorial.models import Student

from tutorial.forms import StudentForm, UpdateForm

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.urls import reverse

# Create your views here.

#create -- create
#read -- all, get, filter 
#update -- update
#delete -- delete


def index(request):    
    return HttpResponse('Hello Adyant')

def home(request):
    context = {}
    context['name'] = 'Hello Adyant'
    print('I called home.....')
    return HttpResponse('Welcome to Adyant Home Page')

def welcome(request):
    context = {}
    context['name'] = 'Hello Adyant'
    return render(request, 'welcome.html', context)
    #return HttpResponse('Welcome Adyant')

def adyant(request):
    return HttpResponse("we are all adyant student")

def registerform(request):
    context = {}
    data = dict()
    if request.POST:
        data['id'] = request.POST.get('student_id')
        data['name'] = request.POST.get('stu_name')
        data['class'] = request.POST.get('stu_class')
        data['branch'] = request.POST.get('stu_branch')
        data['collage'] = request.POST.get('collage_name')
        data['course'] = request.POST.get('course')
        data['address'] = request.POST.get('address')

        print("sgdgfgdfhgd", data)

        if data:
            created = Student.objects.create(
                student_id= data['id'],
                stu_name = data['name'],
                stu_class = data['class'],
                stu_branch = data['branch'],
                collage_name = data['collage'],
                course= data['course'],
                address = data['address']
            )

            if created:
                message = "Student registration is successful"

        context['msg'] = message

    
    data = Student.objects.all()

    context['data'] = data
    context['form'] = StudentForm()
        
    print(data)

    return render(request, 'register.html', context)

def updateForm(request):
    context = {}
    data = Student.objects.all()
    context['data'] = data
    context['form'] = UpdateForm()
    if request.POST.get('update'):
        name = request.POST.get('student_name')
        address = request.POST.get('address')
        #Student.objects.filter(stu_name=name).update(address=address)
        student = Student.objects.get(stu_name=name)
        student.address = address
        student.save()
    
    if request.POST.get('delete'):
        name = request.POST.get('student_name')
        #Student.objects.filter(stu_name=name).delete()
        student = Student.objects.get(stu_name=name)
        student.delete()

    return render(request, 'update.html', context)


class StudentDetailView(DetailView):
    model = Student
    #by default it look for template in same directory (app directory)
    template_name = 'tutorial/templates/student_detail.html'

class StudentListView(ListView):
    model = Student
    #by default it look for template in same directory (app directory)
   
    def get_queryset(self, *args, **kwargs):
        # qs = super(StudentListView, self).get_queryset(*args, **kwargs)
        # qs = qs[:3]
        # return qs

        return Student.objects.all()
        #return Student.objects.filter(address='raipur')

    template_name = 'tutorial/templates/student_list.html'

class StudentCreateView(CreateView):
    model = Student
    fields = ['student_id', 'stu_name', 'stu_class', 'stu_branch', 'collage_name', 'course', 'address']
    template_name = 'tutorial/templates/student_create.html'
    
    def get_success_url(self):
        return reverse('students', kwargs={'pk': self.object.pk})

class StudentData(ListView):
    model = Student
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        context = {}
        context['object_list'] = students
        return render(request, 'student_list.html', context)

    def post(self, request, *args, **kwargs):
        pass



    

# function based views
#class based view
    #1st option:
        # CreateView
        # DetailView/ListView
        # UpdateView
        # DeleteView
    #2nd option:
        #ListView/GenericView/View
        #get/post == perform the operations



    



