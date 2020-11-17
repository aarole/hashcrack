<!DOCTYPE html> 
<html> 

	<head> 
		<title>Hashcrack - Crack</title> 
		<link rel="stylesheet" type="text/css" href="assets/style.css">
	</head>
	<body style="text-align: center;">
		<div id="header">
			<img src="logo.png" width="240px" height="240px" style="vertical-align: middle;"><br>
			
			<a href="/"><h2>Home</h2></a>&emsp;&emsp;&emsp;&emsp;
			<h2><u>Crack</u></h2>&emsp;&emsp;&emsp;&emsp;
			<a href="/about.html"><h2>About</h2></a><br><br>
		</div>
		<br>
		<?php
			if(array_key_exists('crack_btn', $_POST)) {
				if(strlen($_POST['hash']) == 0){
					header("Refresh:0");
				}	
				else if(ctype_alnum($_POST['hash'])){
					$type=id();
					$plaintext=crack($type);
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
			function id(){
				$comm="./id.py " . escapeshellcmd($_POST['hash']);
				exec($comm, $id_out, $id_ret);
				return $id_out[0];
			}
			function crack($type){
				$comm="./crack.py find " . escapeshellcmd($_POST['hash']) . " $type";
				exec($comm, $id_out, $id_ret);
				return $id_out[0];
			}
		?> 

		<form method="post"> 
			<br>
			<input type="text" value="" placeholder="Hash" autocomplete="off" name="hash" size="44"/> <br><br>
			<input type="submit" name="crack_btn" class="button" value="Crack" />
			<input type="submit" name="reset_btn" class="button" value="Reset" />
		</form>
		<p><p>
		<form>
			Identified algorithm: <input type="text" value="<?php echo $type;?>" name="id" readonly /> <p>
			Plaintext: &emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;<input type="text" value="<?php echo $plaintext;?>" name="pass" readonly /> 
		</form>	
</body> 
</html> 
