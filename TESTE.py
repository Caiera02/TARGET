INDICE = 13
soma = 0
K = 0

while K < INDICE :
    K += 1
    soma = soma + K

print(soma)

#Ao final do processamento, qual será o valor da variável SOMA?
# Será o valor de 91
#----------------------------------------------------------------------------------

def fibonacci_sequence(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def verifica_pertence(numero, sequencia):
    if numero in sequencia:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
sequencia_fibonacci = fibonacci_sequence(numero)
print(verifica_pertence(numero, sequencia_fibonacci))

#--------------------------------------------------------------------------------------------
# 3) Descubra a lógica e complete o próximo elemento:

a= 1,3,5,7,9

b= 128

c= 49

d= 100

e= 13

f= 20
#=================================================================================================
#4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

#omo você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

Respota = Eu iria na sala, pediria pra alguém ligar o interruptor e avisaria que acendeu e pediria pra marcar a o interruptor com o numero da sala 

#=========================================================================================

