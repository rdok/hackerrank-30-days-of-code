<?php
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/2/16
 */

namespace App;

/**
 * Class Matrix. See https://en.wikipedia.org/wiki/Matrix_(mathematics)
 * @package App
 */
class Matrix
{
    private $elements;

    public function __construct(array $numbers = [])
    {
        $this->setElements($numbers);
    }

    public function getElements()
    {
        return $this->elements;
    }

    /**
     * @param array $elements
     */
    public function setElements($elements)
    {
        $this->elements = $elements;
    }

    public function storeElementsFromString($elements)
    {
        $rows = explode("\n", $elements);

        foreach ($rows as $row) {
            $elementsRow = str_split($row);

            $this->appendRow($elementsRow);
        }
    }

    public function appendRow(array $elementsRow)
    {
        $this->elements[] = $elementsRow;
    }
}