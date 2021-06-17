def response(input_message):
    message = input_message.lower()

    if message == "Tudo bem?":
        return 'Tudo bem graças a Deus'
    elif message == 'Oii':
        return "Oii, tudo bem?"
    else:
        return "Não posso responder no momento!"