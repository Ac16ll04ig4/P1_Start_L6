def ontcijfer(bericht, sleutel):
    ontcijferd_bericht = ""
    for charactar in bericht:
        if charactar in sleutel:
            ontcijferd_bericht = ontcijferd_bericht + charactar
    return ontcijferd_bericht
