<?php namespace App;
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */

class HackerRank
{
    private $hourglass;

    public function __construct($stream)
    {
        $this->reader = new Reader($stream);

        $this->hourglass = new Matrix();
    }

    public function printRequirements()
    {
//        while (($row = $this->reader->readNextLine()) !== false) {
//            
//            $binaryNumber = $this->hourglass->getBinary($row);
//
//            echo $this->hourglass->getMaximumNumberOfConsecutiveOnes($binaryNumber)."\n";
//        }
        return null;
    }
}
