<?php
use App\Reader;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */
class ReaderTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_opens_file()
    {
        $reader = new Reader();

        $expectedPath = __DIR__ . '/../storage/tests.txt';

        $this->assertNull($reader->getHandler());
        $reader->open($expectedPath);
        $this->assertNotNull($reader->getHandler());

    }

    /** @test */
    public function it_opens_stdir()
    {
        $reader = new Reader();
        $expectedPath = 'php://stdin';

        $this->assertNull($reader->getHandler());
        $reader->open($expectedPath);
        $this->assertNotNull($reader->getHandler());
    }

    /** @test */
    public function it_reads_line()
    {
        $reader = new Reader();
        $reader->open(__DIR__ . '/../storage/tests.txt');

        $this->assertSame("3\n", $reader->readNextLine());
        $this->assertSame("sam 99912222\n", $reader->readNextLine());
        $this->assertSame("tom 11122222\n", $reader->readNextLine());
        $this->assertSame("harry 12299933\n", $reader->readNextLine());
        $this->assertSame("sam\n", $reader->readNextLine());
        $this->assertSame("edward\n", $reader->readNextLine());
        $this->assertSame("harry", $reader->readNextLine());
    }
}