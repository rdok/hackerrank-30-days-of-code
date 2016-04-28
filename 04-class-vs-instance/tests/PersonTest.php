<?php
use App\Person;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 4/28/16
 */
class PersonTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_sets_incorrect_age()
    {
        $incorrectAge = -1;
        $person = new Person();

        $this->assertSame('Age is not valid, setting age to 0.', $person->setAge($incorrectAge));

        $this->assertSame(0, $person->getAge());
    }
}