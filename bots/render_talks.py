from pathlib import Path
from datetime import datetime
import re
from string import punctuation

import jinja2
import pytz
from ruamel.yaml import YAML

registration_form_html ="""<!DOCTYPE html>
<head>
<script src='https://www.google.com/recaptcha/api.js'></script>
</head>
<html>
<style>
body {font-family: Arial, Helvetica, sans-serif;}
* {box-sizing: border-box}
/* Full-width input fields */
input[type=text] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}
input[type=email] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}
input[type=text]:focus {
  background-color: #ddd;
  outline: none;
}
input[type=email]:focus {
  background-color: #ddd;
  outline: none;
}
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}
/* Set a style for all buttons */
button {
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}
button:hover {
  opacity:1;
}
/* Float registration button and add an equal width */
.registerbtn {
  float: left;
  width: 50%;
}
select {
  width: 100%;
  padding: 16px 20px;
  border: none;
  border-radius: 4px;
  background-color: #f1f1f1;
}
/* Add padding to container elements */
.container {
  padding: 16px;
}
/* Clear floats */
.clearfix::after {
  content: '';
  clear: both;
  display: table;
}
.alert {
  padding: 20px;
  background-color: #f44336;
  color: white;
  opacity: 1;
  transition: opacity 0.6s;
  margin-bottom: 15px;
}
.alert.success {background-color: #4CAF50;}
.alert.info {background-color: #2196F3;}
.alert.warning {background-color: #ff9800;}
.closebtn {
  margin-left: 15px;
  color: white;
  font-weight: bold;
  float: right;
  font-size: 12px;
  line-height: 20px;
  cursor: pointer;
  transition: 0.3s;
}
.closebtn:hover {
  color: black;
}
/* Change styles for cancel button and signup button on extra small screens */
@media screen and (max-width: 300px) {
  .cancelbtn, .signupbtn {
     width: 100%;
  }
}
</style>
<body>
<form id='registrationForm-MEETINGID' method='post' action='http://vsf-worker.virtualscienceforum.workers.dev/register' style='border:1px solid #ccc' onsubmit="submitZoomRegistration(event, MEETINGID)">
  <div class='container'>
    <h1>Sign Up</h1>
    <p>Please fill in this form to register for the talk by SPEAKERNAME.</p>
    <hr>
    <label for='firstname'><b>First Name</b></label>
    <input type='text' placeholder='Enter your first name' name='firstname' id='firstname-MEETINGID' required>
    <label for='lastname'><b>Last Name</b></label>
    <input type='text' placeholder='Enter your last name' name='lastname' id='lastname-MEETINGID' required>
    <label for='address'><b>Email</b></label>
    <input type='email' placeholder='Enter your email' name='address' id='address-MEETINGID' required>
    <label for='org'><b>Affiliation</b></label>
    <input type='text' placeholder='Enter your affiliation' name='affiliation' id='affiliation-MEETINGID' required>
    <label for="howdidyouhear"><b>How did you hear about us?</b></label>
    <select id="howdidyouhear-MEETINGID" name="howdidyouhear" required>
      <option value="Email list">Email list</option>
      <option value="A colleague (not an organizer)">A colleague (not an organizer)</option>
      <option value="One of the organizers">One of the organizers</option>
      <option value="Other" selected>Other</option>
    </select>
    <div id='checkboxes'>
        <ul id='checkboxes' style='list-style:none'>
          <li> <input type='checkbox' name='instructions-checkbox' value='confirm-instructions' required> Please confirm you have read the <a href='http://virtualscienceforum.org/#/attendeeguide'>participant instructions*</a> </li>
          <li> <input type='checkbox' name='contact-checkbox' value='confirm-contact' checked> Please check this box if we may contact you about future VSF events </li>
        </ul>
    </div>
    <input type='hidden' name='eventType' id='eventType-MEETINGID' value='EVENTTYPE' required>
    <input type='hidden' name='meetingID' id='meetingID-MEETINGID' value='MEETINGID' required>
    <div id='recaptcha' name='recaptcha' class='g-recaptcha' data-sitekey='6Lf37MoZAAAAAF19QdljioXkLIw23w94QWpy9c5E'></div>
    <div class='clearfix container'>
      <button type='submit' class='registerbtn'>Register</button>
    </div>
    <div id="errordiv-MEETINGID" class="alert" style="display:none">
      <span class="closebtn" onclick="this.parentElement.style.display='none';"">&times;</span>
      <strong id="errormsg-MEETINGID"></strong>
    </div>
  </div>
</form>
</body>
</html>"""

yaml = YAML(typ='safe')
with open('../talks.yml') as f:
    talks = yaml.load(f)

punctuation_without_dash = punctuation.replace('-','')
translation_table = str.maketrans('','', punctuation_without_dash)
def format_title(s):
    return s.translate(translation_table).replace(' ', '-')

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('../templates')
)
env.filters['format_title'] = format_title

def update_registration_form(talk):
    return registration_form_html.replace("SPEAKERNAME", talk['speaker_name']).replace("MEETINGID", str(talk['zoom_meeting_id'])).replace("EVENTTYPE", talk['event_type'])

env.filters['registration_form'] = update_registration_form

header = Path("../speakers-corner-header.md").read_text()

for talk in talks:
    talk['time'] = talk['time'].replace(tzinfo=pytz.UTC)
    if re.fullmatch(r"\d{4}\.\d{5}", talk.get("preprint", "")) is None:
        talk.pop("preprint", "")

sc_talks = [talk for talk in talks if talk['event_type'] == 'speakers_corner']
now = datetime.now(tz=pytz.UTC)
upcoming = [talk for talk in sc_talks if talk["time"] > now]
previous = [talk for talk in sc_talks if talk["time"] < now]

Path('../speakers-corner.md').write_text(
    env.get_template('speakers_corner.md.j2').render(
        header=header,
        upcoming=upcoming,
        previous=previous,
    )
)

Path('../long_range_colloquium.md').write_text(
    env.get_template('long_range_colloquium.md.j2').render(
        header=header,
        talks=[talk for talk in talks if talk['event_type'] == 'lrc'],
        now=now
    )
)
