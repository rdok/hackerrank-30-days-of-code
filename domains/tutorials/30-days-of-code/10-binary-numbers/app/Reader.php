<?php
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */

namespace App;

/**
 * Class Reader
 * @package App
 */
class Reader
{
    /**
     * @var
     */
    private $handler;

    public function __construct($stream)
    {
        $this->open($stream);
    }

    /**
     * @param $stream
     * @return mixed
     */
    public function open($stream)
    {
        $this->setHandler(fopen($stream, 'r'));
    }

    public function readNextLine()
    {
        return fgets($this->getHandler());
    }

    /**
     * @return mixed
     */
    public function getHandler()
    {
        return $this->handler;
    }

    /**
     * @param mixed $handler
     */
    public function setHandler($handler)
    {
        $this->handler = $handler;
    }

    public function close()
    {
        fclose($this->getHandler());
    }
}