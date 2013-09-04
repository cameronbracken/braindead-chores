<!DOCTYPE html>
<html>
  <head>
      <title>Braindead Chores</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <!-- Bootstrap -->
      <link href="${ url_for('static', filename='bootstrap/css/bootstrap.min.css') }" rel="stylesheet" media="screen">
      <link href="${ url_for('static', filename='bootstrap/css/bootstrap-responsive.min.css') }" rel="stylesheet" media="screen">
      <link href="${ url_for('static', filename='css/styles.css') }" rel="stylesheet">

      <script type="text/javascript" src="${ url_for('static', filename='js/jquery.min.js') }"></script>

      <!-- bootstrap widget theme -->
      <link href="${ url_for('static', filename='css/theme.bootstrap.css') }" rel="stylesheet">

  </head>
  <body>
    <h1>Braindead Chores</h1>
    <hr>

    <ul class="nav nav-tabs" id="tabs" data-tabs="tabs">
      <li class="active"><a data-toggle="tab" href="#home">Home</a></li>
      <li>               <a data-toggle="tab" href="#about">About</a></li>
      % if security.current_user.is_authenticated():
      <li>               <a data-toggle="tab" href="#account">Account</a></li>
      % endif 
    </ul>

    <div class="tab-content">
      <div class="tab-pane fade active in" id="home"><%block name="content"/></div>
      <div class="tab-pane fade" id="about"><%include file="about.mako"/></div>
      % if security.current_user.is_authenticated():
      <div class="tab-pane fade" id="about"><%block name="account"/></div>
      % endif 
    </div>

    <script type="text/javascript" src="${ url_for('static', filename='bootstrap/js/bootstrap.min.js') }"></script>
  </body>
</html>
