<?php
use App\LoopUtility;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 4/28/16
 */
class LoopTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_prints_even_index_characters()
    {
        $loopUtility = new LoopUtility();

        $this->assertSame('Hce', $loopUtility->getEvenIndexCharacters('Hacker'));
    }
}