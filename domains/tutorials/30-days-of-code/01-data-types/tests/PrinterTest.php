<?php namespace Tests;

use App\Utilities\IntegerUtility;
use PHPUnit_Framework_TestCase;

/**
 * @author Rizart Dokollar <r.dokollari@gmail.com
 * @since 4/19/16
 */
class PrinterTest extends PHPUnit_Framework_TestCase
{
    protected $integerUtility;

    public function setUp()
    {
        $this->integerUtility = new IntegerUtility();
    }

    /** @test */
    public function it_gets_sum_of_integers()
    {
        $this->assertSame(16, $this->integerUtility->sumInteger(12));
    }

    /** @test */
    public function it_gets_sum_of_doubles()
    {
        $this->assertSame(8.0, $this->integerUtility->sumDouble(4.0));
    }

    /** @test */
    public function it_gets_concatenated_strings()
    {
        $this->assertSame(
            'HackerRank is the best place to learn and practice coding!',
            $this->integerUtility->concatenate('is the best place to learn and practice coding!')
        );
    }
}