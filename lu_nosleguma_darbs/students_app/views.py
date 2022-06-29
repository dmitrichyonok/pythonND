from django.shortcuts import render

from students_app.studentClass import Student
from students_app.models import StudentModel


def get_all_students(request):
	context = {
		'students': StudentModel.objects.all()
	}
	
	return render(request,
	              template_name='all_students.html',
	              context=context)


def get_student(request, student_id):
	context = {
		'StudentModel': Student.objects.get(id=student_id)
	}
	
	return render(request,
	              template_name='student.html',
	              context=context)


def add_student(request):
	from students_app.forms import AddStudentForm
	form = AddStudentForm(request.POST or None)
	
	if form.is_valid():
		newstudent = StudentModel(form.cleaned_data['studentname'],
		                          form.cleaned_data['grades'],
		                          )
		newstudent.average_grade = get_average_grade(newstudent.grades)
		newstudent.save()
		
		context = {
			'NewStudent': newstudent,
		}
		
		return render(request,
		              template_name='student.html',
		              context=context)
	
	context = {
		'form': form,
	}
	
	return render(request,
	              template_name='add_student.html',
	              context=context)


def get_average_grade(grades):
	grades = list(map(int, grades.split(',')))
	avg = sum(grades) / len(grades)

	return avg
