import random

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.vida_max = vida
        self.ataque_base = ataque
        self.defensa = defensa

    def atacar(self, objetivo):
        daño = self.ataque_base

        # probabilidad de crítico
        if random.randint(1, 100) <= 20:
            daño *= 2
            print(self.nombre + " hace un ATAQUE CRÍTICO!")

        print(self.nombre + " ataca a " + objetivo.nombre)
        objetivo.defenderse(daño)

    def defenderse(self, daño):
        daño_final = daño - self.defensa
        if daño_final < 0:
            daño_final = 0
        self.restar_vida(daño_final)

    def restar_vida(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0
        print(self.nombre + " recibe " + str(cantidad) + " de daño")

    def curacion(self):
        curar = 15
        self.vida += curar
        if self.vida > self.vida_max:
            self.vida = self.vida_max
        print(self.nombre + " se cura " + str(curar) + " puntos")

    def mostrar_vida(self):
        print("Vida de " + self.nombre + ": " + str(self.vida) + "/" + str(self.vida_max))

    def es_vivo(self):
        return self.vida > 0


class Guerrero(Personaje):
    def __init__(self, nombre, vida, ataque, defensa, fuerza, resistencia):
        super().__init__(nombre, vida, ataque, defensa)
        self.fuerza = fuerza
        self.resistencia = resistencia

    def ataque_especial(self, objetivo):
        daño = self.ataque_base + self.fuerza
        print(self.nombre + " usa GOLPE PODEROSO")
        objetivo.defenderse(daño)

    def defenderse(self, daño):
        # bloqueo extra
        if random.randint(1, 100) <= 30:
            print(self.nombre + " bloquea parte del daño")
            daño -= self.resistencia
        super().defenderse(daño)


class Arquero(Personaje):
    def __init__(self, nombre, vida, ataque, defensa, punteria, agilidad):
        super().__init__(nombre, vida, ataque, defensa)
        self.punteria = punteria
        self.agilidad = agilidad

    def ataque_especial(self, objetivo):
        daño = self.ataque_base + self.punteria
        print(self.nombre + " dispara FLECHA PRECISA")
        objetivo.defenderse(daño)

    def defenderse(self, daño):
        # probabilidad de esquivar
        if random.randint(1, 100) <= self.agilidad:
            print(self.nombre + " esquiva el ataque!")
        else:
            super().defenderse(daño)


class Mago(Personaje):
    def __init__(self, nombre, vida, ataque, defensa, magia, mana):
        super().__init__(nombre, vida, ataque, defensa)
        self.magia = magia
        self.mana = mana

    def ataque_especial(self, objetivo):
        if self.mana >= 10:
            daño = self.ataque_base + self.magia
            print(self.nombre + " lanza una BOLA DE FUEGO")
            self.mana -= 10
            objetivo.defenderse(daño)
            print("Mana restante:", self.mana)
        else:
            print("No tienes suficiente mana")

# PROGRAMA PRINCIPAL

print("ELIGE TU PERSONAJE: ")
print("1. Guerrero")
print("2. Arquero")
print("3. Mago")

opcion = int(input("Opción: "))
nombre = input("Nombre del personaje: ")
if opcion == 1:
    jugador = Guerrero(nombre, 130, 20, 8, 15, 10)
elif opcion == 2:
    jugador = Arquero(nombre, 100, 18, 5, 15, 30)
elif opcion == 3:
    jugador = Mago(nombre, 90, 15, 4, 25, 40)
else:
    print("Opción no válida")
    exit()
enemigo = Personaje("Enemigo", 110, 12, 4)
print("\n¡Comienza el combate!\n")
while jugador.es_vivo() and enemigo.es_vivo():
    print("\n1. Atacar")
    print("2. Ataque especial")
    print("3. Curarse")
    print("4. Huir")
    eleccion = int(input("Elige acción: "))

    if eleccion == 1:
        jugador.atacar(enemigo)
    elif eleccion == 2:
        jugador.ataque_especial(enemigo)
    elif eleccion == 3:
        jugador.curacion()
    elif eleccion == 4:
        print("Has huido del combate")
        break
    else:
        print("Opción inválida")

    if enemigo.es_vivo():
        enemigo.atacar(jugador)
    print()
    jugador.mostrar_vida()
    enemigo.mostrar_vida()

if not enemigo.es_vivo():
    print("\n¡Has ganado!")

if not jugador.es_vivo():
    print("\nHas perdido...")