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
    public function getEvenAndOddCharactersSeparatedByTwoSpaces($word)
    {
        $word = trim(preg_replace('/\s\s+/', '', $word));

        return sprintf("%s %s\n", $this->getEvenIndexCharacters($word), $this->getOddIndexCharacters($word));
    }

    public function getEvenIndexCharacters($word)
    {
        return $this->getIndexCharacters($word);
    }

    private function getIndexCharacters($word, $requiredEvenIndex = true)
    {
        $evenIndexedCharacters = '';
        $wordArray = str_split($word);
        $wordArraySize = sizeof($wordArray);

        for ($index = 0; $index < $wordArraySize; $index++) {
            if ($requiredEvenIndex && $this->indexIsEven($index)
                || !$requiredEvenIndex && $this->indexIsOdd($index)
            ) {
                $evenIndexedCharacters .= $wordArray[$index];
            }
        }

        return $evenIndexedCharacters;
    }

    /**
     * @param $index
     * @return bool
     */
    private function indexIsEven($index)
    {
        return $index % 2 === 0;
    }

    private function indexIsOdd($index)
    {
        return $index % 2 !== 0;
    }

    public function getOddIndexCharacters($word)
    {
        return $this->getIndexCharacters($word, false);
    }
}