<?php
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/3/16
 */

namespace App;


/**
 * Class Hourglass
 * @package App
 */
class Hourglass
{
    /**
     * @var Matrix
     */
    private $matrix;

    /**
     * Hourglass constructor.
     * @param Matrix $matrix
     */
    public function __construct(Matrix $matrix)
    {
        $this->matrix = $matrix;
    }

    public function findGreatestSum()
    {
        $elements = $this->matrix->getElements();
        $elementsSize = sizeof($elements);
        $maxHourglassSum = 0;

        for ($rowIndex = 2; $rowIndex < $elementsSize - 2; $rowIndex++) {
            $elementsRowSize = sizeof($elements[$rowIndex]);

            for ($columnIndex = 2; $columnIndex < $elementsRowSize - 2; $columnIndex++) {
                $currentHourglassSum = $this->calculateTopGlassSum($elements, $rowIndex, $columnIndex);
                $currentHourglassSum += $this->calculateMiddleGlassSum($elements, $rowIndex, $columnIndex);
                $currentHourglassSum += $this->calculateBottomGlassSum($elements, $rowIndex, $columnIndex);

                if ($maxHourglassSum < $currentHourglassSum) {
                    $maxHourglassSum = $currentHourglassSum;
                }
            }
        }

        return $maxHourglassSum;
    }

    private function calculateTopGlassSum($elements, $rowIndex, $columnIndex)
    {
        return
            $elements[$rowIndex - 2][$columnIndex]
            + $elements[$rowIndex - 2][$columnIndex - 1]
            + $elements[$rowIndex - 2][$columnIndex];
    }

    private function calculateMiddleGlassSum($elements, $rowIndex, $columnIndex)
    {
        return $elements[$rowIndex - 1][$columnIndex - 1];
    }

    private function calculateBottomGlassSum($elements, $rowIndex, $columnIndex)
    {
        return
            $elements[$rowIndex][$columnIndex]
            + $elements[$rowIndex][$columnIndex - 1]
            + $elements[$rowIndex][$columnIndex];
    }
}