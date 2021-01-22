from django.shortcuts import render
from django.urls import reverse_lazy
from myApp.models import Student
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
class StudentListView(ListView):
    model=Student
    #default template=student_list.html
    #default context=student_list
class StudentDetailView(DetailView):
    model=Student
    #default template=student_detail.html
    #default context=student_detail
class StudentCreateView(CreateView):
    model=Student
    fields=('name','number','marks','place')
    #default template=student_form.html
class StudentUpdateView(UpdateView):
    model=Student  
    fields=('name','marks')
    #default template=student_form.html
class StudentDeleteView(DeleteView):
    model=Student    
    success_url=reverse_lazy('students')
    #default template=student_confirm_delete.html
