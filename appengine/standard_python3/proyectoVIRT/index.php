<?php
    echo 'Bienvenido, ingrese los siguientes datos:'
?>


<form method="post">

<input type="text" name="nombre" placeholder="nombre">
<input type="text" name="correo" placeholder="correo">
<input type="text" name="telefono" placeholder="telefono">
    
<input type= "submit" name="enviar">

</form>

<?php 
  var_dump($_POST);

  if(isset($_POST['enviar'])){
      
      $nombre = $_POST['nombre'];
      $correo = $_POST['correo'];
      $telefono = $_POST['telefono'];
      echo "conectando a la DB";
      $servidor = "localhost";
      $usuario = "root";
      $clave = "";
      $bd = "Nautilus";

      $coneccion = mysqli_connect ($servidor, $usuario, $clave, $bd );
      if ($coneccion->connect_error) {
        die("Connection failed: " . $coneccion->connect_error);
      }
      echo "Connected successfully";
      
      $insertar = "INSERT INTO registro_distribuidores (nombre, correo, telefono) Values ('$nombre','$correo','$telefono')";
      echo $insertar;
      if ($coneccion->query($insertar) === TRUE) {
        echo "New record created successfully";
      } else {
        echo "Error: " . $insertar . "<br>" . $coneccion->error;
      }
      
      $coneccion->close();

      echo "Datos almacenados";
  }
?>
