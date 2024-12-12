from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterUserFormClass, PacienteForm, RecetaForm, CitaForm, HistorialFrom, LoginUserForm, ReporteForm
from .models import Receta, Paciente, Citas, Historial, RegisterUserForm, Reporte
import datetime

# Librerias e imports para generar PDFs
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Image
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph

# Estilo para los parrafos
my_Style=ParagraphStyle('My Para style',
    fontName='Helvetica',
    fontSize=12,
)


# View para generar PDFs
# Historiales
def pdf_historial(request, historial_id):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    

    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    historial = Historial.objects.get(pk=historial_id)
    
    lines = [] 
    lines.append("Historial médica") 
    lines.append("--------------------")
    lines.append("Paciente: " + historial.paciente.nombre + ' ' + historial.paciente.apellido_paterno + ' ' + historial.paciente.apellido_materno)
    lines.append("Fecha: " + str(historial.fecha))
    lines.append("--------------------")
    lines.append("Evaluación Muscular")
    lines.append("")
    lines.append("Derecha")
    lines.append("Cuello: " + str(historial.cuello_d))
    lines.append("Torso: " + str(historial.torso_d))
    lines.append("Miembro superior: " + str(historial.m_sup_d))
    lines.append("Miembro Inferior: " + str(historial.m_inf_d))
    lines.append("")
    lines.append("Izquierda")
    lines.append("Cuello: " + str(historial.cuello_i))
    lines.append("Torso: " + str(historial.torso_i))
    lines.append("Miembro superior: " + str(historial.m_sup_i))
    lines.append("Miembro Inferior: " + str(historial.m_inf_i))
    lines.append("--------------------")
    lines.append("Evaluación Goniométrica")
    lines.append("")
    lines.append("Derecha")
    lines.append("Cuello: " + str(historial.cuello_dg))
    lines.append("Torso: " + str(historial.torso_dg))
    lines.append("Miembro superior: " + str(historial.m_sup_dg))
    lines.append("Miembro Inferior: " + str(historial.m_inf_dg))
    lines.append("")
    lines.append("Izquierda")
    lines.append("Cuello: " + str(historial.cuello_ig))
    lines.append("Torso: " + str(historial.torso_ig))
    lines.append("Miembro superior: " + str(historial.m_sup_ig))
    lines.append("Miembro Inferior: " + str(historial.m_inf_ig))
    lines.append("--------------------")
    lines.append("Evaluación Miembros Superiores / Hombro")
    lines.append("")
    lines.append("Hombro")
    lines.append("")
    lines.append("Derecha")
    lines.append("Fexión vertical: " + str(historial.flexv_ms_hd))
    lines.append("Fexión horizontal: " + str(historial.flexh_ms_hd))
    lines.append("Extensión vertical: " + str(historial.extv_ms_hd))
    lines.append("Extensión horizontal: " + str(historial.exth_ms_hd))
    lines.append("Abducción (ABD): " + str(historial.abd_ms_hd))
    lines.append("Aducción (ADD): " + str(historial.add_ms_hd))
    lines.append("Rotación externa: " + str(historial.rotext_ms_hd))
    lines.append("Rotación interna: " + str(historial.rotint_ms_hd))
    lines.append("")
    lines.append("Izquierda")
    lines.append("Fexión vertical: " + str(historial.flexv_ms_hi))
    lines.append("Fexión horizontal: " + str(historial.flexh_ms_hi))
    lines.append("Extensión vertical: " + str(historial.extv_ms_hi))
    lines.append("Extensión horizontal: " + str(historial.exth_ms_hi))
    lines.append("Abducción (ABD): " + str(historial.abd_ms_hi))
    lines.append("Aducción (ADD): " + str(historial.add_ms_hi))
    lines.append("Rotación externa: " + str(historial.rotext_ms_hi))
    lines.append("Rotación interna: " + str(historial.rotint_ms_hi))
    lines.append("")
    lines.append("Brazo")
    lines.append("")
    lines.append("Codo Derecha")
    lines.append("Fexión: " + str(historial.flex_ms_bd))
    lines.append("Extensión: " + str(historial.ext_ms_bd))
    lines.append("")
    lines.append("Antebrazo Derecho")
    lines.append("Pronación: " + str(historial.pron_ms_bd))
    lines.append("Supinación: " + str(historial.susp_ms_bd))
    lines.append("")
    lines.append("Codo Izquierda")
    lines.append("Fexión: " + str(historial.flex_ms_bi))
    lines.append("Extensión: " + str(historial.ext_ms_bi))
    lines.append("")
    lines.append("Antebrazo Izquierda")
    lines.append("Pronación: " + str(historial.pron_ms_bi))
    lines.append("Supinación: " + str(historial.susp_ms_bi))
    lines.append("")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='receta.pdf')

