<?php
use App\PhoneBook;

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
        $this->assertSame($phoneBookEntry, $phoneBook->getByName('sam'));
    }
}