from django.forms import Form, CharField


class AddStudentForm(Form):
	studentname = CharField(label='Name', max_length=20)
	grades = CharField(label='Grades', max_length=100)
