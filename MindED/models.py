from django.db import models
from django.contrib.auth.models import User


class paciente(models.Model):
        GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]    
        N_Paciente= models.BigAutoField(primary_key=True)
        DNI=models.CharField(max_length=8)
        nombre=models.CharField(max_length=200)        
        edad=models.IntegerField()
        genero=models.CharField(max_length=1, choices=GENDER_CHOICES)
        user=models.ForeignKey(User,on_delete=models.CASCADE)        
        

        def __str__(self):
              return self.nombre + '-by' + self.user.username

class intervencion(models.Model):
    paciente=models.ForeignKey(paciente,on_delete=models.CASCADE)
    N_sesion=models.BigAutoField(primary_key=True)
    titulo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)  
    fecha_int=models.DateTimeField(auto_now_add=True)
    Pregunta1=models.IntegerField()
    Pregunta2=models.IntegerField() 
    Pregunta3=models.IntegerField()  
    Pregunta4=models.IntegerField() 
    Pregunta5=models.IntegerField()
    Pregunta6=models.IntegerField()
    Pregunta7=models.IntegerField() 
    Pregunta8=models.IntegerField()  
    Pregunta9=models.IntegerField() 
    Pregunta10=models.IntegerField()
    Pregunta11=models.IntegerField()
    Pregunta12=models.IntegerField() 
    Pregunta13=models.IntegerField()  
    Pregunta14=models.IntegerField() 
    Pregunta15=models.IntegerField()
    Pregunta16=models.IntegerField()
    Pregunta17=models.IntegerField() 
    Pregunta18=models.IntegerField()  
    Pregunta19=models.IntegerField() 
    Pregunta20=models.IntegerField()   
    Pregunta21=models.IntegerField()
    Pregunta22=models.IntegerField() 
    Pregunta23=models.IntegerField()  
    Pregunta24=models.IntegerField() 
    Pregunta25=models.IntegerField()
    Pregunta26=models.IntegerField()
    Pregunta27=models.IntegerField() 
    Pregunta28=models.IntegerField()  
    Pregunta29=models.IntegerField() 
    Pregunta30=models.IntegerField()
    Pregunta31=models.IntegerField()
    Pregunta32=models.IntegerField() 
    Pregunta33=models.IntegerField()  
    Pregunta34=models.IntegerField() 
    Pregunta35=models.IntegerField()
    Pregunta36=models.IntegerField()
    Pregunta37=models.IntegerField() 
    Pregunta38=models.IntegerField()  
    Pregunta39=models.IntegerField() 
    Pregunta40=models.IntegerField()
    Pregunta41=models.IntegerField()
    Pregunta42=models.IntegerField() 
    Pregunta43=models.IntegerField()  
    Pregunta44=models.IntegerField() 
    Pregunta45=models.IntegerField()
    Pregunta46=models.IntegerField()
    Pregunta47=models.IntegerField() 
    Pregunta48=models.IntegerField()  
    Pregunta49=models.IntegerField() 
    Pregunta50=models.IntegerField() 
    Pregunta51=models.IntegerField()
    Pregunta52=models.IntegerField() 
    Pregunta53=models.IntegerField()  
    Pregunta54=models.IntegerField() 
    Pregunta55=models.IntegerField()
    Pregunta56=models.IntegerField()
    Pregunta57=models.IntegerField() 
    Pregunta58=models.IntegerField()  
    Pregunta59=models.IntegerField() 
    Pregunta60=models.IntegerField()
    Pregunta61=models.IntegerField()
    Pregunta62=models.IntegerField() 
    Pregunta63=models.IntegerField()  
    Pregunta64=models.IntegerField() 
    Pregunta65=models.IntegerField()
    Pregunta66=models.IntegerField()
    Pregunta67=models.IntegerField() 
    Pregunta68=models.IntegerField()  
    Pregunta69=models.IntegerField() 
    Pregunta70=models.IntegerField() 
    Pregunta71=models.IntegerField()
    Pregunta72=models.IntegerField() 
    Pregunta73=models.IntegerField()  
    Pregunta74=models.IntegerField() 
    Pregunta75=models.IntegerField()
    Pregunta76=models.IntegerField()
    Pregunta77=models.IntegerField() 
    Pregunta78=models.IntegerField()  
    Pregunta79=models.IntegerField() 
    Pregunta80=models.IntegerField() 
    Pregunta81=models.IntegerField()
    Pregunta82=models.IntegerField() 
    Pregunta83=models.IntegerField()  
    Pregunta84=models.IntegerField() 
    Pregunta85=models.IntegerField()
    Pregunta86=models.IntegerField()
    Pregunta87=models.IntegerField() 
    Pregunta88=models.IntegerField()  
    Pregunta89=models.IntegerField() 
    Pregunta90=models.IntegerField() 
    Pregunta91=models.IntegerField()
    resultado_prediccion = models.FloatField(null=True, blank=True)

    def __str__(self):
              return self.titulo + '-by' + self.paciente.nombre
