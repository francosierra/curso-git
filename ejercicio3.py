año = int(input("Ingrese su edad: "))
salario = float(input("Ingrese sus ingresos mensuales: "))

if año > 16 and salario >= 1000:
    print("Debe pagar impuestos")
else:
    print("No debes pagar Impuestos")