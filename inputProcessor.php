 <!DOCTYPE html>
  <html>
    <head>
      <!--Import Google Icon Font-->
      <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <!--Import materialize.css-->
      <link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>
      <link type="text/css" rel="stylesheet" href="css/custom.css"  media="screen,projection"/>

      <!--Let browser know website is optimized for mobile-->
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    </head>

    <body class="grey lighten-3" >
      <!--Import jQuery before materialize.js-->

      <div class="container ">
        
        <div class="row title">
          <h1 class ="heads center-align">United States Presidential Debate</h1>
        </div>
       <?php

       $date = date_create_from_format("j F, Y",$_POST['date']);
       $dateFormatted = date_format($date,"n/j/y");
       $input = $dateFormatted."#1#".$_POST['speaker']."#".$_POST['content']."#1.0 "."\n";
       file_put_contents("input-web.txt", $input, FILE_APPEND);

       //remove the existing file from HDFS, add the new file and execute the classifier.
       // echo shell_exec("HADOOP_USER_NAME=hdfs hdfs dfs -rm /input-web.txt 2>&1");
       // echo shell_exec("HADOOP_USER_NAME=hdfs hdfs dfs -put /var/www/html/PDB/input-web.txt / 2>&1");
       // echo shell_exec("spark-submit --packages com.databricks:spark-csv_2.10:1.2.0 classify-dt-v5.py --master yarn-client 2>&1");
        ?>

       <div class = "row">
       	 <h3 class =" center-align">Thanks you for your submission</h3>
       	 <h3 class =" center-align">Working on the category, please wait.....</h3>
       </div>
      </div>
      
      <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
      <script type="text/javascript" src="js/materialize.min.js"></script>
    </body>
  </html>

