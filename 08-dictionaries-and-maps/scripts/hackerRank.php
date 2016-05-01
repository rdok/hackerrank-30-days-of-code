<?php
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */
use App\PhoneBook;
use App\Reader;

$reader = new Reader();
$phoneBook = new PhoneBook();
$reader->open('php://stdin');

$totalEntries = $reader->readNextLine();

storePhoneBookEntries($totalEntries, $reader, $phoneBook);

while (($entryName = $reader->readNextLine()) !== false) {
    if (($entry = $phoneBook->getEntryByName($entryName)) !== false) {
        echo $entry;
        continue;
    }

    echo 'Not found';
}

/////////////// end script commands /////////////////////////
//////////////// script functions ///////////////////////////////////
/**
 * @param $totalEntries
 * @param $reader
 * @param $phoneBook
 */
function storePhoneBookEntries($totalEntries, Reader $reader, PhoneBook $phoneBook)
{
    for ($index = 0; $index < $totalEntries; $index++) {
        $rawEntry = explode($reader->readNextLine(), ' ');

        $entry = ['name' => $rawEntry[0], 'phoneNumber' => $rawEntry[1]];

        $phoneBook->add($entry);
    }
}
