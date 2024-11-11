<?php
$string1 = "Hola";
$string2 = "Mundo";
$concatenacion = $string1 . " " . $string2;

$cantidad_palabras = str_word_count($concatenacion);

echo "La concatenación es: '$concatenacion' y tiene $cantidad_palabras palabras.";
?>

