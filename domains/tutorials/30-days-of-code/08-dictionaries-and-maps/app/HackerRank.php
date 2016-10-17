<?php namespace App;
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */

class HackerRank
{
    private $phoneBook;
    private $reader;

    public function __construct($handler)
    {
        $this->reader = new Reader();
        $this->reader->open($handler);

        $this->phoneBook = new PhoneBook();
        $this->phoneBook->addEntriesByReader($this->reader);
    }

    public function printRequirements()
    {
        $this->phoneBook->printEntriesQueryResponseByReader($this->reader);
    }
}


