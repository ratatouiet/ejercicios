from cmu_graphics import *

Rect(0,0,400,400,relleno=gradiente('blanco','gris'))
Rotulo('GRAFICA DE LAS POBLACIONES',200,40,tamaño=20)
#RELIONES
cristianismo=2300
islam=1900
hinduismo=1200
budismo=520
religionesTradicionalesChina=394
religionesAfroamericanas=100
personasNoReligiosas=1200

sumaDeReligiones=cristianismo+islam+hinduismo+budismo+religionesTradicionalesChina+religionesAfroamericanas+personasNoReligiosas

print(sumaDeReligiones)
porcentaje1=(cristianismo/sumaDeReligiones)
porcentaje2=(islam/sumaDeReligiones)
porcentaje3=(hinduismo/sumaDeReligiones)
porcentaje4=(budismo/sumaDeReligiones)
porcentaje5=(religionesTradicionalesChina/sumaDeReligiones)
porcentaje6=(religionesAfroamericanas/sumaDeReligiones)
porcentaje7=(personasNoReligiosas/sumaDeReligiones)

anguloDeBarrido1=int(porcentaje1*360)
anguloDeBarrido2=int(porcentaje2*360)
anguloDeBarrido3=int(porcentaje3*360)
anguloDeBarrido4=int(porcentaje4*360)
anguloDeBarrido5=int(porcentaje5*360)
anguloDeBarrido6=int(porcentaje6*360)
anguloDeBarrido7=int(porcentaje7*360)

print(porcentaje1)
print(porcentaje2)
print(porcentaje3)
print(porcentaje4)
print(porcentaje5)
print(porcentaje6)
print(porcentaje7)

print(anguloDeBarrido1)
print(anguloDeBarrido2)
print(anguloDeBarrido3)
print(anguloDeBarrido4)
print(anguloDeBarrido5)
print(anguloDeBarrido6)
print(anguloDeBarrido7)

grafica=Grupo(
    Circulo(200,200,120),
    Arco(200,200,240,240,0,anguloDeBarrido1,relleno='carmesi'),
    Arco(200,200,240,240,108,anguloDeBarrido2,relleno='indigo'),
    Arco(200,200,240,240,197,anguloDeBarrido3,relleno='azulCieloProfundo'),
    Arco(200,200,240,240,253,anguloDeBarrido4,relleno='verdePalido'),
    Arco(200,200,240,240,277,anguloDeBarrido5,relleno='naranjaOscuro'),
    Arco(200,200,240,240,295,anguloDeBarrido6+4,relleno='oro'),
    Arco(200,200,240,240,300,anguloDeBarrido7+4,relleno='marronCuero')
    
    
)

cmu_graphics.run()