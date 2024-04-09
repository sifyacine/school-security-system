from django.shortcuts import render, redirect
from .forms import StudentReportForm, StaffReportForm
from .utils import save_student_report, save_staff_report

def add_student_report(request):
    if request.method == 'POST':
        form = StudentReportForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.cleaned_data['student']
            report_title = form.cleaned_data['report_title']
            report_content = form.cleaned_data['report_content']
            attachment = form.cleaned_data['attachment']
            save_student_report(student, report_title, report_content, attachment)
            return redirect('dashboard_home')
    else:
        form = StudentReportForm()
    return render(request, 'student_report.html', {'form': form})

def add_staff_report(request):
    if request.method == 'POST':
        form = StaffReportForm(request.POST, request.FILES)
        if form.is_valid():
            staff = form.cleaned_data['staff']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            attachment = form.cleaned_data['attachment']
            save_staff_report(staff, subject, message, attachment)
            return redirect('dashboard_home')
    else:
        form = StaffReportForm()
    return render(request, 'staff_report.html', {'form': form})