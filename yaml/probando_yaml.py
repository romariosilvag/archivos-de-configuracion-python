import yaml

# Abrimos el archivo de configuración
with open('config.yaml', 'r') as config_file:
    # Cargamos el contenido del archivo en un diccionario
    config = yaml.safe_load(config_file)

# Accedemos a una sección del archivo de configuración
nombres = config['nombres']
apellidos = config['apellidos']
edad = config['edad']

# Accedemos a un valor de la sección
primerNombre = nombres['primerNombre']
segundoNombre = nombres['segundoNombre']
primerApellido = apellidos['primerApellido']
segundoApellido = apellidos['segundoApellido']
valorEdad = edad['valorEdad']

# Utilizar parametros de archivo de configuracion
print(f'Primer Nombre: {primerNombre} {type(primerNombre)} \nSegundo Nombre: {segundoNombre} {type(segundoNombre)}\nPrimer Apellido: {primerApellido} {type(primerApellido)}\nSegundo Apellido: {segundoApellido} {type(segundoApellido)} \nEdad: {valorEdad}  {type(valorEdad)}')

