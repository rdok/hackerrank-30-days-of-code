<?php
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 4/28/16
 */

namespace App;


/**
 * Class LoopUtility
 * @package App
 */
class LoopUtility
{

    /**
     * LoopUtility constructor.
     */
    public function __construct()
    {
    }

    /**
     * @param $integer
     * @param int $maximumMultiples
     * @return string
     */
    public function getMultiples($integer, $maximumMultiples = 10)
    {
        $multiples = '';

        for ($index = 1; $index <= $maximumMultiples; $index++) {
            $multiples = $this->formatStringRow($integer, $index, $multiples);
        }

        return $multiples;
    }

    /**
     * @param $integer
     * @param $index
     * @param $multiples
     * @return string
     */
    private function formatStringRow($integer, $index, $multiples)
    {
        $multiples .= "$integer x $index = " . $index * $integer . "\n";

        return $multiples;
    }
}