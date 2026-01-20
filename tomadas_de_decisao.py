#For faz repitções com quantidades repetidas

#Range começa em 0 (0,1,2,3,4)
for i in range(5):
    print("Oi")

# exemplo com números
for i in range(5):
    print(i)

#Exercio FOR 
#1 imprima numeros de 1 a 10

#range(1, 11) faz com que ele comece na posição 1 (pulando o zero) e terminar na posição 11(que representa o numero 10)
for i in range(1, 11):
    print (i)
    
#2 faça a tabuado do 5
tabuado_do_cinco = 5
i+1 faz com que i seja somado com mais 1  apos a próxima rodada
i = i+1

for i in range(11):
    print(tabuado_do_cinco * i)
    
#3 Peça um número e mostre todos os números de 0 até ele.
numero_escolhido = int(input("Escolha um número: "))
i = numero_escolhido

# i + 1 no range é necessario para que conte o numero escolhido na posição correta
for i in range(0, i + 1):
    print(i)
