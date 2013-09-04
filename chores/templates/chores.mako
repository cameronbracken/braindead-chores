<%inherit file="layout.mako"/>

<%block name="content">

<p>You made it! Lets get un-braindead.</p>

<p><a href='${url_for_security("logout")}'>Logout</a></p>

</%block>

<%include file="account.mako"/>
