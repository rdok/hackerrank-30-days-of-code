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
    }

    public function printRequirements()
    {
        while (($elementsRow = $this->reader->readNextLine()) !== false) {
            $this->matrix->storeElementsFromStringRow($elementsRow);

//            $binaryNumber = $this->hourglass->getBinary($row);
//
//            echo $this->hourglass->getMaximumNumberOfConsecutiveOnes($binaryNumber)."\n";
        }

        return null;
    }
}
