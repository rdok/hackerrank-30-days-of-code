<?php
use App\Matrix;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/2/16
 */
class MatrixTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_stores_elements_from_string()
    {
        $matrix = new Matrix();

        $this->assertCount(0, $matrix->getElements());

        $matrix->storeElementsFromString("1 1 1 0 0 0\n0 1 0 0 0 0");

        $this->assertCount(2, $matrix->getElements());

        $this->assertSame([
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0]
        ], $matrix->getElements());
    }

    /** @test */
    public function it_appends_row()
    {
        $matrix = new Matrix();

        $this->assertCount(0, $matrix->getElements());

        $matrix->appendRow([1, 3, 5]);
        $this->assertCount(1, $matrix->getElements());

        $matrix->appendRow([1234, 55, 525, 525]);
        $this->assertCount(2, $matrix->getElements());
    }
}