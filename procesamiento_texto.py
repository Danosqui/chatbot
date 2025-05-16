import unicodedata
import re

# Lista básica de palabras vacías en español
STOPWORDS = {
    "que", "es", "una", "un", "el", "la", "los", "las", "para", "de", "en", "y", "a", "por", "con",
    "al", "del", "se", "lo", "su", "sus", "o", "u", "como", "este", "esta", "estos", "estas", "tambien", "pero",
    "más", "menos", "muy", "ya", "le", "les", "me", "te", "nos", "vos", "ellos", "ellas", "eso", "esa", "aquel",
    "aquella", "aqui", "alli", "allí", "entonces", "porque", "aunque", "donde", "cuando", "quien", "cual"
}

# Diccionario de lematización artesanal
LEMAS_ARTESANALES = {
    # Verbos comunes (ser, estar, tener, hacer, poder, ir, decir, etc.)
    "fui": "ser", "fuiste": "ser", "fue": "ser", "fuimos": "ser", "fueron": "ser",
    "soy": "ser", "eres": "ser", "somos": "ser", "son": "ser",
    "era": "ser", "eras": "ser", "eran": "ser",

    "estoy": "estar", "estas": "estar", "esta": "estar", "estamos": "estar", "estan": "estar",
    "estuve": "estar", "estuviste": "estar", "estuvo": "estar", "estuvimos": "estar", "estuvieron": "estar",

    "tengo": "tener", "tienes": "tener", "tiene": "tener", "tenemos": "tener", "tienen": "tener",
    "tuve": "tener", "tuviste": "tener", "tuvo": "tener", "tuvimos": "tener", "tuvieron": "tener",

    "puedo": "poder", "puedes": "poder", "puede": "poder", "podemos": "poder", "pueden": "poder",
    "pude": "poder", "pudiste": "poder", "pudo": "poder", "pudimos": "poder", "pudieron": "poder",

    "hago": "hacer", "haces": "hacer", "hace": "hacer", "hacemos": "hacer", "hacen": "hacer",
    "hice": "hacer", "hiciste": "hacer", "hizo": "hacer", "hicimos": "hacer", "hicieron": "hacer",

    "voy": "ir", "vas": "ir", "va": "ir", "vamos": "ir", "van": "ir",
    "fui": "ir", "fuiste": "ir", "fue": "ir", "fuimos": "ir", "fueron": "ir",

    "digo": "decir", "dices": "decir", "dice": "decir", "decimos": "decir", "dicen": "decir",
    "dije": "decir", "dijiste": "decir", "dijo": "decir", "dijimos": "decir", "dijeron": "decir",

    "comiendo": "comer", "comi": "comer", "comio": "comer", "como": "comer",
    "jugando": "jugar", "juego": "jugar", "juegas": "jugar", "jugamos": "jugar",

    # Nombres comunes
    "pokemones": "pokemon", "pokemons": "pokemon", "personajes": "personaje", "criaturas": "criatura"
}


def lematizar_artesanal(tokens):
    return [LEMAS_ARTESANALES.get(token, token) for token in tokens]


def preprocesar_texto(texto):
    # 1. Eliminar acentos y convertir a minúsculas
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8').lower()

    # 2. Eliminar signos de puntuación
    texto = re.sub(r'[^\w\s]', '', texto)

    # 3. Tokenizar
    tokens = texto.split()

    # 4. Eliminar palabras vacías
    tokens = [palabra for palabra in tokens if palabra not in STOPWORDS]

    # 5. Aplicar lematización artesanal
    tokens = lematizar_artesanal(tokens)

    return ' '.join(tokens)
