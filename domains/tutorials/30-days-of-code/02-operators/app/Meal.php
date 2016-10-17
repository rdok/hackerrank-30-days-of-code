<?php namespace App;

/**
 * @author Rizart Dokollar <r.dokollari@gmail.com
 * @since 4/20/16
 */
class Meal
{
    private $tipPercent;
    private $taxPercent;
    private $cost;

    public function __construct($cost, $tipPercent, $taxPercent)
    {
        $this->tipPercent = $tipPercent;
        $this->taxPercent = $taxPercent;
        $this->cost = $cost;
    }

    public function toString()
    {
        return sprintf('The total meal cost is %d dollars.', $this->getTotalCost());
    }

    public function getTotalCost()
    {
        $tip = $this->cost * $this->tipPercent / 100;
        $tax = $this->cost * $this->taxPercent / 100;
        $totalCost = $this->cost + $tip + $tax;

        return round($totalCost);
    }
}