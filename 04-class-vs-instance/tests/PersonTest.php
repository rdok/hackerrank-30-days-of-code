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
    public function it_returns_whether_a_person_is_young_teenager_or_old()
    {
        $person = new Person();
        $this->assertSame(0, $person->getAge());

        $this->assertSame('You are young.', $person->amIOld());
        $person->setAge(7);
        $this->assertSame('You are young.', $person->amIOld());
        $person->setAge(12);
        $this->assertSame('You are young.', $person->amIOld());

        $person->setAge(13);
        $this->assertSame('You are a teenager.', $person->amIOld());
        $person->setAge(15);
        $this->assertSame('You are a teenager.', $person->amIOld());
        $person->setAge(17);
        $this->assertSame('You are a teenager.', $person->amIOld());

        $person->setAge(18);
        $this->assertSame('You are old.', $person->amIOld());
        $person->setAge(25);
        $this->assertSame('You are old.', $person->amIOld());
        $person->setAge(75);
        $this->assertSame('You are old.', $person->amIOld());
    }
}