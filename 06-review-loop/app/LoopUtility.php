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
    public function getEvenIndexCharacters($word)
    {
        $evenIndexedCharacters = '';
        $wordArray = str_split($word);
        $wordArraySize = sizeof($wordArray);

        for ($index = 0; $index < $wordArraySize; $index++) {
            if ($this->indexIsEven($index)) {
                $evenIndexedCharacters .= $wordArray[$index];
            }
        }

        return $evenIndexedCharacters;
    }

    /**
     * @param $index
     * @return bool
     */
    public function indexIsEven($index)
    {
        return $index % 2 === 0;
    }
}