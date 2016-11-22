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

    <body class="light-blue darken-4">
      <!--Import jQuery before materialize.js-->

      <div class="container ">
        
        <div class="row title">
          <h1 class ="heads center-align">United States Presidential Debate</h1>
        </div>
        <div class="row">
        <?php 
          $myfile = fopen("Text.csv", "r") or die("Unable to open file!");
          $file =  fread($myfile,filesize("Text.csv"));
          
          $entityLists = explode("\n", $file); //9/26/16#9#Clinton#So let's have paid family leave, earned sick days#Economic
          echo "<div class = 'col s6 content'>";
          foreach ($entityLists as $entity) {
             
             $entitySplitted = explode("#", $entity);
             $date = $entitySplitted[0];
             $line = $entitySplitted[1];

             $speaker = $entitySplitted[2];
             $content = $entitySplitted[3];
             $tag = trim($entitySplitted[4]);
            
             if ($speaker == "Clinton" and $tag == "Economic")
                  echo "<p> $content </p>";
              
           
          }
          echo "</div>";
          echo "<div class = 'col s6 content'>";
            foreach ($entityLists as $entity) {
             
             $entitySplitted = explode("#", $entity);
             $date = $entitySplitted[0];
             $line = $entitySplitted[1];

             $speaker = $entitySplitted[2];
             $content = $entitySplitted[3];
             $tag = trim($entitySplitted[4]);
            
             
             if ($speaker == "Trump" and $tag == "Economic")
                echo "<p> $content </p>";
          }

          echo "</div>";
          fclose($myfile);

        ?>
        </div>
        <div class = "col s6">
        </div>

        <div class = "col s6">
        </div>
       
      
      <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
      <script type="text/javascript" src="js/materialize.min.js"></script>
    </body>
  </html>