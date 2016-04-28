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
class ArrayUtility
{
    public function reversedStringSeparatedBySpace(array $input)
    {
        $array = array_reverse($input);

        return implode(" ", $array);
    }
}