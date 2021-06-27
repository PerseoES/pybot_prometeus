 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from datetime import datetime


def resp_simples(mensaje):
    user_msg = str(mensaje).lower()

    if user_msg in ("hello", "hola", "hi", "buenas"):
        return "Hola! ¿Cómo estás?"
    
    if user_msg in ("how are you", "cómo estás?", "como estas?", "como estas", "cómo estás"):
        return "Estoy súper bien =D"
    
    if user_msg in ("who are you", "who are you?", "quién sos?", "quién eres?", "quien eres?", "quien eres", "quien sos", "quién sos?"):
        return "Soy Lemillion Bot, programado por mi dueño @Sebastian_PS. Es un gusto hablar contigo, espero pueda sacarte una sonrisa :)."
    
    if user_msg in ("time", "time?", "hora", "hora?", "qué hora es?", "dime la hora", "me puedes decir la hora?"):
        ahora = datetime.now()
        date_time = ahora.strftime("%d/%m/%y, %H:%M:%S")
        return (f"{La hora es: str(date_time)}")
    
    if user_msg in ("quién es cande", "quién es candela", "quién es cande?", "quién es candela?")
        return "Cande es una persona increíble, tendrías que conocerla si no lo has hecho aún. :D"
    
    if user_msg in ("quién es juan", "quién es juani", "quién es juani?", "quién es juan?")
        return "Juani es una personita increíble en este mundo, siempre te querrá ver feliz, espero tengas la oportunidad de cruzarte con él porque créeme que jamás te arrepentirás =)."
        
    else:
        return "No pude entender lo que me quisiste decir, por favor, dime otra palabra."