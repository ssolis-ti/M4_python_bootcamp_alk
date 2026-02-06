with open("demo_escritura.txt",'w',encoding='utf-8') as archivo:
    archivo.write("un elefante, se balanceaba\n")
    archivo.write("sobre la tela de una araña\n")

#el econding sirve para decirle a python la codificacion con la que trabajaremos al escribir el archivo
lista_heroes =['Iron Man',
'Captain America',
'Thor',
'Black Widow',
'Hulk',
'Hawkeye',
'Captain Marvel',
'Spider-Man',
'Doctor Strange',
'Scarlet Witch',
'Black Panther',
'Ant-Man',
'Wasp',
'Falcon',
'Winter Soldier',
'War Machine',
'Nebula',
'Gamora',]

# lista_heroes = [ heroe + '\n' for heroe in lista_heroes]

for indice in range(len(lista_heroes)):
    lista_heroes[indice] = lista_heroes[indice] + '\n'


with open("avengers.txt",'w', encoding='utf-8') as file:
    file.writelines(lista_heroes)