<?php
use App\LoopUtility;

/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 4/28/16
 */
class LoopTest extends PHPUnit_Framework_TestCase
{
    /** @test */
    public function it_returns_even_index_characters()
    {
        $loopUtility = new LoopUtility();

        $this->assertSame('Hce', $loopUtility->getEvenIndexCharacters('Hacker'));
        $this->assertSame('Rn', $loopUtility->getEvenIndexCharacters('Rank'));
    }

    /** @test */
    public function it_returns_odd_index_characters()
    {
        $loopUtility = new LoopUtility();

        $this->assertSame('akr', $loopUtility->getOddIndexCharacters('Hacker'));
        $this->assertSame('ak', $loopUtility->getOddIndexCharacters('Rank'));
    }

    /** @test */
    public function it_returns_even_and_index_characters_as_two_space_separated_strings()
    {
        $loopUtility = new LoopUtility();

        $this->assertSame('Hce akr', $loopUtility->getEvenAndOddCharactersSeparatedByTwoSpaces("Hacker\n"));
        $this->assertSame('Hce akr', $loopUtility->getEvenAndOddCharactersSeparatedByTwoSpaces("Hacker"));
        $this->assertSame('Rn ak', $loopUtility->getEvenAndOddCharactersSeparatedByTwoSpaces('Rank'));

        // Bought tests
        $this->assertSame('oyzpyppytrtrttvxxx vvvtvvxzlzszzqrtuq',
            $loopUtility->getEvenAndOddCharactersSeparatedByTwoSpaces('ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq'));

        $this->assertSame('hlm ot',
            $loopUtility->getEvenAndOddCharactersSeparatedByTwoSpaces('holtm'));

        $this->assertSame('uzrmzyypj vxuutqvni',
            $loopUtility->getEvenAndOddCharactersSeparatedByTwoSpaces('uvzxrumuztyqyvpnji'));

        $this->assertSame('trzzwsqszuourwntvsqyzxlruxp muxuokyxtvsysrmxzrwtrptwsuw',
            $loopUtility->getEvenAndOddCharactersSeparatedByTwoSpaces('tmruzxzuwoskqysxztuvosuyrswrnmtxvzsrqwytzrxpltrwusxupw'));

        $this->assertSame('wswuuuyrxsyvquykwyuqvpoqmvxwpsnrtrpuuvzuvpwyvuwsw xtxzyvzsyxuyxxsqsqmrovwunrpqwrvzxxvxnyvpuovzzzvrv',
            $loopUtility->getEvenAndOddCharactersSeparatedByTwoSpaces('wxstwxuzuyuvyzrsxysxyuvyqxuxyskqwsyqumqrvopvowqumnvrxpwqpwsrnvrztxrxpvuxunvyzvupvupowvyzvzuzwvsrwv'));

        $this->assertSame('yzrsrlwmpvwxpq rxxktpptxorrx',
            $loopUtility->getEvenAndOddCharactersSeparatedByTwoSpaces('yrzxrxskrtlpwpmtpxvowrxrpxq'));

        $this->assertSame('pymutopvwl rutnmvwosj',
            $loopUtility->getEvenAndOddCharactersSeparatedByTwoSpaces('pryumtuntmovpwvowslj'));

        $this->assertSame('nslxtutnrsyxyqqxs okrryxmuzrutwwpt',
            $loopUtility->getEvenAndOddCharactersSeparatedByTwoSpaces('nosklrxrtyuxtmnurzsryuxtywqwqpxts'));

        $this->assertSame('fpzvwrvuqzyomxxvypzpuqtwyyznxyptsotuquy msyqxtpwsvvtssuzvwrmxwsvttsuurvyquzrxr',
            $loopUtility->getEvenAndOddCharactersSeparatedByTwoSpaces('fmpszyvqwxrtvpuwqszvyvotmsxsxuvzyvpwzrpmuxqwtswvytytzsnuxuyrpvtysqoutzurqxury'));

        $this->assertSame('jmxwxy kszrz',
            $loopUtility->getEvenAndOddCharactersSeparatedByTwoSpaces('jkmsxzwrxzy'));
    }
}