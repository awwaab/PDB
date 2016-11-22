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
            <form class="col s12" action="inputProcessor.php" method="post">
              <div class="row">
                <div class="input-field col s6 offset-s3">
                  <input type="date" class="datepicker" id="date" required="true" name="date" >
                  <label for="date">Date</label>
                </div>
              </div>
              <div class="row">
                <div class="input-field col s6 offset-s3">
                  <input id="speaker" type="text" class="validate" required="true" name="speaker">
                  <label for="speaker">Speaker</label>
                </div>
              </div>
              <div class="row">
                <div class="input-field col s6 offset-s3">
                  <textarea id="content" class="materialize-textarea" required="true" name = "content"></textarea>
                  <label for="content">Content</label>
                </div>
              </div>
              <div class="row">
                <div class="input-field col s6 offset-s3">
                  <input class="btn waves-effect waves-light col s12" type="submit" name="action"> </input>
                </div>
              </div>
            </form>
          
          </div>
      </div>
      
      <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
      <script type="text/javascript" src="js/materialize.min.js"></script>
    </body>
  </html>


<script type="text/javascript">
   $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 5 // Creates a dropdown of 15 years to control year
  });
</script>