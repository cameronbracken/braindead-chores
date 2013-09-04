<%inherit file="layout.mako"/>
<%namespace file="macros.mako" import="*"/>

<%block name="content">

${ render_flashes() }

<p>Welcome to Brain dead chores, a reminder service for households who can't remember things. </p>

<p>Please <a href='/login'>login</a> to continue.</p>  

</%block>