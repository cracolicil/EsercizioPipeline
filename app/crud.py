import logging

logger = logging.getLogger(__name__)

def count_characters(text):
    """Conta tutti i caratteri nella frase, spazi inclusi."""
    return len(text)
def count_characters_no_spaces(text):
    """Conta solo i caratteri, escludendo gli spazi."""
    return len(text.replace(" ", ""))
def count_each_type(text):
    """Restituisce un dizionario con il conteggio per tipo di carattere."""
    return {
        "totale": len(text),
        "lettere": sum(c.isalpha() for c in text),
        "numeri": sum(c.isdigit() for c in text),
        "spazi": text.count(" "),
        "punteggiatura": sum(not c.isalnum() and not c.isspace() for c in text)
    }