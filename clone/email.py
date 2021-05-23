from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    #Creating message subject and sender
    subject = 'Welcome to Instagram'
    sender = 'attackonbangtan553@gmail.com'

    #passing in the context variables
    ext_content = render_to_string('email/cloneemail.txt',{"name": name})
    html_content = render_to_string('email/cloneemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()