# Recetas
def pdf_receta(request, receta_id):
    buf = io.BytesIO()
    
    medico = RegisterUserForm.objects.filter(id=1).first()
    receta = Receta.objects.get(pk=receta_id)

    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    
    c.drawImage("./mystaticfiles/assets/logo3.png", 40, 48, width=120, height=60)

    textob = c.beginText()
    textob.setTextOrigin(170, 64)
    textob.setFont("Helvetica-Bold", 14)
    
    textob.textLine("Dr. " + medico.nombre + " " + medico.apellido_paterno + " " + medico.apellido_materno)
    textob.setFont("Helvetica", 9)
    textob.textLine("Fisioterapeuta" + "  Cedula profesional: " + medico.cedula)
    textob.setTextOrigin(170, 104)
    textob.textLine("Telefono: " + medico.telefono + "  Dirección: " +
                    medico.direccion + "  Fecha: " + str(datetime.datetime.now().date()))
    c.drawText(textob)

    c.line(40, 110, 555, 110)

    textob.setTextOrigin(50,130)    
    textob.setFont("Helvetica", 9)    
    textob.textLine("Paciente: " + receta.paciente.nombre + ' '  
                 + receta.paciente.apellido_paterno + ' ' + receta.paciente.apellido_materno)
    textob.setTextOrigin(450, 125)    
    textob.textLine("Edad: " + str(receta.paciente.edad))
    textob.textLine("Sexo: " + receta.paciente.sexo)
    textob.textLine("Peso: " + str(receta.paciente.peso))
    textob.textLine("Altura: " + str(receta.paciente.altura))
    textob.textLine("Presion: " + receta.paciente.presion)

    textob.setTextOrigin(50,150)    
    textob.setFont("Helvetica", 9)    
    
    textob.textLine("Diagnostico médico: " + receta.diagnostico) 
    textob.setTextOrigin(50, 170)
    textob.textLine("Tratamiento:")
    textob.textLine(receta.medicamento + ". " + receta.forma + ". " + receta.dosis + ". " + 
                    receta.frecuencia + ". " + receta.via + ". " + receta.duracion + ". " +
                    receta.indicaciones)

    c.line(40, 300, 555, 300)
    
    textob.setFont("Helvetica", 9)    
    textob.setTextOrigin(380, 320)    
    textob.textLine("Firma: ")    
    c.line(409, 322, 550, 322)
    
    textob.setTextOrigin(420, 335)
    textob.textLine("Dr. " + medico.nombre + " " + medico.apellido_paterno + " " + medico.apellido_materno)

    c.drawText(textob)

    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='receta.pdf')

