<?php
// algoritmo1.php
/*
Comentario de múltiples líneas
que abarca más de una línea
*/

function exampleAlgorithm($input) {
    // Example algorithm: Calculate the factorial of a number
    if ($input < 0) {
        return "Invalid input. Please enter a non-negative integer.";
    }
    
    $factorial = 1;
    for ($i = 1; $i <= $input; $i++) {
        $factorial *= $i;
    }
    
    return $factorial;
}

// Example usage
$input = 5;
echo "The factorial of $input is " . exampleAlgorithm($input);
?>