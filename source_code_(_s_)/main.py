import webbrowser
import os

os.system ("cls")

x = open ("C:\\Users\\Admin\\index.html", "w")
ask = input ("\n\033[1;32mPlease enter the full computer location path to the .txt text file to be run as a radium website : ")
y = open (f"{ask}", "r")

codes = str (y.read ()).split ("\n")

for code in codes :

    if ("//" in code) :

        2 == 2 

    if (";" in code) :

        code = code.replace (";")

    if ("radium website to be build down here" in code) :

        2 == 2

    if ((code [0] == ".") and (".title" in code) and ("=" in code)) :

        global title
        title = str (code.replace (".title" , "").replace ("=", "").lstrip ().rstrip ())

        x.write ("""<!DOCTYPE html>

         <html lang = "en">
         
         <head>

             <meta charset="UTF-8">
	         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
	         <meta name="viewport" content="width=device-width, initial-scale=1.0">

          <title>""" + title + """</title>""")
        
x.close ()
