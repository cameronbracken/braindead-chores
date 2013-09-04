<%inherit file="layout.mako"/>
<%namespace file="macros.mako" import="*"/>

<%block name="content">

${ render_flashes() }
${ render_errors(form.errors) }

<p>
% if action == 'register':
  Please create a new account or <a href="/login">login</a>
% else:
  Please login to continue or <a href="/register">register</a>
% endif
</p>

<form method="POST" action="${action}" class='form form-horizontal'>
    ${ render_form(form) }

    <div class="controls">
        <button type="submit" class="btn">Submit</button>
    </div>
</form>

</%block>