<?php
use App\Reader;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */
class ReaderTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_reads_line()
    {
        $reader = new Reader(__DIR__.'/../storage/basic-test-input.txt');

        $this->assertSame("1\n", $reader->readNextLine());
        $this->assertSame("2\n", $reader->readNextLine());
    }
}