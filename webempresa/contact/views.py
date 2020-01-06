from django.shortcuts import render, redirect
from django.urls import reverse
from .froms import ContactForm
# liberia para enviar un mensaje
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    #print("tipo de peticion: {}".format(request.method))
    contact_from = ContactForm()
    if request.method == "POST":
        contact_from = ContactForm(data=request.POST)
        if contact_from.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            # si todo sali bien, enviamos el correo 
            email = EmailMessage(
                "Gracias por deja su comentario",
                "De {} <{}>\n\nSu comentario es:\n\n{}".format(name,email,content),
                'no-contestar@smtp.mailtrap.io',
                ["poncho936537@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                # valio queso hay un fallo en capa 8
                return redirect(reverse('contact')+"?fallo")

    return render(request,"contact/contact.html", {'form':contact_from})