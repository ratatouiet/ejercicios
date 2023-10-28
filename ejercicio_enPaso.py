from cmu_graphics import *

def onMouseMove(x, y):
    

    app.fondo = 'negro'

Rótulo('*No a escala', 340, 370, relleno='blanco', tamaño=16)

cometa=Grupo(
    Linea(40,40,120,80,relleno=gradiente('gris','humoBlanco')),
    Linea(200,20,290,80,relleno=gradiente('gris','humoBlanco'))
)
sol = estrella(200, 200, 35, 400, relleno=gradiente('naranja', 'amarillo', 'rojoNaranja'))
jupiter=Grupo(
    Circulo(200,200,200,relleno=None,borde='grisOscuro')
)


tierra = Grupo(
    Círculo(200, 200, 150, relleno=None, borde='grisOscuro'),
    Círculo(200, 50, 10, relleno=gradiente('verde', 'azulReal', inicio='izquierda-superior'))
    )
jupiter.dirección='sentido-horario'
tierra.dirección = 'sentido-horario'

def enTeclaPresionada(tecla):
    # Cambie la dirección basado en la tecla.
    if (tecla == 'derecha'):
        tierra.dirección = 'sentido-horario'
    elif (tecla == 'izquierda'):
        tierra.dirección = 'sentido-antihorario'

def enPaso():
    # Si la dirección de la tierra es en sentido horario, agregue 3 al rotarÁngulo.
    # Si no, reste 3.
    if (tierra.dirección == 'sentido-horario'):
        tierra.rotarÁngulo += 3
    else:
        tierra.rotarÁngulo -= 3

    # Incremente el número de puntos del sol por 1.
    sol.puntos += 1

cmu_graphics.run()