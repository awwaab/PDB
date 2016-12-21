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

    <body class="categorical grey lighten-3">
        <a href="index.html">BACK</a>
      <!--Import jQuery before materialize.js-->

      <div class="container white-box">
        
        <div class="row">
          <h1 class ="heads-topics center-align">Security</h1>
          <h3 class ="heads-topics center-align">Everything they said about the security</h3>
           
        </div>
        <div class="row">
        <?php 
          $myfile = fopen("result.csv", "r") or die("Unable to open file!");
          $file =  fread($myfile,filesize("result.csv"));
          
          $entityLists = explode("\n", $file); //9/26/16#9#Clinton#So let's have paid family leave, earned sick days#Economic
          
         //for Hillay clinton

          echo "<div class = 'col s6-mod content red darken-3 flexible'>";
          echo "<h5 class = 'center'> HILLARY CLINTON </h5>";

          $countClinton = 0;

          foreach ($entityLists as $entity) {
             
             $entitySplitted = explode("#", $entity);
             $date = $entitySplitted[0];
             $line = $entitySplitted[1];

             $speaker = $entitySplitted[2];
             $content = $entitySplitted[3];
             $tag = trim($entitySplitted[4]);
            
            if ($speaker == "Clinton" and ($tag == "2.0" or $tag == "5.0")  and $countClinton%2 ==0){
                 echo "<p class='amber-text text-lighten-3'> $content </p>";
                 $countClinton += 1;
               }
             elseif ($speaker == "Clinton" and ($tag == "2.0" or $tag == "5.0")  and $countClinton%2 ==1){
                 echo "<p> $content </p>";
                 $countClinton += 1;
             }
              
           
          }
          echo "</div>";

          //for donald trump
          echo "<div class = 'col s6-mod content red darken-3 flexible'>";
            echo "<h5 class = 'center'> DONALD TRUMP </h5>";
            $countTrump = 0;

            foreach ($entityLists as $entity) {
             $entitySplitted = explode("#", $entity);
             $date = $entitySplitted[0];
             $line = $entitySplitted[1];

             $speaker = $entitySplitted[2];
             $content = $entitySplitted[3];
             $tag = trim($entitySplitted[4]);
            
             
             if ($speaker == "Trump" and ($tag == "2.0" or $tag == "5.0") and $countTrump%2 ==0){
                 echo "<p class='amber-text text-lighten-3'> $content </p>";
                 $countTrump += 1;
               }
             elseif ($speaker == "Trump" and ($tag == "2.0" or $tag == "5.0") and $countTrump%2 ==1){
                 echo "<p> $content </p>";
                 $countTrump += 1;
             }
              
          }

          echo "</div>";

          fclose($myfile);

        ?>
        </div>
       
      
      <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
      <script type="text/javascript" src="js/materialize.min.js"></script>
    </body>
  </html>