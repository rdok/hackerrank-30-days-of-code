<?php namespace App\Utilities;

/**
 * @author Rizart Dokollar <r.dokollari@gmail.com
 * @since 4/19/16
 */
class IntegerUtility
{
    private $i = 4;
    private $d = 4.0;
    private $s = "HackerRank ";

    public function sumInteger($integer)
    {
        return $this->i + $integer;
    }

    public function sumDouble($double)
    {
        return (float)($this->d + $double);
    }

    public function concatenate($string)
    {
        return $this->s.$string;
    }
}