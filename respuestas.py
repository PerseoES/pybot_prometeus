 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from datetime import datetime


def resp_simples(mensaje):
    user_msg = str(mensaje).lower()

    if user_msg in ("hello", "hola", "hi", "buenas"):
        return "Hola! ¿Cómo estás?"
    
    if user_msg in ("how are you", "cómo estás?", "como estas?", "como estas"):
        return "Estoy súper bien =D"
    
    if user_msg in ("who are you", "who are you?", "quién sos?", "quién eres?", "quien eres?", "quien eres", "quien sos", "quién sos?"):
        return "Soy Lemillion Bot, programado por mi dueño @Sebastian_PS. Es un gusto hablar contigo, espero pueda sacarte una sonrisa :)."
    
    if user_msg in ("time", "time?", "hora", "hora?", "qué hora es?", "dime la hora", "me puedes decir la hora?"):
        
        ahora = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return (f"La hora es {str(date_time)}")
    else:
        return "No pude entender lo que me quisiste decir, por favor, reingresa otra palabra."