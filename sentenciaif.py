kilometraje = int(input("ingrese su kilometraje: "))

if kilometraje == 1000:
    print("su auto esta usado")
elif kilometraje <= 20000:
    print("toca cambio de aceite")
elif kilometraje <=30000:
    print("a cambiar pastillas de freno")
elif kilometraje <=40000:
    print("cambia el auto")
else:
    print("no sirve mas")
