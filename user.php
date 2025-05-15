<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    try {
        // Connect to sqlite database
        $db = new SQLite3('user_info.db');
        // Query the clients table
        $result = $db->query('SELECT * FROM clients');

        // Display each tow
        while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
            echo "Name: " . $row['name'] . "<br>";
            echo "Email: " . $row['email'] . "<br>";
            echo "Phone: " . $row['phone'] . "<br>";
            echo "Address: " . $row['address'] . "<br><br>";
        }
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
    ?>
</body>
</html>