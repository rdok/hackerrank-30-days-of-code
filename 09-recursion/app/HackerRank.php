<?php namespace App;
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */

class HackerRank
{
    private $mathUtility;

    public function __construct($stream)
    {
        $this->reader = new Reader($stream);

        $this->mathUtility = new MathUtility();
    }

    public function printRequirements()
    {
        while (($integer = $this->reader->readNextLine()) !== false) {
            $integer = (int)rtrim($integer);

            echo $this->mathUtility->factorial($integer)."\n";
        }
        $this->reader->close();
    }
}
