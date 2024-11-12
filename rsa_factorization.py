import math
from sympy import mod_inverse

def factorization(n):
    # Tenta fatorar n encontrando p e q
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return None, None  # Se não encontrar fatores

def encontrar_chave_privada(e, n):
    # Fatorar n para encontrar p e q
    p, q = factorization(n)
    if p is None or q is None:
        print("Não foi possível fatorar n")
        return None

    # Calcular φ(n)
    phi_n = (p - 1) * (q - 1)

    # Calcular d como o inverso modular de e módulo φ(n)
    try:
        d = mod_inverse(e, phi_n)
        return d
    except ValueError:
        print("Não foi possível encontrar o inverso modular.")
        return None

# Exemplo de uso
e = 65534413437  # Exemplo de valor comum para e
n = 32325432612

# Exemplo pequeno de n para teste, deve ser substituído pelo valor real

d = encontrar_chave_privada(e, n)
if d:
    print("Foi encontrada a chave privada:", d)
else:
    print("Chave privada não encontrada.")