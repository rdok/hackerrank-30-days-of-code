<?php
use App\Hourglass;
use App\Matrix;
use App\Reader;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/3/16
 */
class HourglassTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_finds_greatest_sum()
    {
        $matrix = new Matrix();
        $reader = new Reader(__DIR__.'/../storage/basic-test-input.txt');
        $matrix->storeElementsFromReader($reader);

        $hourglass = new Hourglass($matrix);

        $reader = new Reader(__DIR__.'/../storage/basic-test-output.txt');
        $expectedOutput = (int)$reader->readNextLine();

        $this->assertSame($expectedOutput, $hourglass->findGreatestSum());
    }
}