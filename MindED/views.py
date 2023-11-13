from django.http import JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import PacienteForm
from django.core.paginator import Paginator
from .models import paciente,intervencion
from azureml.core import Workspace, Model
from django.http import JsonResponse
from .forms import FiltroFechaForm
import urllib.request
from datetime import datetime, time
import json
import os
import ssl



def registro(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    email=request.POST['email']
                )
                user.dni = request.POST['dni']
                user.nombres = request.POST['nombres']
                user.apellidos = request.POST['apellidos']
                user.fecha_nacimiento = request.POST['fecha_nacimiento']                
                user.save()
                login(request,user)
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'registro.html', {'form': UserCreationForm, 'error': 'El usuario o correo ya existe'})
        else:
            return render(request, 'registro.html', {'form': UserCreationForm, 'error': 'Las contraseñas no coinciden'})
    else:
        return render(request, 'registro.html', {'form': UserCreationForm})


def inicio(request):
    return render(request,'inicio.html')

def test(request):
    return render(request,'Test.html')

def create_paciente(request):
    if request.method =='GET':
        return render(request,'AgregarPaciente.html',{
        'form':PacienteForm
        })
    else:
        try:
            form=PacienteForm(request.POST)
            new_paciente=form.save(commit=False)
            new_paciente.user=request.user
            new_paciente.save()
            return redirect('paciente')
        except ValueError:
         return render(request,'AgregarPaciente.html',{
        'form':PacienteForm,
        'error': 'Por favor ingrese datos válidos'
        })   
        

def pacientes(request):
    pacientes_list = paciente.objects.filter(user=request.user)
    paginator = Paginator(pacientes_list, 5)  # 5 pacientes por página
    page = request.GET.get('page')
    pacientes = paginator.get_page(page)
    mostrar_paginacion = pacientes.paginator.count > 5
    return render(request, 'HistorialPaciente.html', {'pacientes': pacientes, 'mostrar_paginacion': mostrar_paginacion})

def paciente_detail(request, paciente_id):
    if request.method == 'GET':
        Paciente = get_object_or_404(paciente, pk=paciente_id)
        form = PacienteForm(instance=Paciente)
        
        form.fields['DNI'].widget.attrs['readonly'] = True
        form.fields['DNI'].widget.attrs['disabled'] = True
        return render(request, 'EditarPaciente.html', {'Paciente': Paciente, 'form': form})
    else:
        Paciente = get_object_or_404(paciente, pk=paciente_id)
        form = PacienteForm(request.POST.copy(), instance=Paciente)  
        
        original_dni = Paciente.DNI
        if 'DNI' in form.changed_data:
            form.data['DNI'] = original_dni
        
        form.save()
        return redirect('paciente')
    
def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    if request.method =='GET':
        return render(request,'index.html',{
        'form': AuthenticationForm
    })
    else:
        user= authenticate(
            request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'index.html',{
            'form': AuthenticationForm,
            'error':'El nombre de usuario o contraseña es incorrecto'
        })
        else:
            login(request,user)
            return redirect('inicio')


def buscar_pacientes(request):
      nombre_paciente = request.GET.get('nombre', '')    
    
      pacientes_encontrados = paciente.objects.filter(
        nombre__icontains=nombre_paciente,
        user=request.user
    )

      nombres_pacientes = [paciente.nombre for paciente in pacientes_encontrados]

      return JsonResponse(nombres_pacientes, safe=False)



