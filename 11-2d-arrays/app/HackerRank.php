<?php namespace App;
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */

class HackerRank
{
    private $matrix;

    public function __construct($stream)
    {
        $this->reader = new Reader($stream);
        $this->matrix = new Matrix();
        $this->hourglass = new Hourglass($this->matrix);
    }

    public function printRequirements()
    {
        while (($elementsRow = $this->reader->readNextLine()) !== false) {
            $this->matrix->storeElementsFromStringRow($elementsRow);
        }

        echo $this->hourglass->findGreatestSum();
    }
}
