import json

# Abrimos el archivo de configuración
with open('config.json') as config_file:
    # Cargamos el contenido del archivo en un diccionario
    config = json.load(config_file)

# Accedemos a un valor del diccionario
primerNombre = config['primerNombre']
segundoNombre = config['segundoNombre']
primerApellido = config['primerApellido']
segundoApellido = config['segundoApellido']
edad = config['edad']

# Utilizar parametros de archivo de configuracion
print(f'Primer Nombre: {primerNombre} {type(primerNombre)} \nSegundo Nombre: {segundoNombre} {type(segundoNombre)}\nPrimer Apellido: {primerApellido} {type(primerApellido)}\nSegundo Apellido: {segundoApellido} {type(segundoApellido)} \nEdad: {edad}  {type(edad)}')
