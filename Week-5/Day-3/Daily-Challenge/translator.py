from translate import Translator
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translator= Translator(from_lang="french",to_lang="english")
translation = [translator.translate(word) for word in french_words]


result = {french_words[i]: translation[i] for i in range(len(french_words))}

print(result)
