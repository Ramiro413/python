class cadena:
  def longitudCadena(self):
    x=input("Palabra: ")
    y=x
    y=y[1:]
    contador=0
    for i in x:
      contador+=1
    print(y,'tiene',contador,'caracteres.')

  

cadena=cadena()
cadena.longitudCadena()
