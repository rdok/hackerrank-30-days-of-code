<?php
use App\MathUtility;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/2/16
 */
class MathUtilityTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_returns_basic_factorial()
    {
        $mathUtility = new MathUtility();

        $this->assertSame(6, $mathUtility->factorial(3));
        $this->assertSame(120, $mathUtility->factorial(5));
        $this->assertSame(720, $mathUtility->factorial(6));
        $this->assertSame(2432902008176640000, $mathUtility->factorial(20));
    }
}