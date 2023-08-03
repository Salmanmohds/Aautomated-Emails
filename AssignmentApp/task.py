from celery import shared_task
from datetime import date
from django.core.mail import send_mail
from .models import Employee, EmployeeEmailTemplate
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status


@shared_task
def send_emails_event():
    """
        This function or task to Sending automated Emails
    """
    today = date.today()
    employee_data = Employee.objects.filter(Q(birthday__month=today.month, birthday__day=today.day) |
                                        Q(work_anniversary__month=today.month, work_anniversary__day=today.day))
    for employee in employee_data:
        if employee.birthday.month == today.month and employee.birthday.day == today.day:
            event_type = "Birthday"
        else:
            event_type = "Work Anniversary"

        try:
            email_template = EmployeeEmailTemplate.objects.get(event_type=event_type) # Getting Event Type
            subject = email_template.subject
            body = email_template.body.format(name=employee.name, event_type=event_type)
            send_mail(subject, body, 'salmanmohdk83@gmail.com', [employee.email])
        except Exception as error:
            print("Error",str(error))
            return Response({"message": "Something Went Wrong", "status": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)