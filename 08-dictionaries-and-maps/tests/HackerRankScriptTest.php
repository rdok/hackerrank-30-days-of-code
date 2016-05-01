<?php

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */
class HackerRankScriptTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_sees_expected_output()
    {
        $this->expectOutputString("sam=99912222\nNot found\nharry=12299933");

        include __DIR__.'/../scripts/hackerRank.php';
    }
}