# Reportes
def pdf_reporte(request, reporte_id):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    reporte = Reporte.objects.get(pk=reporte_id)
    medico = RegisterUserForm.objects.filter(id=1).first()

    t = c.beginText()
    t.setTextOrigin(240, 80)
    t.setFont("Helvetica-Bold", 14)

    t.textLine("REPORTE MÉDICO")

    t.setTextOrigin(inch, 110)
    t.setFont("Helvetica-Bold", 12)

    t.textLine("MEDICO")
    t.textLine("CEDULA PROFESIONAL")
    t.textLine("PACIENTE")
    t.textLine("EDAD")
    t.textLine("DIRECCIÓN")
    t.textLine("TELEFONO")
    t.textLine("FECHA")

    t.setTextOrigin(230, 108.5)
    t.textLine(":")
    t.textLine(":")
    t.textLine(":")
    t.textLine(":")
    t.textLine(":")
    t.textLine(":")
    t.textLine(":")

    t.setTextOrigin(240, 108.5)
    t.setFont("Helvetica", 12)
    t.textLine(medico.nombre + " " + medico.apellido_paterno + " " + medico.apellido_materno)
    t.textLine(medico.cedula)
    t.textLine(reporte.paciente.nombre + " " + reporte.paciente.apellido_paterno + " " + reporte.paciente.apellido_materno)
    t.textLine(str(reporte.paciente.edad))
    t.textLine(reporte.paciente.direccion)
    t.textLine(str(reporte.paciente.telefonoP))
    t.textLine(str(datetime.datetime.now().date()))
    c.line(40, 205, 555, 205)
    
    c.drawImage("./mystaticfiles/assets/logo3.png", 390, 110, width=150, height=75)


    t.setTextOrigin(inch, 225)
    t.setFont("Helvetica-Bold", 12)
    t.textLine("DIAGNOSTICO")

    p1=Paragraph(reporte.diagnostico, my_Style)
    p1.wrapOn(c, 475, 500 )
    p1.drawOn(c, 72, 218)

    t.setTextOrigin(inch, 325)
    t.setFont("Helvetica-Bold", 12)
    t.textLine("MOTIVO DE CONSULTA")

    p1=Paragraph(reporte.motivoconsulta, my_Style)
    p1.wrapOn(c, 475, 500 )
    p1.drawOn(c, inch, 318)

    t.setTextOrigin(inch, 425)
    t.setFont("Helvetica-Bold", 12)
    t.textLine("DESCRIPCIÓN")

    p1=Paragraph(reporte.descripcion, my_Style)
    p1.wrapOn(c, 475, 500 )
    p1.drawOn(c, inch, 418)

    t.setTextOrigin(inch, 525)
    t.setFont("Helvetica-Bold", 12)
    t.textLine("COMPROMISO")

    p1=Paragraph(reporte.compromisos, my_Style)
    p1.wrapOn(c, 475, 500 )
    p1.drawOn(c, inch, 518)

    t.setTextOrigin(inch, 625)
    t.setFont("Helvetica-Bold", 12)
    t.textLine("FECHA DE NUEVA CONSULTA:")
    
    t.setTextOrigin(257, 625)
    t.setFont("Helvetica", 12)
    t.textLine(str(reporte.fechasnconsulta))
    
    t.setFont("Helvetica", 10)    
    t.setTextOrigin(380, 672)    
    t.textLine("Firma: ")    
    c.line(409, 675, 550, 675)

    t.setTextOrigin(420, 686)
    t.textLine("Dr. " + medico.nombre + " " + medico.apellido_paterno + " " + medico.apellido_materno)



    """    
    lines = [] 
    lines.append("Reporte médico")
    lines.append("---------------------")
    lines.append("Paciente: " + reporte.paciente.nombre + ' ' + reporte.paciente.apellido_paterno + ' ' + reporte.paciente.apellido_materno)
    lines.append("Diagnostico: " + reporte.diagnostico)
    lines.append("Fecha: " + str(reporte.fecha))
    lines.append("Motivo de consulta: " + reporte.motivoconsulta)
    lines.append("Descripción: " + reporte.descripcion)
    lines.append("Compromisos: " + reporte.compromisos)
    lines.append("---------------------")
    lines.append("Proxima fechas de consulta: " + str(reporte.fechasnconsulta))
    lines.append("Proxima hora de consulta: " + str(reporte.horanconsulta))
    """

    c.drawText(t)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='receta.pdf')

