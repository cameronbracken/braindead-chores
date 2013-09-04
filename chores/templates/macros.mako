<%def name="bootstrap_alert_box(messages, alert_type)">
  % for message in messages:
    <div class="alert alert-error">
      <button type="button" class="close" data-dismiss="alert">&times;</button>
      <strong>${message}</strong> 
    </div>
  %endfor
</%def>

<%def name="render_form(form)">
  ${ form.hidden_tag() if form.hidden_tag else ''}
    % for field in form:
      % if field.type != 'HiddenField' and field.type != 'CSRFTokenField':
        % if field.type == 'SubmitField':
          <div class="controls">
            <button type="submit" class="btn">Submit</button>
          </div>
        % elif field.label.text != 'Remember Me':
          ${ field.label(for_=field.name, class_='control-label')}
          <div class="controls">
              ${ field(placeholder=field.label.text, id=field.label.text) }
          </div>
        % endif
      % endif
    % endfor
</%def>

<!-- Flashed messages (if any they will be errors) -->
<%def name="render_flashes()">
    <% messages = get_flashed_messages() %>
    % if messages:
      ${ bootstrap_alert_box(messages, 'error') }
    % endif
</%def>

<!-- Form validation errors (if any) -->
<%def name="render_errors(errors)">
    % for error,messages in dict.iteritems(errors):
      ${ bootstrap_alert_box(messages, 'info') }
    % endfor
</%def>