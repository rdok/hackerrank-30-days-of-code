<?php
/**
 * @author Rizart Dokollari <r.dokollari@gmail.com>
 * @since 5/1/16
 */
use App\Reader;

$reader = new Reader();
$reader->open('php://stdin');

$totalEntries = $reader->read();