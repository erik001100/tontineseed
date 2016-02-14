<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="/static/images/favicon.ico">

    <title>{{title or 'No title'}}</title>

    <!-- Bootstrap core CSS -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/static/css/starter-template.css" rel="stylesheet">
    
  </head>
  <body>
    <div class="site-wrapper"> 
     <div class="site-wrapper-inner">
      <div class="cover-container">
        <div class="masthead clearfix">
          <div class="inner">
            <img  id="navLogo" class="masthead-brand img-responsive" src="/static/images/logo-text.png" alt="Bitster">
            <nav>
              <ul class="nav masthead-nav">
                <li class=""><a href="/">Home</a></li>
                <li class=""><a href="/sendtorrent">Upload</a></li>
                <li class=""><a href="/play">Play</a></li>
                <li class=""><a href="/status">Status</a></li>
              </ul>
            </nav>
          </div>
        </div>       
        {{!base}}
        <div class="mastfoot">
          <div class="inner">
            <p>We winnin </p>
          </div>
        </div>
      </div>
    </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="/static/js/bootstrap.min.js"></script>

  </body>
</html>

