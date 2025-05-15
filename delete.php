<?php 
if ( isset($_GET["id"]) ) {
    $id = intval($_GET["id"]);

    $connection = new SQLite3('user_info.db');

    $sql = "DELETE FROM clients WHERE id=$id";
    $connection->query($sql);
}

header("location: index.php");
exit;

?>