def ejercicio4():
    """
    Ejercicio No 4:
    “A la mamá de Juan le preguntan su edad, y contesta: tengo 3 hijos, pregúntele a Juan su edad.
    Alberto tiene 2/3 de la edad de Juan, Ana tiene 4/3 de la edad de Juan y mi edad es la suma de las tres.
    Hacer un algoritmo que muestre la edad de los cuatro.”
    """
    try:
        # Se pide la edad de Juan
        edad_juan = float(input("Ingrese la edad de Juan: "))
        edad_alberto = (2/3) * edad_juan
        edad_ana = (4/3) * edad_juan
        edad_mama = edad_juan + edad_alberto + edad_ana  # equivalently 3 * edad_juan
        
        print("\n--- Resultados ---")
        print(f"Edad de Juan: {edad_juan:.2f}")
        print(f"Edad de Alberto: {edad_alberto:.2f}")
        print(f"Edad de Ana: {edad_ana:.2f}")
        print(f"Edad de la mamá: {edad_mama:.2f}")
    except Exception as e:
        print("Error en la entrada:", e)


def ejercicio9():
    """
    Ejercicio No 9:
    Se calcula X de acuerdo con:
      X = 0 si Y < A y (A < B < C)
      X = 1 si A <= Y < B
      X = 2 si B <= Y < C
      X = 3 si C <= Y
      X = 4 si no se cumple ninguna de las condiciones anteriores.
    """
    try:
        y = float(input("Ingrese el valor de Y: "))
        a = float(input("Ingrese el valor de A: "))
        b = float(input("Ingrese el valor de B: "))
        c = float(input("Ingrese el valor de C: "))
        
        if y < a and a < b and b < c:
            x = 0
        elif a <= y < b:
            x = 1
        elif b <= y < c:
            x = 2
        elif c <= y:
            x = 3
        else:
            x = 4
        
        print(f"\nEl valor de X es: {x}")
    except Exception as e:
        print("Error en la entrada:", e)


def ejercicio10():
    """
    Ejercicio No 10:
    Se requiere liquidar la matrícula de un estudiante a partir de:
      - Número de inscripción
      - Nombres
      - Patrimonio
      - Estrato social
    La cuota base es de $50,000, pero si el patrimonio es mayor a $2,000,000 y el estrato es superior a 3,
    se le suma un 3% del patrimonio.
    """
    try:
        inscripcion = input("Ingrese el número de inscripción: ")
        nombres = input("Ingrese los nombres del estudiante: ")
        patrimonio = float(input("Ingrese el patrimonio: "))
        estrato = int(input("Ingrese el estrato social: "))
        
        matricula_base = 50000
        if patrimonio > 2000000 and estrato > 3:
            incremento = 0.03 * patrimonio
        else:
            incremento = 0
        pago_matricula = matricula_base + incremento
        
        print("\n--- Datos del Estudiante ---")
        print(f"Número de inscripción: {inscripcion}")
        print(f"Nombres: {nombres}")
        print(f"Pago de matrícula: ${pago_matricula:,.2f}")
    except Exception as e:
        print("Error en la entrada:", e)


def ejercicio11():
    """
    Ejercicio Resuelto No 11:
    Solicitar tres números enteros diferentes y mostrar el mayor.
    """
    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        num3 = int(input("Ingrese el tercer número entero: "))
        
        mayor = max(num1, num2, num3)
        print(f"\nEl mayor de los tres números es: {mayor}")
    except Exception as e:
        print("Error en la entrada:", e)


def ejercicio12():
    """
    Ejercicio Resuelto No 12:
    Calcular el salario semanal de un trabajador, teniendo en cuenta que las horas
    laborales hasta 40 se pagan a tarifa normal; las horas extras, si son hasta 8, se pagan al doble,
    y si superan las 8, las primeras 8 se pagan al doble y el resto al triple.
    """
    try:
        nombre = input("Ingrese el nombre del trabajador: ")
        horas_trabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))
        valor_hora = float(input("Ingrese el valor de una hora normal de trabajo: "))
        
        if horas_trabajadas <= 40:
            salario = horas_trabajadas * valor_hora
        else:
            salario_normal = 40 * valor_hora
            horas_extra = horas_trabajadas - 40
            if horas_extra <= 8:
                salario_extra = horas_extra * (2 * valor_hora)
            else:
                salario_extra = 8 * (2 * valor_hora) + (horas_extra - 8) * (3 * valor_hora)
            salario = salario_normal + salario_extra
        
        print(f"\nTrabajador: {nombre}")
        print(f"Salario semanal: ${salario:,.2f}")
    except Exception as e:
        print("Error en la entrada:", e)


