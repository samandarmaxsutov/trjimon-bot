from googletrans import Translator

translator = Translator()


def getTranslate(text):
    return translator.translate(text,getTranslateLang(text)).text

def getTranslateLang(text):
    lan = translator.detect(text).lang

    det = 'uz' if lan == 'en' else 'en'
    return det

print(getTranslateLang("Salom")=='en')