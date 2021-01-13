from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
from django.http import HttpResponse





# Create your views here.
def register(request):
    if request.user.is_authenticated:

        if request.method == 'POST':

            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            student_id = request.POST['student_id']
            father_name =request.POST['father_name']
            mother_name = request.POST['mother_name']
            #date_of_birth = request.POST['birthday']
            phone_number = request.POST['phone_number']
            gender = request.POST['gender']
            address = request.POST['address']

            student = Student(first_name=first_name,last_name=last_name,student_id=student_id,father_name=father_name,mother_name=mother_name,phone_number=phone_number,gender=gender,address=address)
            student.save()

            print('Success!! Student Created!')
            html= "<script>alert(\"Registered!\");window.location.href = \"/home\";</script>"
            return HttpResponse(html)


        else:
            return render(request,'teacher/register_student.html')
    else:
        html= "<script>if (window.confirm(\'You must be logged in as a Teacher ! \')){window.location.href=\'/\';};</script>"
        return HttpResponse(html)


def editStudent(request):

    if request.method=='POST':
        student_id = request.POST['student_id']
        student = Student.objects.get(student_id=student_id)
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.student_id = request.POST['student_id']
        student.father_name =request.POST['father_name']
        student.mother_name = request.POST['mother_name']
        #date_of_birth = request.POST['birthday']
        student.phone_number = request.POST['phone_number']
        student.gender = request.POST['gender']
        student.address = request.POST['address']
        student.save()
        system_messages = messages.get_messages(request)
        for message in system_messages:
            # This iteration is necessary
            pass
        messages.success(request,"Success! Changes made.")
        return redirect("../../edit/fetchstudent")
        # html= "<script>if (window.confirm(\'Changes made!\')){window.location.href=\'/\';};</script>"
        # return HttpResponse(html)

    else:
        return render(request,'teacher/edit.html')

def fetchStudent(request):
    if request.method=='POST':
        student_id= request.POST['student_id']
        try:
            student = Student.objects.get(student_id=student_id)
            context = {'student_id':student.student_id,'first_name':student.first_name,'last_name':student.last_name,'father_name':student.father_name,'mother_name':student.mother_name,'phone_number':student.phone_number,'gender':student.gender,'address':student.address}
            return render(request,'teacher/edit_student.html',{'context':context})
        except:
            system_messages = messages.get_messages(request)
            for message in system_messages:
                # This iteration is necessary
                pass
            messages.info(request,"Student not found!")
            return redirect("../fetchstudent")

    else:
        return render(request,'teacher/edit.html')
