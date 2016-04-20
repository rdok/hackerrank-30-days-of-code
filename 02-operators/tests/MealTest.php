<?php
use App\Meal;

/**
 * @author Rizart Dokollar <r.dokollari@gmail.com
 * @since 4/20/16
 */
class MealTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_returns_total_meal_cost()
    {
        $meal = new Meal(12.00, 20, 8);

        $this->assertSame(
            15.0,
            $meal->getTotalCost()
        );
    }

    /** @test */
    public function it_returns_total_meal_cost_message()
    {
        $meal = new Meal(12.00, 20, 8);

        $this->assertSame(
            'The total meal cost is 15 dollars.',
            $meal->toString()
        );
    }
}