def rythm(poem):
    syllables = []
    for phrase in poem:
        vowels = [letter for letter in phrase if letter in 'аоиеёэыуюя']
        syllables.append(len(vowels))
    if len(set(syllables)) == 1:
         return True
    return False

poem = input('Введите стихотворение ').split() 
if rythm(poem):
    print('Парам пам-пам')
else:
    print('Пам-парам')