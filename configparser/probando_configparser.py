import configparser

# Creamos una instancia de `ConfigParser`
config = configparser.ConfigParser()

# Leemos el archivo de configuración
config.read('config.ini')

# Accedemos a una sección del archivo de configuración
nombres = config['nombres']
apellidos = config['apellidos']
edad = config['edad']

# Accedemos a un valor de la sección
primerNombre = nombres['primerNombre']
SegundoNombre = nombres['segundoNombre']
primerApellido = apellidos['primerApellido']
SegundoApellido = apellidos['SegundoApellido']
valorEdad = int(edad['valorEdad'])

# Utilizar parametros de archivo de configuracion
print(f'Primer Nombre: {primerNombre} {type(primerNombre)} \nSegundo Nombre: {SegundoNombre} {type(SegundoNombre)}\nPrimer Apellido: {primerApellido} {type(primerApellido)}\nSegundo Apellido: {SegundoApellido} {type(SegundoApellido)} \nEdad: {valorEdad}  {type(valorEdad)}')
