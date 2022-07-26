Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "hola mundo"
'hola mundo'
>>> "hola mundo'
SyntaxError: EOL while scanning string literal
>>> "hola mundo'
SyntaxError: EOL while scanning string literal
>>> "este es mi primer texto en python"
'este es mi primer texto en python'
>>> "este es un texto 'entre' comillas dobles"
"este es un texto 'entre' comillas dobles"
>>> 'este es "mi" texto'
'este es "mi" texto'
>>> "este es el metodo para poner \"comillas\" dobles"
'este es el metodo para poner "comillas" dobles'
>>> 'este es \"mi\" texto'
'este es "mi" texto'
>>> c = Franco
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    c = Franco
NameError: name 'Franco' is not defined
>>> c = "franco"
>>> c
'franco'
>>> print("hola mundo")
hola mundo
>>> c+c
'francofranco'
>>> c*20
'francofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofranco'
>>> print(c*20)
francofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofrancofranco
>>> print("mi nombre es"+c)
mi nombre esfranco
>>> print("mi nombre es: " +c)
mi nombre es: franco
>>> print("este es mi primer\ncurso en python")
este es mi primer
curso en python
>>> print("este es otro de\t mis texto")
este es otro de	 mis texto
>>> print("este es otro de\tmis textos")
este es otro de	mis textos
>>> 