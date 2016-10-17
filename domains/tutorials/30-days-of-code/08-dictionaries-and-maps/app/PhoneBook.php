<?php
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */

namespace App;

/**
 * Class PhoneBook
 * @package App
 */
class PhoneBook
{
    /**
     * @var array
     */
    private $entries;

    /**
     * PhoneBook constructor.
     */
    public function __construct()
    {
        $this->entries = [];
    }

    /**
     * @return mixed
     */
    public function getTotalEntries()
    {
        return sizeof($this->entries);
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

            $entry = ['name' => $rawEntry[0], 'phoneNumber' => rtrim($rawEntry[1])];

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
        $this->entries[$phoneBookEntry['name']] = $phoneBookEntry;

        return true;
    }

    /**
     * @param Reader $reader
     */
    public function printEntriesQueryResponseByReader(Reader $reader)
    {
        $output = '';

        while (($entryName = $reader->readNextLine()) !== false) {

            if (($entry = $this->getEntryByName(rtrim($entryName))) !== false) {
                $output .= $entry['name'].'='.$entry['phoneNumber']."\n";
                continue;
            }

            $output .= "Not found\n";
        }

        echo $output;

        $reader->close();
    }

    /**
     * Entry name must be already validated/trimed.
     *
     * @param $name
     * @return bool|mixed
     */
    public function getEntryByName($name)
    {
        if (array_key_exists($name, $this->entries)) {
            return $this->entries[$name];
        }

        return false;
    }

    /**
     * @return array
     */
    public function getEntries()
    {
        return $this->entries;
    }
}