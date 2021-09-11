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

input[type=text]:focus {
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

/* Float signup button and add an equal width */
.signupbtn {
  float: left;
  margin-top: 50px;
  width: 50%;
}

/* Add padding to container elements */
.container {
  padding: 16px;
}

/* Clear floats */
.clearfix::after {
  content: "";
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
  .signupbtn {
     width: 100%;
  }
}

</style>
  <form id="mailingListForm" method="post" action="https://vsf-worker.virtualscienceforum.workers.dev/maillinglist" style="border:1px solid #ccc" onsubmit="submitMailingListSignupForm(event);">
  <div class="container">
    <h1>Sign Up</h1>
    <p>Please fill in this form and select the mailing lists you would like to join.</p>
    <div id="errordiv" class="alert" style="display:none">
      <span class="closebtn" onclick="this.parentElement.style.display='none';"">&times;</span>
      <strong id="errormsg"></strong>
    </div>
    <hr>
    <label for="name"><b>Name</b></label>
    <input type="text" placeholder="Enter your name" name="name" id="name" required>
    <label for="address"><b>Email</b></label>
    <input type="text" placeholder="Enter your Email" name="address" id="address" required>
    <div id="mailinglists">
      <label for="mailinglist"><b>Mailing lists</b></label>
      <ul id="mailinglist" style='list-style:none'>
        <li> <input type="checkbox" name="signup-checkbox" value="signup-general" checked> General mailing list </li>
        <li> <input type="checkbox" name="signup-checkbox" value="signup-speakerscorner"> <a href="#speakers-corner">Speakers' Corner</a> mailing list </li>
      </ul>
    </div>
    <div id="recaptcha" name="recaptcha" class="g-recaptcha" data-sitekey="6Lf37MoZAAAAAF19QdljioXkLIw23w94QWpy9c5E"></div>
    <div class="clearfix">
      <button type="submit" class="signupbtn">Sign Up</button>
    </div>
  </div>
</form>

<script src='https://www.google.com/recaptcha/api.js' async defer></script>