def base(request):
    return render(request, "./base.html")

def index(request):
    return render(request, "./index.html")

def aboutus(request):
    return render(request,"./aboutus.html")

def login_view(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = RegisterUserForm.objects.get(username=username)
            except RegisterUserForm.DoesNotExist:
                user = None
                
            if user is not None and user.check_password(password):
                login(request, user)
                return redirect('home')
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("./login.html")
    
def home(request):
    info_citas = Citas.objects.all
    info_historial = Historial.objects.all
    info_reportes = Reporte.objects.all
    return render(request, "./home.html", {'citas': info_citas, 'historiales' : info_historial, 'reportes' : info_reportes})

def register(request):
    if request.method == "POST":
        form = RegisterUserFormClass(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect("login")
            
    else:
        form = RegisterUserFormClass()
    return render(request, "./register.html", { "form": form})

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        
        message = f"Hola {name} {lname},\n\nGracias por contactarnos. Nos comunicaremos contigo al número {telephone} o al correo {email}."
        send_mail(
            subject="Gracias por contactarnos",
            message=message,
            from_email="myphysiomx@gmail.com",
            recipient_list=[email],
            fail_silently=False,
        )
    return render(request, "contacts.html")

def dashboard_home(request):
    return render(request,"./dashboard_home.html")

def pacientes(request):
    info_paciente = Paciente.objects.all
    return render(request, "./pacientes.html", {'all': info_paciente})

def reg_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('El paciente fue registrado correctamente'))
            return redirect("pacientes")
    else:
        messages.success(request, ('Error'))
        form = PacienteForm()
    return render(request, "reg_paciente.html", {"form": form})

def update_paciente(request, paciente_id):
    paciente = Paciente.objects.get(pk=paciente_id)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect("pacientes")
    return render(request, "./update_paciente.html", {'paciente': paciente, 'form': form})

def delete_paciente(request, paciente_id):
    paciente = Paciente.objects.get(pk=paciente_id)
    paciente.delete()
    return redirect('pacientes')

def mostrar_paciente(request, paciente_id):
    paciente = Paciente.objects.get(pk=paciente_id)
    return render(request, "./mostrar_paciente.html", {'paciente': paciente})


def recetas(request):
    info_receta = Receta.objects.all
    return render(request, "./recetas.html", {'all': info_receta})

def recetaspa(request):
    info_receta = Receta.objects.all
    return render(request, "./recetaspa.html", {'all': info_receta})

def reg_recetas (request):
    if request.method == "POST":
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('El paciente fue registrado correctamente'))
            return redirect("recetas")
    else:
        messages.success(request, ('Error'))
        form = RecetaForm()
    return render(request, "reg_recetas.html", {"form": form})

def reg_recetaspa (request):
    if request.method == "POST":
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Receta creada exitosamente!'))
            return redirect("recetaspa")
    else:
        messages.success(request, ('Error'))
        form = RecetaForm()
    return render(request, "reg_recetaspa.html", {"form": form})

def update_receta(request, receta_id):
    receta = Receta.objects.get(pk=receta_id)
    form = RecetaForm(request.POST or None, instance=receta)
    if form.is_valid():
        form.save()
        return redirect("recetas")
    return render(request, "./update_receta.html", {'receta': receta, 'form': form})

def delete_receta(request, receta_id):
    receta = Receta.objects.get(pk=receta_id)
    receta.delete()
    return redirect('recetas')

def citas(request):
    info_citas = Citas.objects.all
    return render(request, "./citas.html", {'all': info_citas})

def citaspa(request):
    info_citas = Citas.objects.all
    return render(request, "./citaspa.html", {'all': info_citas})
    
