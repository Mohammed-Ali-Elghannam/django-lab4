from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from course_app.models import Course
from .forms import TraineeForm ,Traineeformmodel

def add_trainee(request):
    courses = Course.objects.all()  
    if request.method == 'POST':
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
    else:
        form = TraineeForm()

    return render(request, 'trainee/add_trainee.html', {'form': form, 'courses': courses})


def update_trainee(request, trainee_id):
    trainee = get_object_or_404(Trainee, id=trainee_id)
    
    if request.method == "POST":
        form = Traineeformmodel(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = Traineeformmodel(instance=trainee)

    courses = Course.objects.all()  

    return render(request, 'trainee/update_trainee.html', {
        'form': form,
        'courses': courses,  
    })


def trainee_list(request):
    trainees = Trainee.objects.all()  
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})


def delete_trainee(request, trainee_id):
    trainee = get_object_or_404(Trainee, id=trainee_id)  
    if request.method == 'POST':
        trainee.delete()  
        return redirect('trainee_list')  

    return render(request, 'trainee/delete_trainee.html', {'trainee': trainee})

