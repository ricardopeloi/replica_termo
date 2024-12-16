dict_caracteres_especiais = {
        "Á": "A",
        "Â": "A",
        "Ã": "A",
        "É": "E",
        "Ê": "E",
        "Í": "I",
        "Î": "I",
        "Ó": "O",
        "Ô": "O",
        "Õ": "O",
        "Ú": "U",
        "Û": "U",
        "Ç": "C",
    }

letra = "Ç"
print(dict_caracteres_especiais.get(letra, letra))
