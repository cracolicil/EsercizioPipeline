import logging

logger = logging.getLogger(__name__)

def count_characters(text):
    logger.info("Counting all characters, spaces included")
    return len(text)
def count_characters_no_spaces(text):
    logger.info("counting all characters, spaces excluded")
    return len(text.replace(" ", ""))
def count_each_type(text):
    logger.info("Counting each character type")
    return {
        "total": len(text),
        "letters": sum(c.isalpha() for c in text),
        "numbers": sum(c.isdigit() for c in text),
        "spaces": text.count(" "),
        "punctuation": sum(not c.isalnum() and not c.isspace() for c in text)
    }