def ejercicio14():
    """
    Ejercicio Resuelto No 14:
    Dado el importe global de las ventas de tres departamentos y un salario base (igual para todos),
    a cada departamento que supere el 33% de las ventas totales se le suma un 20% extra al salario.
    Se debe determinar el salario final para los vendedores de cada departamento.
    """
    try:
        venta1 = float(input("Ingrese las ventas del departamento 1: "))
        venta2 = float(input("Ingrese las ventas del departamento 2: "))
        venta3 = float(input("Ingrese las ventas del departamento 3: "))
        SALAR = float(input("Ingrese el salario mensual de los vendedores: "))
        
        TOTVEN = venta1 + venta2 + venta3
        PORVEN = 0.33 * TOTVEN

        if venta1> PORVEN:
            SALAR1 = SALAR + 0.20 * SALAR
        else:
            SALAR1 = SALAR

        if venta2 > PORVEN:
            SALAR2 = SALAR + 0.20 * SALAR
        else:
            SALAR2 = SALAR

        if venta3 > PORVEN:
            SALAR3 = SALAR + 0.20 * SALAR
        else:
            SALAR3 = SALAR

        print("\n--- Salarios Finales por Departamento ---")
        print(f"Departamento 1 - Ventas: {venta1}, Salario final: ${SALAR1:,.2f}")
        print(f"Departamento 2 - Ventas: {venta2}, Salario final: ${SALAR2:,.2f}")
        print(f"Departamento 3 - Ventas: {venta3}, Salario final: ${SALAR3:,.2f}")
    except Exception as e:
        print("Error en la entrada:", e)


def ejercicio15():
    """
    Ejercicio Resuelto No 15:
    Se tienen cuatro esferas (A, B, C, D) de las cuales tres tienen el mismo peso y una es diferente.
    El algoritmo determina cuál esfera es la diferente y si es de mayor o menor peso.
    """
    try:
        pesoa = float(input("Ingrese el peso de la esfera A: "))
        pesob = float(input("Ingrese el peso de la esfera B: "))
        pesoc = float(input("Ingrese el peso de la esfera C: "))
        pesod = float(input("Ingrese el peso de la esfera D: "))
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        return

    if pesoa == pesob and pesoa == pesoc:
        if pesod > pesoa:
            print("LA ESFERA D ES LA DIFERENTE Y ES DE MAYOR PESO")
        else:
            print("LA ESFERA D ES LA DIFERENTE Y ES DE MENOR PESO")
    

    elif pesoa == pesob and pesoa == pesod:
        if pesoc > pesoa:
            print("LA ESFERA C ES LA DIFERENTE Y ES DE MAYOR PESO")
        else:
            print("LA ESFERA C ES LA DIFERENTE Y ES DE MENOR PESO")
    

    elif pesoa == pesoc and pesoa == pesod:
        if pesob > pesoa:  
            print("LA ESFERA B ES LA DIFERENTE Y ES DE MAYOR PESO")
        else:
            print("LA ESFERA B ES LA DIFERENTE Y ES DE MENOR PESO")
    
    else:
        if pesoa > pesob:
            print("LA ESFERA A ES LA DIFERENTE Y ES DE MAYOR PESO")
        else:
            print("LA ESFERA A ES LA DIFERENTE Y ES DE MENOR PESO")


