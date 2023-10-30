from cmu_graphics import *

def onMouseMove(x, y):
    

    app.fondo = 'negro'

Rótulo('*No a escala', 340, 370, relleno='blanco', tamaño=16)

cometa=Grupo(
    Linea(40,60,120,20,relleno=gradiente('negro','humoBlanco',inicio='derecha')),
    Linea(360,40,280,80,relleno=gradiente('negro','humoBlanco',inicio='derecha')),
    Linea(260,293,180,325,relleno=gradiente('negro','humoBlanco',inicio='derecha'))
    )
sol = Estrella(200, 200, 35, 400, relleno=gradiente('naranja', 'amarillo', 'rojoNaranja'))
marte=Grupo(
    Circulo(200,200,180,relleno=None,borde='grisOscuro'),
    Circulo(200,20,10,relleno=gradiente('marron','tierra',inicio='superior'))
    )
venus=Grupo(
    Circulo(200,200,100,relleno=None,borde='grisOscuro'),
    Circulo(200,100,13,relleno=gradiente('marrónCuero','naranja',inicio='superior'))
    
    
)

tierra = Grupo(
    Círculo(200, 200, 140, relleno=None, borde='grisOscuro'),
    Círculo(200, 60, 15, relleno=gradiente('verde', 'azulReal', inicio='izquierda-superior'))
    )
marte.dirección='sentido-horario'
venus.dirección='sentido-horario'
tierra.dirección = 'sentido-horario'

def enTeclaPresionada(tecla):
    # Cambie la dirección basado en la tecla.
    if (tecla == 'derecha'):
        tierra.dirección = 'sentido-horario'
    elif (tecla == 'izquierda'):
        tierra.dirección = 'sentido-antihorario'
    if (tecla == 'derecha'):
        marte.dirección='sentido-horario'
    elif (tecla == 'izquierda'):
        marte.dirección='sentido-antihorario'
    if(tecla == 'derecha'):
        venus.dirección='sentido-horario'
    elif(tecla == 'izquierda'):
        venus.dirección='sentido-antihorario'
        
        
def enPaso():
    # Si la dirección de la tierra es en sentido horario, agregue 3 al rotarÁngulo.
    # Si no, reste 3.
    if (tierra.dirección == 'sentido-horario'):
        tierra.rotarÁngulo += 2
    else:
        tierra.rotarÁngulo -= 2
    
    if(marte.dirección == 'sentido-horario'):
        marte.rotarÁngulo += 3
    else:
       marte.rotarÁngulo -= 3   
    
    if (venus.dirección == 'sentido-horario'):
        venus.rotarÁngulo += 3
    else:
       venus.rotarÁngulo -= 3 
    
    # Incremente el número de puntos del sol por 1.
    sol.puntos += 1

cmu_graphics.run()