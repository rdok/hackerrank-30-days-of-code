<?php
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */

namespace App;

class PhoneBook
{
    private $entries;

    /**
     * PhoneBook constructor.
     */
    public function __construct()
    {
        $this->entries = [];
    }

    public function getTotalEntries()
    {
        return sizeof($this->entries);
    }

    /**
     * Add a new entry. The entries must be already validated:
     *  - Contains key with 'name', at least one alphanumeric character.
     *  - Contains key with 'phoneNumber' of 9 digits
     *
     * @param $phoneBookEntry
     * @return bool
     */
    public function add(array $phoneBookEntry)
    {
        array_push($this->entries, $phoneBookEntry);

        return true;
    }

    public function getByName($name)
    {
        foreach ($this->entries as $entry) {
            if ($entry['name'] === $name) {
                return $entry;
            }
        }

        return null;
    }
}