def encuesta_view(request):        
    if request.method == 'POST':      
        nombre_paciente = request.POST['nombre_paciente']
        PacienteN = None
        paciente_id = None
        
        try:
            PacienteN = paciente.objects.get(nombre__icontains=nombre_paciente)
            paciente_id = PacienteN.N_Paciente  
        except paciente.DoesNotExist:
            paciente_id = None


        titulo = str(request.POST.get('titulo', ''))
        descripcion = str(request.POST.get('descripcion', ''))        
        pregunta1 = int(request.POST.get('pregunta1', 0))
        pregunta2 = int(request.POST.get('pregunta2', 0))
        pregunta3 = int(request.POST.get('pregunta3', 0))
        pregunta4 = int(request.POST.get('pregunta4', 0))
        pregunta5 = int(request.POST.get('pregunta5', 0))
        pregunta6 = int(request.POST.get('pregunta6', 0))
        pregunta7 = int(request.POST.get('pregunta7', 0))
        pregunta8 = int(request.POST.get('pregunta8', 0))
        pregunta9 = int(request.POST.get('pregunta9', 0))
        pregunta10 = int(request.POST.get('pregunta10', 0))
        pregunta11 = int(request.POST.get('pregunta11', 0))
        pregunta12 = int(request.POST.get('pregunta12', 0))
        pregunta13 = int(request.POST.get('pregunta13', 0))
        pregunta14 = int(request.POST.get('pregunta14', 0))
        pregunta15 = int(request.POST.get('pregunta15', 0))
        pregunta16 = int(request.POST.get('pregunta16', 0))
        pregunta17 = int(request.POST.get('pregunta17', 0))
        pregunta18 = int(request.POST.get('pregunta18', 0))
        pregunta19 = int(request.POST.get('pregunta19', 0))
        pregunta20 = int(request.POST.get('pregunta20', 0))
        pregunta21 = int(request.POST.get('pregunta21', 0))
        pregunta22 = int(request.POST.get('pregunta22', 0))
        pregunta23 = int(request.POST.get('pregunta23', 0))
        pregunta24 = int(request.POST.get('pregunta24', 0))
        pregunta25 = int(request.POST.get('pregunta25', 0))
        pregunta26 = int(request.POST.get('pregunta26', 0))
        pregunta27 = int(request.POST.get('pregunta27', 0))
        pregunta28 = int(request.POST.get('pregunta28', 0))
        pregunta29 = int(request.POST.get('pregunta29', 0))
        pregunta30 = int(request.POST.get('pregunta30', 0))
        pregunta31 = int(request.POST.get('pregunta31', 0))
        pregunta32 = int(request.POST.get('pregunta32', 0))
        pregunta33 = int(request.POST.get('pregunta33', 0))
        pregunta34 = int(request.POST.get('pregunta34', 0))
        pregunta35 = int(request.POST.get('pregunta35', 0))
        pregunta36 = int(request.POST.get('pregunta36', 0))
        pregunta37 = int(request.POST.get('pregunta37', 0))
        pregunta38 = int(request.POST.get('pregunta38', 0))
        pregunta39 = int(request.POST.get('pregunta39', 0))
        pregunta40 = int(request.POST.get('pregunta40', 0))
        pregunta41 = int(request.POST.get('pregunta41', 0))
        pregunta42 = int(request.POST.get('pregunta42', 0))
        pregunta43 = int(request.POST.get('pregunta43', 0))
        pregunta44 = int(request.POST.get('pregunta44', 0))
        pregunta45 = int(request.POST.get('pregunta45', 0))
        pregunta46 = int(request.POST.get('pregunta46', 0))
        pregunta47 = int(request.POST.get('pregunta47', 0))
        pregunta48 = int(request.POST.get('pregunta48', 0))
        pregunta49 = int(request.POST.get('pregunta49', 0))
        pregunta50 = int(request.POST.get('pregunta50', 0))
        pregunta51 = int(request.POST.get('pregunta51', 0))
        pregunta52 = int(request.POST.get('pregunta52', 0))
        pregunta53 = int(request.POST.get('pregunta53', 0))
        pregunta54 = int(request.POST.get('pregunta54', 0))
        pregunta55 = int(request.POST.get('pregunta55', 0))
        pregunta56 = int(request.POST.get('pregunta56', 0))
        pregunta57 = int(request.POST.get('pregunta57', 0))
        pregunta58 = int(request.POST.get('pregunta58', 0))
        pregunta59 = int(request.POST.get('pregunta59', 0))
        pregunta60 = int(request.POST.get('pregunta60', 0))
        pregunta61 = int(request.POST.get('pregunta61', 0))
        pregunta62 = int(request.POST.get('pregunta62', 0))
        pregunta63 = int(request.POST.get('pregunta63', 0))
        pregunta64 = int(request.POST.get('pregunta64', 0))
        pregunta65 = int(request.POST.get('pregunta65', 0))
        pregunta66 = int(request.POST.get('pregunta66', 0))
        pregunta67 = int(request.POST.get('pregunta67', 0))
        pregunta68 = int(request.POST.get('pregunta68', 0))
        pregunta69 = int(request.POST.get('pregunta69', 0))
        pregunta70 = int(request.POST.get('pregunta70', 0))
        pregunta71 = int(request.POST.get('pregunta71', 0))
        pregunta72 = int(request.POST.get('pregunta72', 0))
        pregunta73 = int(request.POST.get('pregunta73', 0))
        pregunta74 = int(request.POST.get('pregunta74', 0))
        pregunta75 = int(request.POST.get('pregunta75', 0))
        pregunta76 = int(request.POST.get('pregunta76', 0))
        pregunta77 = int(request.POST.get('pregunta77', 0))
        pregunta78 = int(request.POST.get('pregunta78', 0))
        pregunta79 = int(request.POST.get('pregunta79', 0))
        pregunta80 = int(request.POST.get('pregunta80', 0))
        pregunta81 = int(request.POST.get('pregunta81', 0))
        pregunta82 = int(request.POST.get('pregunta82', 0))
        pregunta83 = int(request.POST.get('pregunta83', 0))
        pregunta84 = int(request.POST.get('pregunta84', 0))
        pregunta85 = int(request.POST.get('pregunta85', 0))
        pregunta86 = int(request.POST.get('pregunta86', 0))
        pregunta87 = int(request.POST.get('pregunta87', 0))
        pregunta88 = int(request.POST.get('pregunta88', 0))
        pregunta89 = int(request.POST.get('pregunta89', 0))
        pregunta90 = int(request.POST.get('pregunta90', 0))
        pregunta91 = int(request.POST.get('pregunta91', 0))
        
        data =  {
        "Inputs": {
            "data": [
            {
           "1": pregunta1,
           "2": pregunta2,
           "4": pregunta4,
           "5": pregunta5,
           "7": pregunta7,
           "9": pregunta9,
           "11": pregunta11,
           "12": pregunta12,
           "16": pregunta16,
           "19": pregunta19,
           "25": pregunta25,
           "28": pregunta28,
           "31": pregunta31,
           "32": pregunta32,
           "38": pregunta38,
           "45": pregunta45,
           "46": pregunta46,
           "47": pregunta47,
           "49": pregunta49,
           "53": pregunta53,
           "55": pregunta55,
           "59":pregunta59,
           "61": pregunta61,
           "62": pregunta62,
           "64": pregunta64            
             }
            ]
        },
        "GlobalParameters": {
        "method": "predict"
        }
     }    
     
        body = str.encode(json.dumps(data))

        url = 'http://dd0795ab-f10f-4da2-bd84-2c6c16388310.eastus2.azurecontainer.io/score'
        api_key = 'Ivvtp7phlUIPOORs6IremjD8nG21L8bb'
        if not api_key:
            raise Exception("A key should be provided to invoke the endpoint")


        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.request.Request(url, body, headers)

        try: 
            response = urllib.request.urlopen(req)
            response_data = json.loads(response.read())
            result = response_data["Results"][0]        
            resultado_prediccion = int(round(result))
            print(resultado_prediccion)
        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))
            print(error.info())
            print(error.read().decode("utf8", 'ignore'))
            resultado_prediccion = None 

    # Guardar datos en base de datos
        Intervencion = intervencion(
            paciente_id=paciente_id,
            titulo=titulo,
            descripcion=descripcion, 
            Pregunta1=pregunta1,
            Pregunta2=pregunta2,
            Pregunta3=pregunta3,
            Pregunta4=pregunta4,
            Pregunta5=pregunta5,
            Pregunta6=pregunta6,
            Pregunta7=pregunta7,
            Pregunta8=pregunta8,
            Pregunta9=pregunta9,
            Pregunta10=pregunta10,
            Pregunta11=pregunta11,
            Pregunta12=pregunta12,
            Pregunta13=pregunta13,
            Pregunta14=pregunta14,
            Pregunta15=pregunta15,
            Pregunta16=pregunta16,
            Pregunta17=pregunta17,
            Pregunta18=pregunta18,
            Pregunta19=pregunta19,
            Pregunta20=pregunta20,            
            Pregunta21=pregunta21,
            Pregunta22=pregunta22,
            Pregunta23=pregunta23,
            Pregunta24=pregunta24,
            Pregunta25=pregunta25,
            Pregunta26=pregunta26,
            Pregunta27=pregunta27,
            Pregunta28=pregunta28,
            Pregunta29=pregunta29,
            Pregunta30=pregunta30,
            Pregunta31=pregunta31,
            Pregunta32=pregunta32,
            Pregunta33=pregunta33,
            Pregunta34=pregunta34,
            Pregunta35=pregunta35,
            Pregunta36=pregunta36,
            Pregunta37=pregunta37,
            Pregunta38=pregunta38,
            Pregunta39=pregunta39,
            Pregunta40=pregunta40,
            Pregunta41=pregunta41,
            Pregunta42=pregunta42,
            Pregunta43=pregunta43,
            Pregunta44=pregunta44,
            Pregunta45=pregunta45,
            Pregunta46=pregunta46,
            Pregunta47=pregunta47,
            Pregunta48=pregunta48,
            Pregunta49=pregunta49,
            Pregunta50=pregunta50,
            Pregunta51=pregunta51,
            Pregunta52=pregunta52,
            Pregunta53=pregunta53,
            Pregunta54=pregunta54,
            Pregunta55=pregunta55,
            Pregunta56=pregunta56,
            Pregunta57=pregunta57,
            Pregunta58=pregunta58,
            Pregunta59=pregunta59,
            Pregunta60=pregunta60,
            Pregunta61=pregunta61,
            Pregunta62=pregunta62,
            Pregunta63=pregunta63,
            Pregunta64=pregunta64,
            Pregunta65=pregunta65,
            Pregunta66=pregunta66,
            Pregunta67=pregunta67,
            Pregunta68=pregunta68,
            Pregunta69=pregunta69,
            Pregunta70=pregunta70,
            Pregunta71=pregunta71,
            Pregunta72=pregunta72,
            Pregunta73=pregunta73,
            Pregunta74=pregunta74,
            Pregunta75=pregunta75,
            Pregunta76=pregunta76,
            Pregunta77=pregunta77,
            Pregunta78=pregunta78,
            Pregunta79=pregunta79,
            Pregunta80=pregunta80,
            Pregunta81=pregunta81,
            Pregunta82=pregunta82,
            Pregunta83=pregunta83,
            Pregunta84=pregunta84,
            Pregunta85=pregunta85,
            Pregunta86=pregunta86,
            Pregunta87=pregunta87,
            Pregunta88=pregunta88,
            Pregunta89=pregunta89,
            Pregunta90=pregunta90,
            Pregunta91=pregunta91,              
            resultado_prediccion=resultado_prediccion
            )
        Intervencion.save()
        return redirect('inicio')
    else:
        return render(request,'Test.html')
        
    
