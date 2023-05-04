from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="estilos" href="styles.css"> 
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@100&display=swap" rel="stylesheet">
    <title>Negocios</title>
    <link rel="icon" href="logo_nautilus.ico">
</head>
<body>
    <style>

        /* estilos CSS para la pagina*/
        /*estilos para barra fija superior*/
        *{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body{
            font-family: 'PT Sans', sans-serif;
        }
        header {
            width: 100%;
            height: 100vh;
            background-image: url(static/fondofinal.jpg);
            background-size: cover;
            background-position: center;
        }
        .nav{

            position: fixed;
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 25px;
            transition: all 0.5s ease;

        }
        .nav.active{

            background: #3a96b5;
            padding: 15px;
        }
        .nav.active .logo,
        .nav.active a{
            color: #fff;
        }
        .nav.active a:hover{

            background: #000;
            color: #fff;

        }
        .logo{
            font-size: 25px;
            color: #fff;
            font-weight: 100;
        }
        .menu{
            display: flex;
        }
        .menu li{
            list-style: none;
            margin: 10px;            
        }
        .menu li a{
            color: #fff;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.5s ease;
        }        
        .menu li a:hover{
            padding: 5px 10px;
            background: #fff;
            color: #000;
            border-radius: 15px;
        }
        .scrol{

            height: 900px;

        }
        /*estilos de texto interior medio pagina*/
        .desc        
        {
			background-color: #2e677a;
			color:#fff;
            height: 10vh;
            margin: 5%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .fotoportada       
        {
            background: size 10%;
            height: 2vh;
            margin: 5%;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        div {
            height: 20px; 
        }
        .div2 {
            height: 350px; 
        } 
        .space {
            height: 230px; 
        }        
        .contenedorNot        
        {
            background-color: none;
            color:#333;
            height: 0.5vh;
            margin: 4%;
            font-size: 2px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .gradiente {
            height: 100px;
            background: linear-gradient(to left, #a49797, #3a7990);
        }
        .div3        
        {
            font-size: 5px;
            background-color: none;
			color:#2e677a;
            height: 1vh;
            margin: 5%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .div4        
        {
            font-size: 5px;
            background-color: none;
			color:#2e677a;
            height: 1vh;
            margin: 5%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .divtexto        
        {
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            font-size: 15px;
            background-color: none;
			color:#2e677a;
            height: 1vh;
            margin: 5%;

            justify-content: center;
            align-items: center;
        }
        .divtexto h2{
            font-style: normal;
        }
    </style>
    <style>
        .texto {
            font-style: normal;
            font-weight: 2000;
            font-size: 20px;
            color: black;   
            margin: 15%;

            justify-content: center;
            align-items: center;
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@100&display=swap" rel="stylesheet">


    <title>Comentarios</title>






    <!--Aqui comienza el texto html-->

    <header>
        <nav class="nav">    
            <ul class="menu">
                <div class="logo">CORPORACION NAUTILUS</div>    
                <li><a href="#">Inicio</a></li>
                <li><a href="#">Servicios</a></li>
                <li><a href="#">Contacto</a></li>
                <li><a href="#">Negocios</a></li>                
            </ul>
        </nav>    
    </header>


    <div class="desc">
        <h1> NEGOCIOS </h1>       
    </div>

    <div class="divtexto">
        <h1>Candidatos a Distribuidores.</h1>
        <h2>Y Recopilación de Datos</h2>
    </div>


    <!--formulario comienza-->



<form method="post">

<input type="text" name="nombre" placeholder="nombre">
<input type="text" name="correo" placeholder="correo">
<input type="text" name="telefono" placeholder="telefono">
    
<input type= "submit" name="enviar">

</form>



    <!--aqui termina el formulario-->


    <div class="space"></div>


    <div class="div3">
        <h1>Página creada por: Grupo Atlas. Guatemala C.A. 2023       </h1>
    </div>
    <div class="div4">
        <h1>© Copyright Nautilus Corp. 2023</h1>
    </div>

    <div class="gradiente"></div>
    <script>
        const nav = document.querySelector('.nav');
            window.addEventListener('scroll',function(){
                nav.classList.toggle('active',window.scrollY>0)
            })
    </script>
</body>
</html>
    
    '''

if __name__ == '__main__':
    app.run()
