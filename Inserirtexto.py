import os
os.chdir("C:\\Users\\User\\Desktop\\Projetinho")
linha_especifica=1
texto = input("digite o texto que deseja inserir \n".upper())

file = open('texto.txt', 'r')
lines = file.readlines()
file.close()

lines.insert(linha_especifica, texto + "\n")

file = open('texto.txt', 'w')
file.writelines(lines)
file.close()
