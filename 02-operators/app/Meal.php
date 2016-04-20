<?php

/**
 * @author Rizart Dokollar <r.dokollari@gmail.com
 * @since 4/20/16
 */
class Meal
{

    public function cost()
    {
        $handle = fopen("php://stdin", "r");
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        $mealCost = (float)fgets($handle);
        $tipPercent = (float)fgets($handle);
        $taxPercent = (float)fgets($handle);

        $tip = $mealCost * $tipPercent / 100;
        $tax = $mealCost * $taxPercent / 100;
        $totalCost = $mealCost + $tip + $tax;

        $cost = round($totalCost);

        echo "The total meal cost is $cost dollars.";
    }
}