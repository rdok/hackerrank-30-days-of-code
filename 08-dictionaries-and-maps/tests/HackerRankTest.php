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
        $this->expectOutputString("sam=99912222\nNot found\nharry=12299933\n");

        $hackerRank = new HackerRank(__DIR__.'/../storage/tests.txt');

        $hackerRank->printRequirements();
    }

    /** @test */
    public function it_passes_testcase_1()
    {
        $this->expectOutputString(file_get_contents(__DIR__.'/../storage/output01.txt'));

        $hackerRank = new HackerRank(__DIR__.'/../storage/input01.txt');

        $hackerRank->printRequirements();
    }
}