<%block name="content">

<p>${security.current_user.email}</p>

<p><a href='${url_for_security("logout")}'>Logout</a></p>

</%block>