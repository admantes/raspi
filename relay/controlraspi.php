<?php

$relay = $_GET['switch'];  //relay index to control
$mode = $_GET['mode'];	//1 for ON, 0 for OFF

$output = shell_exec("controlrelay.py $relay$mode");
echo $output;
//echo "$relay and $mode";

?>