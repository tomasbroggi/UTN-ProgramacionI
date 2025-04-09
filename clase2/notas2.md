*>case _: -> es un else en match.
    En Python, dentro de una estructura match, el case _: funciona como un "default", es decir, una cláusula que coincide con cualquier valor que no haya coincidido antes. El guion bajo _ se usa como comodín y significa “no me importa el valor”.

    def evaluar(x):
        match x:
            case 1:
                print("Es uno")
            case 2:
                print("Es dos")
            case _:
                print("No es ni uno ni dos")

*>WHILE
    🌀 while <condición>:
    Se usa cuando sabés una condición lógica que determina cuándo continuar o frenar el bucle.
    🔁 while True:
    Se usa cuando querés un bucle infinito (algo que no tiene una condición clara al principio), y vas a romper el bucle desde adentro con break.

    ¿Cuándo usar cada uno?
    Situación	                            Usá
    Sabés la condición desde el principio	while <condición>
    Querés repetir "hasta que algo pase"	while True + break

    