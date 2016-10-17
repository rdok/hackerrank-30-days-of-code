<?php
use App\ConditionalActioner;

/**
 * @author Rizart Dokollar <r.dokollari@gmail.com
 * @since 4/21/16
 */
class ConditionalActionerTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_prints_weird_for_odd_input()
    {
        $conditionalActioner = new ConditionalActioner();

        $this->assertSame('Weird', $conditionalActioner->check(3));
    }

    /** @test */
    public function it_prints_not_weird_for_even_and_inclusive_2_to_5_range()
    {
        $conditionalActioner = new ConditionalActioner();

        $this->assertSame('Not Weird', $conditionalActioner->check(2));
        $this->assertSame('Not Weird', $conditionalActioner->check(4));
    }

    /** @test */
    public function it_prints_weird_for_even_and_inclusive_6_to_20_range()
    {
        $conditionalActioner = new ConditionalActioner();

        $this->assertSame('Weird', $conditionalActioner->check(6));
        $this->assertSame('Weird', $conditionalActioner->check(18));
        $this->assertSame('Weird', $conditionalActioner->check(20));
    }

    /** @test */
    public function it_prints_not_weird_for_even_and_greater_than_20_input()
    {
        $conditionalActioner = new ConditionalActioner();

        $this->assertSame('Not Weird', $conditionalActioner->check(24));
    }
}