<?php
use App\MathUtility;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/2/16
 */
class MathUtilityTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_returns_binary_format()
    {
        $mathUtility = new MathUtility();

        $this->assertSame("101", $mathUtility->getBinary(5));
        $this->assertSame("1101", $mathUtility->getBinary(13));
    }

    /** @test */
    public function it_returns_maximum_number_of_consecutive_ones()
    {
        $mathUtility = new MathUtility();

        $this->assertSame(1, $mathUtility->getMaximumNumberOfConsecutiveOnes(101));
        $this->assertSame(2, $mathUtility->getMaximumNumberOfConsecutiveOnes(1101));
        $this->assertSame(0, $mathUtility->getMaximumNumberOfConsecutiveOnes(0));
    }
}