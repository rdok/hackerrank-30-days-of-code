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

    /**
     * @param $stream
     * @return mixed
     */
    public function open($stream)
    {
        $this->setHandler(fopen($stream, 'r'));
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
}