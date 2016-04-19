<?php
use App\Printer;

/**
 * @author Rizart Dokollar <r.dokollari@gmail.com
 * @since 4/19/16
 */
class PrinterTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_prints_sum_of_both_integers_on_a_new_line()
    {
        $printer = $this->getMock(Printer::class);

        $printer->expects($this->any())
            ->method('fgets')
            ->willReturn(12);

        $this->expectOutputString(16);

        $printer->printIntegersSum();
    }
}