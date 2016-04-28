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
            echo "Age is not valid, setting age to 0.\n";

            $this->age = 0;

            return;
        }

        $this->age = $age;
    }

    /**
     * @return string
     */
    public function amIOld()
    {
        if ($this->getAge() < 13) {
            echo "You are young.\n";

            return;
        }

        if ($this->getAge() < 18) {
            echo "You are a teenager.\n";

            return;
        }

        echo "You are old.\n";
    }
}