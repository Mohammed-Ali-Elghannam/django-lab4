# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Trainee
# from course_app.models import Course
# from .forms import TraineeForm ,Traineeformmodel

# def add_trainee(request):
#     courses = Course.objects.all()  
#     if request.method == 'POST':
#         form = TraineeForm(request.POST)
#         if form.is_valid():
#             course_id = request.POST.get('course')  
#             course = Course.objects.get(id=course_id) if course_id else None

#             Trainee.objects.create(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 phone=form.cleaned_data['phone'],
#                 course=course  
#             )
#             return redirect('trainee_list')
#     else:
#         form = TraineeForm()

#     return render(request, 'trainee/add_trainee.html', {'form': form, 'courses': courses})

# def add_trainee(request):
#     if request.method == 'POST':
#         form = TraineeForm(request.POST, request.FILES)  # Handle file uploads
#         if form.is_valid():
#             form.save()
#             return redirect('trainee_list')
#     else:
#         form = TraineeForm()
    
#     return render(request, 'trainee/add_trainee.html', {'form': form})





# def update_trainee(request, trainee_id):
#     trainee = get_object_or_404(Trainee, id=trainee_id)
    
#     if request.method == "POST":
#         form = Traineeformmodel(request.POST, instance=trainee)
#         if form.is_valid():
#             form.save()
#             return redirect('trainee_list')
#     else:
#         form = Traineeformmodel(instance=trainee)

#     courses = Course.objects.all()  

#     return render(request, 'trainee/update_trainee.html', {
#         'form': form,
#         'courses': courses,  
#     })


# def trainee_list(request):
#     trainees = Trainee.objects.all()  
#     return render(request, 'trainee/trainee_list.html', {'trainees': trainees})


# def delete_trainee(request, trainee_id):
#     trainee = get_object_or_404(Trainee, id=trainee_id)  
#     if request.method == 'POST':
#         trainee.delete()  
#         return redirect('trainee_list')  

#     return render(request, 'trainee/delete_trainee.html', {'trainee': trainee})

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView ,DetailView
from django.shortcuts import get_object_or_404, render
from .models import Trainee
from .forms import TraineeForm, Traineeformmodel
from course_app.models import Course

# Generic View for Listing Trainees
class TraineeListView(ListView):
    model = Trainee
    template_name = 'trainee/trainee_list.html'
    context_object_name = 'trainees'


# Generic View for Showing Trainee Details
class TraineeDetailView(DetailView):
    model = Trainee
    template_name = 'trainee/trainee_detail.html'
    context_object_name = 'trainee'


# Class-Based View for Creating Trainees
class TraineeCreateView(View):
    template_name = 'trainee/add_trainee.html'

    def get(self, request):
        form = TraineeForm()
        courses = Course.objects.all()
        return render(request, self.template_name, {'form': form, 'courses': courses})

    def post(self, request):
        form = TraineeForm(request.POST)
        if form.is_valid():
            course_id = request.POST.get('course')
            course = Course.objects.get(id=course_id) if course_id else None
            Trainee.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                course=course
            )
            return redirect('trainee_list')
        courses = Course.objects.all()
        return render(request, self.template_name, {'form': form, 'courses': courses})


# Class-Based View for Updating Trainees
class TraineeUpdateView(View):
    template_name = 'trainee/update_trainee.html'

    def get(self, request, pk):
        trainee = get_object_or_404(Trainee, id=pk)
        form = Traineeformmodel(instance=trainee)
        courses = Course.objects.all()
        return render(request, self.template_name, {'form': form, 'courses': courses})

    def post(self, request, pk):
        trainee = get_object_or_404(Trainee, id=pk)
        form = Traineeformmodel(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
        courses = Course.objects.all()
        return render(request, self.template_name, {'form': form, 'courses': courses})

# Generic View for Deleting Trainees
class TraineeDeleteView(DeleteView):
    model = Trainee
    template_name = 'trainee/delete_trainee.html'
    success_url = reverse_lazy('trainee_list')
