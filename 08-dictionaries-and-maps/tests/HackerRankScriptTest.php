<?php

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */
class HackerRankScriptTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_reads_test_input_from_file()
    {
        $inputs = file_get_contents(__DIR__ . '/../storage/tests.txt');
    }
}