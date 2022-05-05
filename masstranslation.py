import pandas as pd
from googletrans import Translator
translator = Translator()

sourcelang = "French"
sourcelangcode = "fr"

df = pd.read_csv("fortranslation.csv")

df["English"] = [translator.translate(i, dest='en', src=sourcelangcode).text for i in df[sourcelang]]
# df["French"] = [translator.translate(i, dest='fr', src=sourcelangcode).text for i in df[sourcelang]]
df["Spanish"] = [translator.translate(i, dest='es', src=sourcelangcode).text for i in df[sourcelang]]
df["Italian"] = [translator.translate(i, dest='it', src=sourcelangcode).text for i in df[sourcelang]]
df["German"] = [translator.translate(i, dest='de', src=sourcelangcode).text for i in df[sourcelang]]
df["Hindi"] = [translator.translate(i, dest='hi', src=sourcelangcode).text for i in df[sourcelang]]
df["Japanese"] = [translator.translate(i, dest='ja', src=sourcelangcode).text for i in df[sourcelang]]
df["Swedish"] = [translator.translate(i, dest='sv', src=sourcelangcode).text for i in df[sourcelang]]

df.to_csv("translated.csv", sep= ",", index=False, encoding="utf-8")
