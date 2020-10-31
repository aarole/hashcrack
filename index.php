<!DOCTYPE html> 
<html> 
      
<head> 
    <title>Web-based hash cracker</title> 
</head> 
  
<body style="text-align:center;"> 
	<h1> 
		CNIT 370 Group 9 Project 
    </h1> 
      
    <h4>
		Identify and crack hashes with rainbow table attacks.
    </h4> 
      
    <?php
		$type="asdf";
		if(array_key_exists('crack_btn', $_POST)) {
			if(strlen($_POST['hash']) == 0){
				header("Refresh:0");
			}	
			else if(ctype_alnum($_POST['hash'])){
				crack_btn();
			}
			else {
				echo "<script language='javascript'>";
				echo 'alert("Incorrect hash format!");';
				echo "</script>";
			}
			
		}
		if(array_key_exists('reset_btn', $_POST)) {
			header("Refresh:0");
		}
		function br(){
			echo "</br>";
			echo "</br>";
		}
		function id(){
			$comm="/var/www/html/id.py " . escapeshellcmd($_POST['hash']);
			exec($comm, $id_out, $id_ret);
			echo "<b>Detected format </b></br>".$id_out[0];
			return $id_out[0];
		}
		function crack(){	
			echo "</br>";
			$type = id();
			br();
			$comm="/var/www/html/crack.py find " . escapeshellcmd($_POST['hash']) . " $type";
			exec($comm, $id_out, $id_ret);
			echo "<b>Plaintext password </b></br>".$id_out[0];
		}	
		function crack_btn() { 
			echo "--------------------------------------------------------------------------";
			echo "</br>";
			echo "<b>Hash provided (wrapped) </b>";
			echo "</br>";
			$prov = wordwrap($_POST['hash'],48,"</br>",true);
			echo "$prov";
			echo "</br>";
			echo "--------------------------------------------------------------------------";
			crack();
			echo "</br>";
			echo "--------------------------------------------------------------------------";
			echo "</br>";
		} 
    ?> 
  
    <form method="post"> 
		<br>
		<input type="text" value="" placeholder="Hash" autocomplete="off" name="hash"/> 
		<input type="submit" name="crack_btn" class="button" value="Crack" />
		<input type="submit" name="reset_btn" class="button" value="Reset" />
	</form>
</body> 
  
</html> 
