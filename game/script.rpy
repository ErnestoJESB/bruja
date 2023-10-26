# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:


init:
    $ vida_bruja = 3  # La bruja comienza con 3 vidas
    $ vida_nino = 3   # El niño comienza con 3 vidas
    $ puntaje = 0     # Inicializa el puntaje del jugador
    $ imgFondo = "https://cdn.pixabay.com/photo/2023/09/21/18/17/automobile-8267369_1280.jpg"  # Imagen de fondo del juego


# El juego comienza aquí.

label start:
    "Eras un niño curioso que se encontró con una libreta encantada."
    "Al abrirla, fuiste absorbido por ella y ahora estás atrapado dentro."
    
    "Para escapar, debes responder correctamente 3 preguntas de ortografía."
    "Si fallas, te convertirás en un sapo."
    "Dentro de la libreta, te enfrentas a la temida Bruja de la Ortografía."
    
    $ pregunta_actual = 1
    jump juego
    

label juego:
    if vida_bruja <= 0:
        "¡Has vencido a la Bruja de la Ortografía y escapaste de la libreta!"
    elif vida_nino <= 0:
        "Fallaste en responder correctamente y te has convertido en un sapo. ¡Juego terminado!"
    else:
        "Te enfrentas a la Bruja de la Ortografía."
        "Ella tiene [vida_bruja] vidas restantes."
        
        "¿Cuál es la palabra correcta? 'Zanahoria' o 'Zanaoria'"
        menu:
            "Zanahoria":
                "¡Respuesta correcta! Le restas una vida a la bruja."
                $ vida_bruja -= 1
                $ puntaje += 10
                jump siguiente_pregunta
            "Zanaoria":
                "Respuesta incorrecta. La bruja te lanza un hechizo y te conviertes en un sapo."
                $ vida_nino -= 1
                jump juego
                
label siguiente_pregunta:
        $ pregunta_actual += 1
        if pregunta_actual > 3:
            jump juego  # El niño ha respondido correctamente 3 preguntas, gana el juego
        else:
            jump juego  # Continúa enfrentando a la bruja

label final:
    "Fin del juego. Tu puntaje final es [puntaje]."
    return
