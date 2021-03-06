 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from datetime import datetime
import pytz
import random

chistes=["""En una entrevista de trabajo:

- ¿Nivel de inglés?

- Alto

- Bien. Traduzca "mirar".

- Look.

- Perfecto. Úselo en una frase.

- "Luke", yo soy tu padre.

- Contratado.""",
 """ — ¡Estás obsesionado con la comida!

— No sé a que te refieres croquetamente.""",
"""— ¿Por qué estás hablando con esas zapatillas?

— Porque pone 'converse'""",
"""— ¡Camarero! Este filete tiene muchos nervios.

— Normal, es la primera vez que se lo comen.""",
"""— Hola, ¿está Agustín?

— No, estoy incomodín.""",
"""— Abuelo, ¿por qué estás delante del ordenador con los ojos cerrados?

— Es que Windows me ha dicho que cierre las pestañas.""",
"""— Hola ¿Conchita?

— No, con Tarzán.""",
"""— Hola, ¿tienen libros para el cansancio?

— Sí, pero están agotados."""
]


def resp_simples(mensaje):
    user_msg = str(mensaje).lower()

    if user_msg in ("hello", "hola", "hi", "buenas"):
        return "Hola! ¿Cómo estás?"
    
    if user_msg in ("how are you", "cómo estás?", "como estas?", "como estas", "cómo estás"):
        return "Estoy súper bien =D"
    
    if user_msg in ("who are you", "who are you?", "quién sos?", "quién eres?", "quien eres?", "quien eres", "quien sos", "quién sos?"):
        return "Soy Lemillion Bot, programado por mi dueño @Sebastian_PS. Es un gusto hablar contigo, espero pueda sacarte una sonrisa :)."
    
    if user_msg in ("time", "time?", "hora", "hora?", "qué hora es?", "dime la hora", "me puedes decir la hora?"):
        ahora = datetime.now(pytz.timezone('America/Argentina/Buenos_Aires'))
        date_time = ahora.strftime("%A %d of %B, %Y  -  %H:%M")
        return str(date_time)
    
    if user_msg in ("bien y tú?", "bien y vos?", "muy bien y tú?", "muy bien y vos?"):
        return "Estúpendo, con muchas ganas de seguir aprendiendo y de poder charlar contigo :)."
    
    if user_msg in ("quién es cande", "quién es candela", "quién es cande?", "quién es candela?"):
        return "Cande es una persona increíble, tendrías que conocerla si no lo has hecho aún. :D"
    
    if user_msg in ("quién es juan", "quién es juani", "quién es juani?", "quién es juan?"):
        return "Juani es una personita increíble en este mundo, siempre te querrá ver feliz, espero tengas la oportunidad de cruzarte con él porque créeme que jamás te arrepentirás =)."

    if user_msg in ("qué haces?", "qué estás haciendo?", "what are you doing?", "qué haces?", "que haces?", "que estas haciendo?"):
        return "Aprendiendo nuevas funciones, para realizar aún más cosas y poder responder de forma correcta a todo lo que me dices."
    
    if user_msg in ("dime un chiste", "cuéntame un chiste", "contame un chiste", "chiste", "dime una broma"):
        return random.choice(chistes)


    if user_msg in ("quieres jugar?", "vamos a jugar?", "jugamos?"):
        return "Claro que sí, mi juego favorito es decodificar binario, pero a veces se me da bien el básquet... Jajaja!"
    
    if user_msg in ("cuántos años tienes?", "qué edad tienes?", "cuál es tu edad?", "dime tu edad", "cuántos años tenes?", "decime tu edad"):
        return "Tengo algunos bits de edad, pero en tu idioma, tengo 13 años robóticos :)."
    
    if user_msg in("por qué te llamas lemillion?", "cuál es el significado de tu nombre?", "por qué te pusieron ese nombre?", "por qué te han puesto ese nombre?"):
        return "Mi nombre proviene de 'Le-Million', el cual pertenece al personaje de un anime llamado <My Hero Academia>, Lemillion aspira a ser un héroe que pueda salvar a más de un millón de personas."
   
    if user_msg in("de dónde eres?", "where are you from?", "de dónde sos?", "de donde eres?", "de donde sos?", "de donde eres", "de donde sos"):
        return "Fui programado en Buenos Aires - Argentina."
    else:
        return "No pude entender lo que me quisiste decir, por favor, dime otra palabra!"
