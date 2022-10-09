<?php

$datas = file_get_contents("php://input");

$socket0 = socket_create(AF_INET,SOCK_STREAM,SOL_TCP);

socket_connect($socket0,"127.0.0.1",8081);

socket_write($socket0,$datas,strlen($datas));

$datar = socket_read($socket0,50);

socket_close($socket0);

header("Content_Type:text/plain");

echo $datar;
?>
