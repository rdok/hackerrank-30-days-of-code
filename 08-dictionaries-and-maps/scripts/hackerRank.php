<?php
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */
use App\PhoneBook;
use App\Reader;

$reader = new Reader();
$phoneBook = new PhoneBook();
$reader->open(__DIR__.'/../storage/tests.txt');

$phoneBook->addEntriesByReader($reader);

$phoneBook->printEntriesQueryResponseByReader($reader);
