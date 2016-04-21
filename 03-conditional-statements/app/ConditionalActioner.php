<?php namespace App;
use Exception;

/**
 * @author Rizart Dokollar <r.dokollari@gmail.com
 * @since 4/21/16
 */
class ConditionalActioner
{
    public function check($number)
    {
        if ($this->isEven($number) && $number >= 6 && $number <= 20) {
            return 'Weird';
        }

        if ($this->isEven($number) && $number >= 2 && $number <= 5) {
            return 'Not Weird';
        }

        if ($this->isEven($number) && $number > 20) {
            return 'Not Weird';
        }

        if ($this->isOdd($number)) {
            return 'Weird';
        }

        return new Exception('Not Implemented.');
    }

    private function isEven($int)
    {
        if ($int % 2 === 0) {
            return true;
        }

        return false;
    }

    private function isOdd($number)
    {
        if ($number % 2 !== 0) {
            return true;
        }

        return false;
    }
}