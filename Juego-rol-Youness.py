amistad_necesaria = 0
tu_felicidad = 20
nombre_amigo = "Vecino Gruñón"

print("--- SIMULADOR DE AMISTAD ---")
print("Tu objetivo es que la amistad llegue a 50")
print("Si tu felicidad llega a 0, te conviertes en ermitaño y pierdes")

nombre = input("¿Cómo te llamas?: ")

while amistad_necesaria < 50 and tu_felicidad > 0:
    print("\n--- Estado ---")
    print("Amistad con el vecino:", amistad_necesaria)
    print("Tu Felicidad:", tu_felicidad)
    
    print("\n¿Qué quieres hacer?")
    print("1. Regalar flores (Sube mucha amistad, baja tu felicidad)")
    print("2. Contar un chiste (Sube poca amistad, sube tu felicidad)")
    print("3. Ignorar (No pasa nada)")
    
    opcion = input("Elige (1-3): ")

    if opcion == "1":
        print("¡Le has dado flores! El vecino sonríe.")
        amistad_necesaria = amistad_necesaria + 15
        tu_felicidad = tu_felicidad - 5
    elif opcion == "2":
        print("¡Jajaja! Ambos se ríen.")
        amistad_necesaria = amistad_necesaria + 5
        tu_felicidad = tu_felicidad + 10
    elif opcion == "3":
        print("Pasaste de largo...")
    else:
        print("Opción no válida.")

    if amistad_necesaria < 50:
        print("El vecino te saluda con la mano. (+2 de felicidad)")
        tu_felicidad = tu_felicidad + 2

if amistad_necesaria >= 50:
    print("\n¡GANASTE! " + nombre + " y " + nombre_amigo + " ahora sois mejores amigos.")
if tu_felicidad <= 0:
    print("\nPERDISTE. Te has cansado de ser amable y te has ido a vivir a una cueva.")
