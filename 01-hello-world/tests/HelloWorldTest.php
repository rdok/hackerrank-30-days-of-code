<?php
use App\Utilities\HelloWorldUtility;

/**
 * @author Rizart Dokollar <r.dokollari@gmail.com
 * @since 4/18/16
 */
class HelloWorldTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_sees_printed_text()
    {
        $expectedOutput = "Hello, World.\nWelcome to 30 Days of Code!\n";

        $this->expectOutputString($expectedOutput);

        $helloWorldUtility = new HelloWorldUtility();

        $helloWorldUtility->promptUser();
    }
}