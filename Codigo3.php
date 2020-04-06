$servidor= "localhost";
$usuario= "root";
$password = "";
$nombreBD= "php_buscador";
$db = new mysqli($servidor, $usuario, $password, $nombreBD);
if ($db->connect_error) {
    die("la conexión ha fallado: " . $db->connect_error);
}
?>
