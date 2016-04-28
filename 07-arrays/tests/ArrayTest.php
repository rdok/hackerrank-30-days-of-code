<?php
use App\ArrayUtility;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 4/28/16
 */
class ArrayTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_returns_reversed_array_elements_separated_by_space()
    {
        $arrayUtility = new ArrayUtility();
        $input = [1, 4, 3, 2];
        $expectedOutput = "2 3 4 1";

        $this->assertSame($expectedOutput, $arrayUtility->reversedStringSeparatedBySpace($input));
    }
}