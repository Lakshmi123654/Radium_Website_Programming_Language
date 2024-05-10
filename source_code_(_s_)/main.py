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

    if ((code.startswith ("." == True) and ("=" in code) :

	if (".title" in code) :

		global title
		title = str (code.replace (".title", "").rstrip ().lstrip ()

	if (".content" in code) or (".body" in code) :

		global body
		body = str (code.replace (".body", "").rstrip ().lstrip ().replace ("\n", "<br> </br>")
       
global html_content
html_content = """
<!DOCTYPE html>
<html lang = "en">
<head>

    <meta charset = "UTF-8">
    <meta name = "viewport" content = "width=device-width, initial-scale=1.0">
    
    <title> {title} </title>

    <link href = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel = "stylesheet" integrity = "sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin = "anonymous">

    <script src = "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity = "sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin = "anonymous"></script>
    <script src = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity = "sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin = "anonymous"></script>
    <script src = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity = "sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin = "anonymous"></script>	
    
</head>

<body>
    
    {body}
    
</body>

</html>
"""
x.write (html_content)
x.close ()

webbrowser.open ("C:\\Users\\Admin\\index.html")
