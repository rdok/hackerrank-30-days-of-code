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

    public function __construct(array $elements = [])
    {
        $this->setElements($elements);
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

    public function storeElementsFromStringRow($elements)
    {
        $elements = rtrim($elements);

        $elements = array_map('intval', explode(" ", $elements));

        $this->appendRow($elements);
    }

    public function appendRow(array $elementsRow)
    {
        $this->elements[] = $elementsRow;
    }

    public function storeElementsFromString($elements)
    {
        $elementRows = explode("\n", $elements);

        foreach ($elementRows as $row) {
            $this->storeElementsFromStringRow($row);
        }
    }
}