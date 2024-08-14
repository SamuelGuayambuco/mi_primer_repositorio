while True:
    meme_dict = {
                "CRINGE": "Algo excepcionalmente raro o embarazoso",
                "LOL": "Una respuesta común a algo gracioso",
                "XD":"Es cuando sucede algo gracioso",
                "ROFL":"Una respuesta a una broma",
                "SHEESH":"Ligera desaprobación",
                "CREEPY":"Aterrador, siniestro",
                "AGGRO": "Ponerse agresivo/enojado",
                }
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print(meme_dict[word])
    else:
        # ¿Qué hacer si no se encuentra la palabra?
        print("no tenemos esta palabra")
