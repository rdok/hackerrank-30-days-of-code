<?php namespace App\Utilities;

/**
 * @author Rizart Dokollar <r.dokollari@gmail.com
 * @since 4/18/16
 */
class HelloWorldUtility
{
    public function promptUser()
    {
        // User must enter: Welcome to 30 Days of Code!

        $userInput = fopen("php://stdin", "r");

        $inputString = fgets($userInput);

        print("Hello, World.\n$inputString");

        fclose($userInput);
    }
}