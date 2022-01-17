# import main Flask class and request object
from flask import Flask, Response, request, redirect, url_for
from unicodedata import normalize
from http import HTTPStatus

# create the Flask app
app = Flask(__name__)

#crea el archivo si no existe y abre en modo anexar
try:
	file = open('archivo.txt','a+')
	print("archivo.txt is open")
except:
	print("An exception occurred")
 
print("Server operative")

@app.route('/correct')
def correct():
  return Response('<h1>received<h1>', HTTPStatus.CREATED)

#endpoint 1
@app.route('/file/write/', methods=['POST'])
def addText():
  try:
    # Recoge el argumento string de la petición 
    str = request.form('str')
    #escribe en el fichero y salta de linea
    file.write( str + '\n')
    file.flush()
    return redirect(url_for('/correct'))

  except:
    print("An exception occurred")  
    return Response('error', HTTPStatus.BAD_REQUEST)

#endpoint 2
@app.route('/file/read')
def matchesToWord():
  try:
    # Almacenamos la palabra que queremos buscar
    word = request.args.get('str')
    #iniciamos variable contador
    cont = 0  
    #bucle for para recorrer linea a linea del archivo
    for line in file:
      # Si la linea contiene la palabra suma 1 al contador
      if word in line:
        cont+=1
    return Response('La palabra ' + word + ' aparece ' + cont , HTTPStatus.BAD_REQUEST)

  except:
    print("An exception occurred")  
    return   Response('<h1>ERROR<h1>', HTTPStatus.BAD_REQUEST)             

# run app in debug mode on port 12345
app.run(debug=True, port=12345)

	