def ejercicio22():
    """
    Ejercicio Propuesto No 22:
    Se introduce el nombre de un empleado, su salario básico por hora y el número de horas trabajadas
    en el mes. Se debe mostrar el nombre y el salario mensual si éste es mayor a $450,000; de lo contrario,
    sólo se muestra el nombre.
    """
    try:
        nombre = input("Ingrese el nombre del empleado: ")
        salario_hora = float(input("Ingrese el salario básico por hora: "))
        horas_mes = float(input("Ingrese el número de horas trabajadas en el mes: "))
        salario_mensual = salario_hora * horas_mes
        
        print("\n--- Datos del Empleado ---")
        if salario_mensual > 450000:
            print(f"Empleado: {nombre} - Salario mensual: ${salario_mensual:,.2f}")
        else:
            print(f"Empleado: {nombre}")
    except Exception as e:
        print("Error en la entrada:", e)


def ejercicio32():
    """
    Ejercicio Propuesto No 32:
    Un almacén de escritorios ofrece descuentos según la cantidad:
      - Menos de 5 unidades: 10%
      - De 5 a 9 unidades: 20%
      - 10 o más unidades: 40%
    Se debe calcular el total a pagar si el valor de cada escritorio es de $800,000.
    """
    try:
        unidades = int(input("Ingrese el número de escritorios a comprar: "))
        precio_unitario = 800000
        total = unidades * precio_unitario
        
        if unidades < 5:
            descuento = 0.10
        elif 5 <= unidades < 10:
            descuento = 0.20
        else:  # 10 o más
            descuento = 0.40
        
        descuento_valor = total * descuento
        total_a_pagar = total - descuento_valor
        
        print("\n--- Cálculo de Descuento ---")
        print(f"Total sin descuento: ${total:,.2f}")
        print(f"Descuento aplicado: {descuento*100:.0f}% (equivalente a ${descuento_valor:,.2f})")
        print(f"Total a pagar: ${total_a_pagar:,.2f}")
    except Exception as e:
        print("Error en la entrada:", e)


def ejercicio33():
    """
    Ejercicio Propuesto No 33:
    Se implementa un juego de preguntas que se responde 'SI' o 'NO'. Gana el participante si responde
    correctamente las tres preguntas. Si se falla en alguna, se termina el juego.
    
    Preguntas:
      1. ¿Simón Bolívar libertó a Colombia? (Respuesta correcta: SI)
      2. ¿Camilo Torres fue un guerrillero? (Respuesta correcta: NO)
      3. ¿El Binomio de Oro es un grupo de música vallenata? (Respuesta correcta: SI)
    """
    try:
        print("\nJuego de Preguntas: Responde SI o NO")
        resp1 = input("1. ¿Simón Bolívar libertó a Colombia? ").strip().upper()
        if resp1 != "SI":
            print("Respuesta incorrecta. Fin del juego.")
            return
        
        resp2 = input("2. ¿Camilo Torres fue un guerrillero? ").strip().upper()
        if resp2 != "NO":
            print("Respuesta incorrecta. Fin del juego.")
            return
        
        resp3 = input("3. ¿El Binomio de Oro es un grupo de música vallenata? ").strip().upper()
        if resp3 != "SI":
            print("Respuesta incorrecta. Fin del juego.")
            return
        
        print("¡Ganaste! Respondiste correctamente todas las preguntas.")
    except Exception as e:
        print("Error en la entrada:", e)


def main():
    """
    Menú para ejecutar cada uno de los 10 ejercicios solicitados.
    """
    while True:
        print("\nSeleccione el ejercicio a ejecutar:")
        print("1. Ejercicio 4")
        print("2. Ejercicio 9")
        print("3. Ejercicio 10")
        print("4. Ejercicio 11")
        print("5. Ejercicio 12")
        print("6. Ejercicio 14")
        print("7. Ejercicio 15")
        print("8. Ejercicio Propuesto 22")
        print("9. Ejercicio Propuesto 32")
        print("10. Ejercicio Propuesto 33")
        print("0. Salir")
        
        opcion = input("Ingrese el número de ejercicio: ")
        
        if opcion == "1":
            ejercicio4()
        elif opcion == "2":
            ejercicio9()
        elif opcion == "3":
            ejercicio10()
        elif opcion == "4":
            ejercicio11()
        elif opcion == "5":
            ejercicio12()
        elif opcion == "6":
            ejercicio14()
        elif opcion == "7":
            ejercicio15()
        elif opcion == "8":
            ejercicio22()
        elif opcion == "9":
            ejercicio32()
        elif opcion == "10":
            ejercicio33()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
