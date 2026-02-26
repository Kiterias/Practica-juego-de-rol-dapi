class Personaje:
    def __init__(self,nombre,vida,ataque,defensa):
        self.nombre=nombre
        self.vida=vida
        self.ataquebase=ataque
        self.defensa=defensa
    def atacar(self,objetivo):
        print(self.nombre+" ataca a "+objetivo.nombre)
        objetivo.defenderse(self.ataquebase)
    def ataqueespecial(self,objetivo):
        print(self.nombre+" usa ataqueespecial")
        objetivo.defenderse(self.ataquebase*2)
    def defenderse(self,daño):
        dañofinal=daño-self.defensa
        if dañofinal<0:
            dañofinal=0
        self.restarvida(dañofinal)
    def restarvida(self,cantidad):
        self.vida-=cantidad
        if self.vida<0:
            self.vida=0
        print(self.nombre+" recibio "+str(cantidad)+" de daño")
    def curacion(self,cantidad):
        self.vida+=cantidad
        print(self.nombre+" se curo "+str(cantidad))
    def mostrarvida(self):
        print("Vida de "+self.nombre+": "+str(self.vida))
    def esvivo(self):
        return self.vida>0
class Guerrero(Personaje):
    def __init__(self,nombre,vida,ataque,defensa,fuerza,resistencia):
        super().__init__(nombre,vida,ataque,defensa)
        self.fuerza=fuerza
        self.resistencia=resistencia
    def ataqueespecial(self,objetivo):
        print(self.nombre+" usa golpefuerte")
        daño=self.ataquebase+self.fuerza
        objetivo.defenderse(daño)
class Arquero(Personaje):
    def __init__(self,nombre,vida,ataque,defensa,punteria,agilidad):
        super().__init__(nombre,vida,ataque,defensa)
        self.punteria=punteria
        self.agilidad=agilidad
    def ataqueespecial(self,objetivo):
        print(self.nombre+" usa flechaprecisa")
        daño=self.ataquebase+self.punteria
        objetivo.defenderse(daño)
class Mago(Personaje):
    def __init__(self,nombre,vida,ataque,defensa,magia,mana):
        super().__init__(nombre,vida,ataque,defensa)
        self.magia=magia
        self.mana=mana
    def ataqueespecial(self,objetivo):
        if self.mana>=5:
            print(self.nombre+" lanza hechizo")
            daño=self.ataquebase+self.magia
            self.mana-=5
            objetivo.defenderse(daño)
        else:
            print(self.nombre+" sin mana")
print("Elige clase")
print("1 Guerrero")
print("2 Arquero")
print("3 Mago")
opcion=int(input("Opcion: "))
nombre=input("Nombre: ")
if opcion==1:
    jugador=Guerrero(nombre,120,20,8,15,10)
elif opcion==2:
    jugador=Arquero(nombre,90,18,5,20,15)
elif opcion==3:
    jugador=Mago(nombre,80,15,4,25,30)
else:
    exit()
enemigo=Personaje("Enemigo",100,12,3)
ultespecial=False
jugador.atacar(enemigo)
enemigo.atacar(jugador)
while jugador.esvivo() and enemigo.esvivo():
    print("1 atacar")
    print("2 ataqueespecial")
    print("3 curar")
    print("4 huir")
    eleccion=int(input("Opcion: "))
    accion=True
    if eleccion==1:
        jugador.atacar(enemigo)
        ultespecial=False
    elif eleccion==2:
        if ultespecial:
            print("No puedes usar ataqueespecial dos veces seguidas")
            accion=False
        else:
            jugador.ataqueespecial(enemigo)
            ultespecial=True
    elif eleccion==3:
        jugador.curacion(10)
        ultespecial=False
    elif eleccion==4:
        print("Has huido")
        break
    else:
        accion=False
    if accion and enemigo.esvivo():
        enemigo.atacar(jugador)
    jugador.mostrarvida()
    enemigo.mostrarvida()
if not enemigo.esvivo():
    print("Has ganado")
if not jugador.esvivo():
    print("Has perdido")