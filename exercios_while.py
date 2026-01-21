#While repete uma ação enquanto ela for verdadeira

# fazendo um simples contador
#iniciando o contador do zero
contador = 0

#while contador < 10:
    #print ("Contador ", contador)
    #contador += 1
    
#exercicio 1 Mostre números de 1 a 10 usando while

while contador < 11:
    print(contador)
    contador += 1
    
#exercicio 2 peça números ao usuário até ele digitar 0
contador2 = int(input("Digite um numero para a contagem regressiva: "))

while contador2 > 0:
    print(contador2)
    contador2 -=1

#exercicio 3 Peça uma senha:Enquanto a senha estiver errada → pedir de novo

senha = input("Digite a senha: ")

while senha != "Teste123": 
    print("Senha incorreta!")
    senha = input("Digite a senha novamente: ")
    
print("Acesso liberado!")