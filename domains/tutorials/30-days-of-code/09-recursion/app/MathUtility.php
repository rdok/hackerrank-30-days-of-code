<?php
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/2/16
 */

namespace App;

/**
 * Class MathUtility
 * @package App
 */
class MathUtility
{
    /**
     * Factorial constructor.
     */
    public function __construct()
    {
    }

    /**
     * @param $integer
     * @return int
     */
    public function factorial($integer)
    {
        if ($integer === 1) {
            return 1;
        }

        return $integer * $this->factorial($integer - 1);
    }
}