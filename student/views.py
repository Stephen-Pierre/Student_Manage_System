from django.http import HttpResponse
from django.shortcuts import render, redirect

from student.models import Grades, Students


# Create your views here.


def show_classes(request):
    """
    显示班级列表
    :param request:
    :return:
    """
    grade_list = Grades.objects.all()
    return render(request, 'show_classes.html', {'grade_list': grade_list})


def add_grade(requset):
    """
    添加班级
    :param requset:
    :return:
    """
    return render(requset, 'add_grade.html')


def add_grade_01(request):
    grade_name = request.POST.get('grade_name')
    grade = Grades()
    grade.grades_name = grade_name
    grade.save()
    return redirect('/student/show_classes/')


def alter_grade(request):
    """
    修改班级信息
    :param request:
    :return:
    """
    nid = request.GET.get('nid')
    grade = Grades.objects.get(pk=nid)
    return render(request, 'alter_grade.html', {'nid': nid, 'grade_name': grade.grades_name})


def alter_grade_01(request):
    nid = request.GET.get('nid')
    grade = Grades.objects.get(pk=nid)
    grade.grades_name = request.POST.get('grade_name')
    grade.save()
    return redirect('/student/show_classes/')


def delete_grade(request):
    """
    删除班级信息
    :param request:
    :return:
    """
    nid = request.GET.get('nid')
    grade = Grades.objects.get(pk=nid)
    grade.delete()
    return redirect('/student/show_classes/')


def show_students(request):
    """
    显示学生列表
    :param request:
    :return:
    """
    student_list = Students.objects.all()
    return render(request, 'show_student.html', {'student_list': student_list})


def add_student(request):
    grade_list = Grades.objects.all()
    if request.method == 'GET':
        return render(request, 'add_student.html', {'grade_list': grade_list})
    else:
        student_name = request.POST.get('student_name')
        grade_id = request.POST.get('grade')
        student = Students()
        student.student_name = student_name
        student.student_grade_id = grade_id
        student.save()
        return redirect('/student/show_students/')


def delete_student(request):

    nid = request.GET.get('nid')
    student = Students.objects.get(pk=nid)
    student.delete()
    return redirect('/student/show_students/')


def alter_student(request):
    grade_list = Grades.objects.all()
    if request.method == 'GET':
        nid = request.GET.get('nid')
        student = Students.objects.get(pk=nid)
        return render(request, 'alter_student.html', {'nid': nid, 'student_name': student.student_name, 'grade_list': grade_list})
    else:
        student_name = request.POST.get('student_name')
        student_grade_id = request.POST.get('grade')
        nid = request.GET.get('nid')
        student = Students.objects.get(pk=nid)
        student.student_name = student_name
        student.student_grade_id = student_grade_id
        student.save()
        return redirect('/student/show_students/')
