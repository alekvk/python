'''
38. Напишите программу, удаляющую
из текста все слова, содержащие ""абв"".
'''

text = "Привет, абырвалг мебв! р рарабрв аааа вабв! Вабв, абв"
text = text.split()
text_new = []
for i in range (len(text)):
    if "абв" not in text[i]:
        text_new.append(text[i])
text2 = ("  ".join(text_new))
print(text2)
