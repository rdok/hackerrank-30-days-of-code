<?php
use App\Reader;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */
class HackerRankScriptTest extends PHPUnit_Framework_TestCase
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
}