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
    <title>Contacto</title>
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
            background-image: url(static/fondomitad.jpg);
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
            color: #000;
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
        .desc22        
        {
			background-color: #2e677a;
            font-size: 9px;
			color:#fff;
            height: 5vh;
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
        .div5        
        {
            font-size: 8px;
			color:#2e677a;
            height: 1vh;
            margin: 5%;
            display: flex;
            justify-content:left;
            align-items: center;    
        }
        .div6        
        {
            font-size: 8px;
			color:#000000;
            height: 1vh;
            margin: 5%;
            display: flex;
            justify-content:left;
            align-items: center;    
        }
        .divtexto        
        {
			color:#2e677a;
            height: 1vh;
            margin: 5%;
            display: flex;
            justify-content:center;
            align-items: center;
            text-align: center;
            font-size: 9px;
        }
        .divtexto2        
        {
			color:#2e677a;
            height: 10vh;
            margin: 5%;
            display: flex;
            justify-content:center;
            align-items: center;
            text-align: center;
            font-size: 25px;
        }

    </style>
    <style>
        .texto {
            font-style: normal;
            font-weight: 200;
            font-size: 25px;
            color: black;   
            margin: 15%;
            display: flex;
            justify-content: center;
            align-items:normal;

        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@100&display=swap" rel="stylesheet">


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
        <h1> CONTACTO </h1>       
    </div>


    <div class="space"></div>

    <div class="divtexto">
        <img src="static/cliente.png" alt="." width="590">
        <h1>¡Bienvenido a nuestro portal! Estamos encantados de que desees ponerte en contacto con nosotros. Si tienes alguna pregunta, sugerencia, comentario o simplemente deseas saludarnos, este es el lugar adecuado.
            Para ponerte en contacto con nosotros, por favor lee la información y mándanos un mensaje
            Si tienes alguna pregunta específica sobre nuestros productos o servicios, no dudes en echar un vistazo a nuestras preguntas frecuentes. También puedes encontrar información adicional en nuestras redes sociales y blog.

            ¡Gracias por ponerte en contacto con nosotros! Estamos ansiosos por ser parte del proceso de crecimiento de tu empresa.<h1>
    </div>


    <div class="space"></div>

    <div class="divtexto2">
        <img src="static/red1.png" alt="." width="290">

        <a href="https://www.facebook.com/profile.php?id=100092171114292&mibextid=LQQJ4d">Ir a la página de Facebook: Corporación Nautilus GT</a>
    </div>

    <div class="divtexto2">
        <img src="static/red2.png" alt="." width="290">
        <a href="mailto:nautiluscorpgt@gmail.com">Enviar correo electrónico: nautiluscorpgt@gmail.com</a>


    </div>



    <div class="desc22">
        <h1> PREGUNTAS FRECUENTES </h1>       
    </div>

    <!--preguntas-->
    <div class="div5">
        <h1>¿Cómo me pongo en contacto con ustedes?</h1>
    </div>
    <div class="div6">
        <h1>Puedes enviar un mensaje a nuestro correo Gmail: nautiluscorpgt@gmail.com
            solicitando una reunión exponiendo tus principales necesidades empresariales.</h1>
    </div>
    <!--preguntas-->

    <div class="div5">
        <h1>¿Quiénes son ustedes?</h1>
    </div>
    <div class="div6">
        <h1>Somos una empresa 100% Guatemalteca, brindamos servicios de transporte de carga
            marítima a todos los países latinoamericanos y del caribe.</h1>
    </div>
    <!--preguntas-->
    <div class="div5">
        <h1>¿Dónde están ubicados?</h1>
    </div>
    <div class="div6">
        <h1>Tenemos nuestra sede central en la ciudad de Guatemala, C.A. donde agendamos reuniones
            ejecutivas generales y donde tenemos nuestra sede de servicio al cliente principal. 
            Nuestro centro marítimo está ubicado en Puerto Barrios, Guatemala C.A.</h1>
    </div>
    <!--preguntas-->       
    <div class="div5">
        <h1>¿Tienen planes de financiamiento?</h1>
    </div>
    <div class="div6">
        <h1>En lo absoluto, tenemos planes de financiamiento según cantidad, distancia y categorías 
            de los productos que la empresa solicitante desea manejar.</h1>
    </div>
    <!--preguntas-->   
    <div class="div5">
        <h1>Si un cargamento no llegara a su destino, ¿qué procede??</h1>
    </div>
    <div class="div6">
        <h1>Nosotros nos aseguramos de que cada cargamento sea transportado y recibido con la mejor calidad, 
            y si en dado caso existiera algún contratiempo, contamos con una póliza de seguro.</h1>
    </div>
    <!--preguntas-->
    <div class="div5">
        <h1>¿Existen devoluciones monetarias?</h1>
    </div>
    <div class="div6">
        <h1>No, ya que cada uno de los recursos es utilizado con un propósito y no contamos con un fondo 
            para cuando exista un arrepentimiento de algún cliente. </h1>
    </div>
    <!--preguntas-->   
    <div class="div5">
        <h1>¿Cómo puedo saber el estado de mi envío?</h1>
    </div>
    <div class="div6">
        <h1>Durante el traslado de su envío, puede hacer consultas al número telefónico de nuestro centro 
            de atención al cliente, este estará siendo brindado al momento de cierre de contrato. </h1>
    </div>
    <!--preguntas--> 
    <div class="div5">
        <h1>¿Qué clase de productos puedo enviar y recibir?</h1>
    </div>
    <div class="div6">
        <h1>Cualquier clase de productos, tenemos secciones para productos frágiles y no tan frágiles, 
            el costo y tiempos de entrega varían en cada uno de ellos. Tomar en cuenta que existen costos 
            fijos de cantidades específicas según kilogramos a movilizar. </h1>
    </div>
    <!--preguntas-->


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
