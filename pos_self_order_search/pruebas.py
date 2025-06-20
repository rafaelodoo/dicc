

def funcion_decoradora(func):

    def super_envoltura(*args, **kwargs):
        resultado=func(*args, **kwargs)
        return resultado

    return super_envoltura

    

@funcion_decoradora
def saludo_nombre(nombre,apellido):
    if apellido:
        return "hola "+nombre+" "+apellido
    else:
        return "hola "+nombre

# Llamamos a la función decorada
resultado_final = saludo_nombre("Rafael","Lopez")
print(resultado_final)