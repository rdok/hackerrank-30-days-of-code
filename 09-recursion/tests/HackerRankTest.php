<?php
use App\HackerRank;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */
class HackerRankTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_sees_basic_expected_output()
    {
        $this->expectOutputString(file_get_contents(__DIR__.'/../storage/basic-test-output.txt'));

        $hackerRank = new HackerRank(__DIR__.'/../storage/basic-test-input.txt');

        $hackerRank->printRequirements();
    }
}