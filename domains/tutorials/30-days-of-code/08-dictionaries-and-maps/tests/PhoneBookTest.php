<?php
use App\PhoneBook;
use App\Reader;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 4/28/16
 */
class PhoneBookTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_appends_new_entry()
    {
        $phoneBook = new PhoneBook();
        $phoneBookEntry = ['name' => 'sam', 'phoneNumber' => 99912222];

        $this->assertSame(0, $phoneBook->getTotalEntries());

        $this->assertTrue($phoneBook->add($phoneBookEntry));

        $this->assertSame(1, $phoneBook->getTotalEntries());
        $this->assertSame($phoneBookEntry, $phoneBook->getEntryByName('sam'));
    }

    /** @test */
    public function it_stores_entries_from_fgets()
    {
        $phoneBook = new PhoneBook();
        $reader = new Reader();
        $filePath = __DIR__.'/../storage/tests.txt';
        $reader->open($filePath);

        $this->assertSame(0, $phoneBook->getTotalEntries());

        $phoneBook->addEntriesByReader($reader);

        $this->assertSame(3, $phoneBook->getTotalEntries());
    }

    /** @test */
    public function it_prints_entries_query_response_from_reader()
    {
        $phoneBook = new PhoneBook();
        $reader = new Reader();
        $filePath = __DIR__.'/../storage/tests.txt';
        $reader->open($filePath);

        $phoneBook->addEntriesByReader($reader);
        $phoneBook->printEntriesQueryResponseByReader($reader);

        $this->expectOutputString("sam=99912222\nNot found\nharry=12299933\n");
    }
}