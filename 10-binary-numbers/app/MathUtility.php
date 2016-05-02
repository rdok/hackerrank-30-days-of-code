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
    public function getBinary($number)
    {
        return decbin($number);
    }

    public function getMaximumNumberOfConsecutiveOnes($number)
    {
        $numberArray = str_split($number);
        $maximumConsecutiveOnesCounter = 0;
        $currentConsecutiveOnesCounter = $maximumConsecutiveOnesCounter;

        foreach ($numberArray as $digit) {
            $digit = (int)$digit;

            $currentConsecutiveOnesCounter =
                $this->incrementOrResetCurrentConsecutiveOnesCounter($digit, $currentConsecutiveOnesCounter);

            if ($this->isNewMaxCounterOfConsecutiveOnesFound($currentConsecutiveOnesCounter,
                $maximumConsecutiveOnesCounter)
            ) {
                $maximumConsecutiveOnesCounter = $currentConsecutiveOnesCounter;
            }
        }

        return $maximumConsecutiveOnesCounter;
    }

    /**
     * @param $digit
     * @param $currentConsecutiveOnesCounter
     * @return int
     */
    private function incrementOrResetCurrentConsecutiveOnesCounter($digit, $currentConsecutiveOnesCounter)
    {
        if ($digit === 1) {
            $currentConsecutiveOnesCounter++;

            return $currentConsecutiveOnesCounter;
        }

        $currentConsecutiveOnesCounter = 0;

        return $currentConsecutiveOnesCounter;
    }

    /**
     * @param $currentConsecutiveOnesCounter
     * @param $maximumConsecutiveOnesCounter
     * @return bool
     */
    private function isNewMaxCounterOfConsecutiveOnesFound($currentConsecutiveOnesCounter, $maximumConsecutiveOnesCounter)
    {
        return $currentConsecutiveOnesCounter > $maximumConsecutiveOnesCounter;
    }
}