<?php
// http://wwww.xxx.xxx/add.php?mac=5CCF7F23CDB9&masse=123600&temp_capteur=25.25&hygro_capteur=45&date=2016-8-13&heure=13:31:13&nour=1&vbat=11.55&send_counter=0

   	include("connect.php");
   	
   	$link=Connection();

   	
	// recherche du numero de colonie depuis l'adresse mac de l'emetteur
	$mac=$_GET["mac"];
	$query="SELECT PK_IdCapteur,typeCapteur,FK_IdColonie FROM `capteur` WHERE `adresse` =\"$mac\"";
	$result=mysqli_query($link,$query) or die(mysqli_error($link)." Q=".$query);
	$row_cnt = mysqli_num_rows($result);
	if ( $row_cnt ) {
	    $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
	    $PK_IdCapteur = $row["PK_IdCapteur"];
	    $FK_IdColonie = $row["FK_IdColonie"];
	    $typeCapteur = $row["typeCapteur"];
	    mysqli_free_result($result);
	    
	    // insertion des donnees 
	    switch ($typeCapteur)  {
	      case 'E' : // table mesure_ext =========================================
		$nourrissement = $_GET["nour"];
		$masse = $_GET["masse"];
		$date = $_GET["date"]." ".$_GET["heure"];
		// recherche des valeurs des dernières mesures
		$query="SELECT * FROM `mesure_ext` WHERE `FK_IdColonie` = ".$FK_IdColonie." ORDER BY `date_enr` ASC";
		$result=mysqli_query($link,$query) or die(mysqli_error($link)." Q=".$query);
		if($result!==FALSE){
		    while($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
			  $oldtare = $row["tare"];
			  $oldmasse = $row["masse"];
			  $olddate = $row["timestamp"];
		    }
		} else {
		    $oldtare = 0;
		}
		mysqli_free_result($result);	    
		// insertion des donnees si variation significative
		//$interval = abs(time() - strtotime($olddate)); // interval en secondes 
		//if( abs( $masse - $oldmasse ) > 50 || $nourrissement || $interval > 1000 ) {
		    if( ($nourrissement > 0) && ($nourrissement < 5) ) {
			if( $nourrissement == 4 ) // chgt de tare 
			  $query = "INSERT INTO `mesure_ext` (`masse`,`tare`,`temp_capteur`,`hygro_capteur`,`date`,`vbat`,`send_counter`,`FK_IdColonie`,`FK_IdCapteur`) 
			  VALUES ('".$masse."',".$oldtare."+".$masse."-".$oldmasse.",'".$_GET["temp_capteur"]."','".$_GET["hygro_capteur"]."',
			  '".$_GET["date"]." ".$_GET["heure"]."','".$_GET["vbat"]."','".$_GET["counter"]."',".$FK_IdColonie.",".$PK_IdCapteur.")"; 
			else  // sirop ou candy
			  $query = "INSERT INTO `mesure_ext` (`masse`,`tare`,`temp_capteur`,`hygro_capteur`,`date`,
			  `nourriss_t`, `nourriss_q`, `vbat`,`send_counter`, `FK_IdColonie`, `FK_IdCapteur`) 
			  VALUES ('".$masse."','".$oldtare."','".$_GET["temp_capteur"]."','".$_GET["hygro_capteur"]."','".$_GET["date"]." ".$_GET["heure"]."',
			  '".$nourrissement."',".$masse."-".$oldmasse.",'".$_GET["vbat"]."','".$_GET["counter"]."',".$FK_IdColonie.",".$PK_IdCapteur.")"; 
		    } else {
			$query = "INSERT INTO `mesure_ext` (`masse`, `tare`, `temp_capteur`,`hygro_capteur`, `date`, `vbat`,`send_counter`, `FK_IdColonie`, `FK_IdCapteur`) 
			  VALUES ('".$masse."','".$oldtare."','".$_GET["temp_capteur"]."','".$_GET["hygro_capteur"]."','".$_GET["date"]." ".$_GET["heure"]."','"
			  .$_GET["vbat"]."','".$_GET["counter"]."',".$FK_IdColonie.",".$PK_IdCapteur.")"; 
		    }
		    $result=mysqli_query($link,$query) or die(mysqli_error($link)." Q=".$query);
		//}
		break;
	      case 'I' : // table mesure_int =========================================
		break; 
	      case 'M' : // table meteo      =========================================
		break;
	    }
	    if ( $result==FALSE )
	      echo "erreur : $query";
	    else
	      echo "INSERT_DONE : $query";
   	} else {
	    echo "Pas de capteur : $query";
   	}
	mysqli_close($link);

   	//header("Location: index.php"); /* Redirection du navigateur */
?>
