<?php
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 4/28/16
 */

namespace App;

/**
 * Class Person
 * @package App
 */
class Person
{
    /**
     * @var
     */
    private $age;

    /**
     * Person constructor.
     * @param $initialAge
     */
    public function __construct($initialAge = 0)
    {
        $this->setAge($initialAge);
    }

    /**
     *
     */
    public function yearPasses()
    {
        $this->setAge($this->getAge() + 1);
    }

    /**
     * @return mixed
     */
    public function getAge()
    {
        return $this->age;
    }

    /**
     * @param mixed $age
     * @return string|null
     */
    public function setAge($age)
    {
        if ($age < 0) {
            $this->age = 0;

            return "Age is not valid, setting age to 0.";
        }

        $this->age = $age;

        return null;
    }

    /**
     * @return string
     */
    public function amIOld()
    {
        if ($this->getAge() < 13) {
            return 'You are young.';
        }

        if ($this->getAge() < 18) {
            return 'You are a teenager.';
        }

        return 'You are old.';
    }
}