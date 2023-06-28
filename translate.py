import deepl

def translate(text, filename ,lang):
    auth_key = "9d56cfd6-b967-d042-9128-1c798129a22d:fx"
    translator =deepl.Translator(auth_key=auth_key)
    path = f"result//{filename}_{lang}.txt"
    result = translator.translate_text(text, target_lang=lang)
    with open(path, "w") as f:
        f.write(result.text)

