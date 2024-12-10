import math
from sympy import mod_inverse


def is_prime(num):
    # Simple check if a number is prime
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def factorization(n):
    # Tenta fatorar n encontrando p e q
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i) and is_prime(n//i):
                return i, n // i
            
    return None, None  # Se não encontrar fatores

def encontrar_chave_privada(e, n):
    # Fatorar n para encontrar p e q, ambos primos
    p, q = factorization(n)
    
    # Se não for possível fatorar n, retornar None 
    if p is None or q is None:
        print("Não foi possível fatorar n")
        return None

    # Calcular o coeficiente 
    coef = (p - 1) * (q - 1)

    # Calcular d como o inverso modular de e módulo coef
    # d = e^(-1) mod coef
    try:
        d = mod_inverse(e, coef)
        return d
    except ValueError:
        print("Não foi possível encontrar o inverso modular.")
        return None

def decrypt(cipher_text, d, n):
    # Descriptografar cada número no texto cifrado
    decrypted_numbers = [pow(int(c), d, n) for c in cipher_text.split()]
    # Converter números para caracteres
    decrypted_text = ''.join(chr(num) for num in decrypted_numbers)
    return decrypted_text


cipher_text = input("Insira o texto cifrado (números separados por espaço): ")

# Obter a chave pública
# PU = (e, n)
e = int(input("Insira o inteiro e: ")) 
n = int(input("Insira o valor de n: "))

# Calcular a chave privada
# PR = (d, n)
d = encontrar_chave_privada(e, n)

# Se achou a chave, descriptografa o texto cifrado 
if d:
    print("Foi encontrada a chave privada:", d)
    # Descriptografar o texto
    decrypted_text = decrypt(cipher_text, d, n)
    # Converter o texto descriptografado em decimais
    decrypted_decimals = [ord(char) for char in decrypted_text]
    print("Texto descriptografado (em ASCII):", decrypted_text)
    print("Texto descriptografado (em decimais):", decrypted_decimals)
else:
    print("Chave privada não encontrada.")