def historial(request):    
    pacientes=paciente.objects.filter(user=request.user)
    paginator = Paginator(pacientes, 5)  # 5 pacientes por página
    page = request.GET.get('page')
    pacientes_list = paginator.get_page(page)
    mostrar_paginacion = pacientes_list.paginator.count > 5
    return render(request,'HistorialResultados.html',{'pacientes':pacientes, 'mostrar_paginacion': mostrar_paginacion})

def sesiones(request, paciente_id):
    paciente_obj = paciente.objects.get(pk=paciente_id)
    intervenciones = intervencion.objects.filter(paciente=paciente_obj)
    
    form = FiltroFechaForm(request.GET)
    
    if form.is_valid():
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_fin = form.cleaned_data.get('fecha_fin')
        
        if fecha_inicio and fecha_fin:
            fecha_fin = datetime.combine(fecha_fin, time(23, 59, 59))
            intervenciones = intervenciones.filter(fecha_int__range=(fecha_inicio, fecha_fin))
    
    return render(request, 'Sesiones.html', {'Paciente': paciente_obj, 'Intervenciones': intervenciones, 'form': form})

def intervencion_detail(request,paciente_id,intervencion_id):
     Paciente = get_object_or_404(paciente, pk=paciente_id)
     Intervencion = get_object_or_404(intervencion, pk=intervencion_id) 
     #Variables para TCA 
     variables_intervencion_DT = [Intervencion.Pregunta1, Intervencion.Pregunta7, Intervencion.Pregunta11, Intervencion.Pregunta16, Intervencion.Pregunta25, Intervencion.Pregunta32, Intervencion.Pregunta49]  
     variables_intervencion_B = [Intervencion.Pregunta4, Intervencion.Pregunta5, Intervencion.Pregunta28, Intervencion.Pregunta38, Intervencion.Pregunta46, Intervencion.Pregunta53, Intervencion.Pregunta61, Intervencion.Pregunta64]
     variables_intervencion_BD = [Intervencion.Pregunta2, Intervencion.Pregunta9, Intervencion.Pregunta12, Intervencion.Pregunta19, Intervencion.Pregunta31, Intervencion.Pregunta45, Intervencion.Pregunta47, Intervencion.Pregunta55, Intervencion.Pregunta59, Intervencion.Pregunta62]  
    #Variables para resto de sumas
     variables_intervencion_LSE = [Intervencion.Pregunta10, Intervencion.Pregunta27, Intervencion.Pregunta41, Intervencion.Pregunta42, Intervencion.Pregunta50, Intervencion.Pregunta37]
     variables_intervencion_PA = [Intervencion.Pregunta18, Intervencion.Pregunta21, Intervencion.Pregunta24, Intervencion.Pregunta56, Intervencion.Pregunta80, Intervencion.Pregunta84, Intervencion.Pregunta91]
     variables_intervencion_II = [Intervencion.Pregunta15, Intervencion.Pregunta23, Intervencion.Pregunta34, Intervencion.Pregunta57, Intervencion.Pregunta69, Intervencion.Pregunta73, Intervencion.Pregunta87]
     variables_intervencion_IA = [Intervencion.Pregunta30, Intervencion.Pregunta54, Intervencion.Pregunta65, Intervencion.Pregunta74, Intervencion.Pregunta17]
     variables_intervencion_ID = [Intervencion.Pregunta8, Intervencion.Pregunta21, Intervencion.Pregunta26, Intervencion.Pregunta33, Intervencion.Pregunta40, Intervencion.Pregunta44, Intervencion.Pregunta51, Intervencion.Pregunta60, Intervencion.Pregunta77]
     variables_intervencion_ED = [Intervencion.Pregunta67, Intervencion.Pregunta70, Intervencion.Pregunta73, Intervencion.Pregunta79, Intervencion.Pregunta81, Intervencion.Pregunta83, Intervencion.Pregunta85, Intervencion.Pregunta90] 
     variables_intervencion_P = [Intervencion.Pregunta13, Intervencion.Pregunta29, Intervencion.Pregunta36, Intervencion.Pregunta43, Intervencion.Pregunta52, Intervencion.Pregunta63] 
     variables_intervencion_A = [Intervencion.Pregunta66, Intervencion.Pregunta68, Intervencion.Pregunta75, Intervencion.Pregunta78, Intervencion.Pregunta82, Intervencion.Pregunta86, Intervencion.Pregunta88] 
     variables_intervencion_MF = [Intervencion.Pregunta3, Intervencion.Pregunta6, Intervencion.Pregunta14, Intervencion.Pregunta22, Intervencion.Pregunta35, Intervencion.Pregunta39, Intervencion.Pregunta48, Intervencion.Pregunta58] 
    # Calcula la suma de las variables de intervención
     DT = sum(variables_intervencion_DT) 
     B= sum(variables_intervencion_B) 
     BD= sum(variables_intervencion_BD) 
     LSE= sum(variables_intervencion_LSE) 
     PA= sum(variables_intervencion_PA) 
     II= sum(variables_intervencion_II) 
     IA= sum(variables_intervencion_IA) 
     ID= sum(variables_intervencion_ID) 
     ED= sum(variables_intervencion_ED) 
     P= sum(variables_intervencion_P) 
     A= sum(variables_intervencion_A) 
     MF= sum(variables_intervencion_MF) 
     #Cálculo de TCA
     variables_intervencion_EDR=[DT,B,BD]
     EDR= sum(variables_intervencion_EDR) 
     #Cálculo de subtotales
     variables_intervencion_IC=[LSE,PA]
     IC= sum(variables_intervencion_IC) 
     
     variables_intervencion_IPC=[II,IA]
     IPC= sum(variables_intervencion_IPC) 

     variables_intervencion_APC=[ID,ED]
     APC= sum(variables_intervencion_APC) 

     variables_intervencion_OC=[P,A]
     OC= sum(variables_intervencion_OC) 

     variables_intervencion_GPMC=[LSE,PA,II,IA,ID,ED,P,A,MF]
     GPMC= sum(variables_intervencion_GPMC) 
    
     return render(request, 'intervencion_detail.html', {'Paciente': Paciente, 'Intervencion': Intervencion, 
                                                         'DT': DT, 'B': B, 'BD': BD,'EDR':EDR,
                                                         'LSE':LSE,'PA':PA,'II':II,'IA':IA,'ID':ID,
                                                         'ED':ED,'P':P,'A':A,'MF':MF,'IC':IC,'IPC':IPC,'APC':APC
                                                         ,'OC':OC,'GPMC':GPMC})