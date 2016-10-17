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

        $this->expectOutputString("Age is not valid, setting age to 0.\n");

        $person->setAge($incorrectAge);

        $this->assertSame(0, $person->getAge());
    }

    /** @test */
    public function it_increases_age_each_year()
    {
        $person = new Person();
        $this->assertSame(0, $person->getAge());

        $person->yearPasses();
        $this->assertSame(1, $person->getAge());

        $person->yearPasses();
        $this->assertSame(2, $person->getAge());
    }

    /** @test */
    public function it_prints_young_person()
    {
        $person = new Person();
        $this->assertSame(0, $person->getAge());

        $person->setAge(0);
        $person->amIOld();
        $person->setAge(7);
        $person->amIOld();
        $person->setAge(12);
        $person->amIOld();
        $this->expectOutputString("You are young.\nYou are young.\nYou are young.\n");
    }

    /** @test */
    public function it_prints_teenager_person()
    {
        $person = new Person();
        $this->assertSame(0, $person->getAge());

        $person->setAge(13);
        $person->amIOld();
        $person->setAge(15);
        $person->amIOld();
        $person->setAge(17);
        $person->amIOld();
        $this->expectOutputString("You are a teenager.\nYou are a teenager.\nYou are a teenager.\n");
    }

    /** @test */
    public function it_prints_old_person()
    {
        $person = new Person();
        $this->assertSame(0, $person->getAge());

        $person->setAge(18);
        $person->amIOld();
        $person->setAge(25);
        $person->amIOld();
        $person->setAge(105);
        $person->amIOld();
        $this->expectOutputString("You are old.\nYou are old.\nYou are old.\n");
    }
}