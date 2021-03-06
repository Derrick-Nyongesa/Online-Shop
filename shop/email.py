from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to Albany e-Shop'
    sender = 'derrdan592@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/welcome.txt',{"name": name})
    html_content = render_to_string('email/welcome.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def payment_recieved_email(name,receiver):
    # Creating message subject and sender
    subject = 'Payment Successful'
    sender = 'derrdan592@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('payment/payment.txt',{"name": name})
    html_content = render_to_string('payment/payment.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()