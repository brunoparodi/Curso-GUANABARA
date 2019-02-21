frase = 'Curso em Vídeo Python1'
print(frase[9::3])
print(len(frase))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android')) #substitui pontualmente
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = '   Aprenda Python2  '
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

print(frase.split())

frase3 = 'Curso em Vídeo Python3'
print('-'.join(frase3))