<?php namespace App;

/**
 * @author Rizart Dokollar <r.dokollari@gmail.com
 * @since 4/19/16
 */
class Printer
{
    public function printIntegersSum()
    {
        $handle = fopen("php://stdin", "r");
        $i = 4;
        $d = 4.0;
        $s = "HackerRank ";

        // Read and save an integer, double, and String to your variables.
        $integer = fgets($handle);
        $double = fgets($handle);
        $string = fgets($handle);

// Print the sum of both integer variables on a new line.
        echo($i + $integer);

// Print the sum of the double variables on a new line.
        echo("\n".number_format($d + $double, 1));

// Concatenate and print the String variables on a new line
// The 's' variable above should be printed first.
        echo("\n".($s.$string));
        fclose($handle);
    }

}