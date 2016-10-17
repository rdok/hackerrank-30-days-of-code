<?php
use App\LoopUtility;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 4/28/16
 */
class LoopTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_prints_first_ten_multiples()
    {
        $input = 2;
        $expectedOutput = "2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20\n";

        $loopUtility = new LoopUtility();

        $this->assertSame($expectedOutput, $loopUtility->getMultiples($input));
    }
}