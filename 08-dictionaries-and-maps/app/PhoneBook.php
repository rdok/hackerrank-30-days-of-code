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

    public function getEntryByName($name)
    {
        foreach ($this->entries as $entry) {
            if ($entry['name'] === $name) {
                return $entry;
            }
        }

        return false;
    }

    /**
     * The reader must point to the row saying the total entries.
     * Next, for the total number of entries, the reader must able to read name/phone pairs.
     *
     * @param $reader
     */
    function addEntriesByReader(Reader $reader)
    {
        $totalEntries = $reader->readNextLine();

        for ($index = 0; $index < $totalEntries; $index++) {
            $rawEntry = explode(' ', $reader->readNextLine());

            $entry = ['name' => $rawEntry[0], 'phoneNumber' => $rawEntry[1]];

            $this->add($entry);
        }
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
}