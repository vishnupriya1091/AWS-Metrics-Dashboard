<?php

function getOutput($userInput){
	
$output =  shell_exec(escapeshellcmd("python pyscripts/get_user_request.py '$userInput'"));
$outputJson =  json_decode($output,true);

echo json_encode($outputJson);	
	
}


function getCSVOutput($userInput){

$output =  shell_exec(escapeshellcmd("python pyscripts/get_user_request.py '$userInput'"));
if(strcmp($output,"CSVFileCreated")){

$filePath = "/var/www/html/output/".$userInput.".csv";
$file = fopen($filePath,"r") or die("Unable to open file!");
echo fread($file,filesize($filePath));
fclose($file);

}else{
	
	echo "File-Read-Error";
	
}
	
}



function getUserInput(){
	
	$getParam = $_GET['display'];
	
	switch($getParam){
		
	case 'instances' : getOutput('getInstances');
	break;
	
	case 'dbInstances' : getOutput('getDBInstances');
	break;
	
	case 'metrics' :	getOutput('getMetrics');
	break;	
	
	case 'dbMetrics' :	getOutput('getDBMetrics');
	break;
	
	case 'AllInstanceNetworkIn' : getCSVOutput('AllInstanceNetworkIn');
	break;
	
	case 'AllInstanceCPUUsage' : getCSVOutput('AllInstanceCPUUsage');
	break;
	
	case 'AllInstanceDBUsage' :	getCSVOutput('AllInstanceDBUsage');
	break;
	
	case 'AllInstanceNetworkPacketsIn' : getCSVOutput('AllInstanceNetworkPacketsIn');
	break;
	
	case 'AllInstanceDBReadThroughput' : getCSVOutput('AllInstanceDBReadThroughput');
	break;
	
	case 'AllInstanceDBWriteThroughput' : getCSVOutput('AllInstanceDBWriteThroughput');
	break;
		
	default : echo "No Parameter Specified";	
			
	}
}

getUserInput();


?>
