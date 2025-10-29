from collections import deque

# Implementación de AC-3 para propagación de restricciones
def ac3(variables, dominios, restricciones):
    cola = deque([(xi, xj) for xi in variables for xj in variables if xi != xj])  # pares de variables

    while cola:
        xi, xj = cola.popleft()
        if revisar_dominio(xi, xj, dominios, restricciones):
            if not dominios[xi]:  # dominio vacío -> inconsistente
                return False
            for xk in variables:
                if xk != xi and xk != xj:
                    cola.append((xk, xi))
    return True

# Revisar y reducir el dominio de xi según xj
def revisar_dominio(xi, xj, dominios, restricciones):
    revisado = False
    nuevos_valores = []
    for x in dominios[xi]:
        if any(restricciones(xi, x, xj, y) for y in dominios[xj]):  # si hay valor compatible
            nuevos_valores.append(x)
        else:
            revisado = True
    dominios[xi] = nuevos_valores
    return revisado

# Ejemplo de CSP con propagación de restricciones
if __name__ == "__main__":
    variables = ['A', 'B', 'C']  # definir variables
    dominios = {
        'A': [1, 2, 3],
        'B': [1, 2, 3],
        'C': [1, 2, 3]
    }

    def restriccion(xi, vi, xj, vj):
        return vi != vj  # valores distintos

    if ac3(variables, dominios, restriccion):
        print("Dominios consistentes tras AC-3:", dominios)
    else:
        print("No hay solución consistente")