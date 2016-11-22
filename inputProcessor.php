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
       <?php 
      
       $date = date_create_from_format("j F, Y",$_POST['date']);
       $dateFormatted = date_format($date,"n/j/y");
       $input = $dateFormatted."#".$_POST['speaker']."#".$_POST['content'];
       file_put_contents("webInput.csv", $input);
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