def reg_citas(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Cita agendada exitosamente!'))
            return redirect("citas")
    else:
        messages.success(request, ('Error'))
        form = CitaForm()
    return render(request, "reg_citas.html", {"form": form})

def reg_citaspa(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Cita agendada exitosamente!'))
            return redirect("citaspa")
    else:
        messages.success(request, ('Error'))
        form = CitaForm()
    return render(request, "reg_citaspa.html", {"form": form})

def update_cita(request, cita_id):
    cita = Citas.objects.get(pk=cita_id)
    form = CitaForm(request.POST or None, instance=cita)
    if form.is_valid():
        form.save()
        return redirect("citas")
    return render(request, "./update_cita.html", {'cita': cita, 'form': form})

def delete_cita(request, cita_id):
    cita = Citas.objects.get(pk=cita_id)
    cita.delete()
    return redirect('citas')

def historial2(request):
    return render(request,"./historial2.html")

def historial(request):
    info_historial = Historial.objects.all
    return render(request, "./historial.html", {'all': info_historial})

def historialpa(request):
    info_historial = Historial.objects.all
    return render(request, "./historialpa.html", {'all': info_historial})

def mostrar_historial(request, historial_id):
    historial = Historial.objects.get(pk=historial_id)
    return render(request, "./mostrar_historial.html", {'historial': historial})

def reg_historial (request):
    if request.method == "POST":
        form = HistorialFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('El historial fue registrado correctamente'))
            return redirect("historial")
    else:
        messages.success(request, ('Error'))
        form = HistorialFrom()
    return render(request, "reg_historial.html", {"form": form})

def reg_historialpa (request):
    if request.method == "POST":
        form = HistorialFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('El historial fue registrado correctamente'))
            return redirect("historialpa")
    else:
        messages.success(request, ('Error'))
        form = HistorialFrom()
    return render(request, "reg_historialpa.html", {"form": form})


def update_historial(request, historial_id):
    historial = Historial.objects.get(pk=historial_id)
    form = HistorialFrom(request.POST or None, instance=historial)
    if form.is_valid():
        form.save()
        return redirect("historial")
    return render(request, "./update_historial.html", {'historial': historial, 'form': form})

def delete_historial(request, historial_id):
    historial = Historial.objects.get(pk=historial_id)
    historial.delete()
    return redirect('historial')

def reportemedico(request):
    info_reporte = Reporte.objects.all
    return render(request, "./reportemedico.html", {'all': info_reporte})

def reg_reporte (request):
    if request.method == "POST":
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('El reporte fue registrado correctamente'))
            return redirect("reportemedico")
    else:
        messages.success(request, ('Error'))
        form = ReporteForm()
    return render(request, "reg_reporte.html", {"form": form})

def update_reporte(request, reporte_id):
    reporte = Reporte.objects.get(pk=reporte_id)
    form = ReporteForm(request.POST or None, instance=reporte)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            nueva_fecha_consulta = form.cleaned_data.get("fechasnconsulta")
            nueva_hora_consulta = form.cleaned_data.get("horanconsulta")
            try:
                cita, created = Citas.objects.update_or_create(
                    paciente=reporte.paciente,
                    defaults={
                        "fecha": nueva_fecha_consulta,
                        "hora": nueva_hora_consulta,
                    }
                )

                if created:
                    print(f"Cita creada para: {reporte.paciente.nombre}")
                else:
                    print(f"Cita actualizada para: {reporte.paciente.nombre}")

            except ValidationError as e:
                form.add_error(None, f"Error: {e.message}")
                return render(request, "./update_reporte.html", {'reporte': reporte, 'form': form})

            return redirect("reportemedico")

    return render(request, "./update_reporte.html", {'reporte': reporte, 'form': form})

def delete_reporte(request, reporte_id):
    reporte = Reporte.objects.get(pk=reporte_id)
    reporte.delete()
    return redirect('reportemedico')

def dashboard_homepa(request):
    return render(request, "./dashboard_homepa.html")

def loginpa(request):
    return render(request, "./loginpa.html")

def reportemedicopa(request):
    info_reporte = Reporte.objects.all
    return render(request, "./reportemedicopa.html", {'all': info_reporte})

