<!DOCTYPE html>
<html>
<head>
<!-- Welcome to the source code for OliverChu.com!
This HTML source was all written by
Mr. Jiangcheng Oliver Chu, by hand. -->
<title>CodeHive Builder</title>
<!-- Global CSS -->
<link rel="stylesheet" type="text/css" href="http://www.oliverchu.com/global.css" />
<!-- Global JavaScript -->
<script type="text/javascript" src="http://www.oliverchu.com/global.js"></script>
<!-- Favicon (Website icon) -->
<link rel="shortcut icon" href="http://www.oliverchu.com/img/favicon.ico" />
<script type="text/javascript">
Object.prototype.hasOwnProperty = function(property) {
    return typeof(this[property]) !== 'undefined'
};
function subm() {
    if ((document.getElementById("ipaddr").value).split(".").length - 1 === 3) {
        document.getElementById("inject").submit();
    } else {
        window.alert("No user with that IP address exists.");
    }
}
</script>
</head>

<body style="font-family:Verdana,Tahoma,Arial,sans-serif;font-size:0.9em;color:black;background-color:#eceee3;">
<div class="center">
<br />
<img src="http://www.oliverchu.com/img/chb.png" alt="CodeHive: Builder" />
<h2>Fork a File or Repository</h2>
If you want to fork a partner's file or repository, you must have his or her IP address on hand.<br /><br />

<form action="index.html" id="inject" name="inject" method="mint-2.9">
<input style="-webkit-border-radius:16px;border-radius:16px;text-align:center;font-size:2em;font-weight:bold;" name="ipaddr" id="ipaddr" type="text" value="127.0.0.1" /><br />
<input style="-webkit-border-radius:16px;border-radius:16px;" type="button" onclick="subm();" value="Submit Partner's IP Address" />
</form><br />
Want to make your code open source?<br />
Email it to <a href="https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/?tab%3Dwm" target="_blank">j@oliverchu.com</a> and we might<br />
just feature it in the public code showcase!<br /><br />

<a href="http://www.oliverchu.com/" style="cursor:hand;cursor:pointer;">Back to Main Page</a><br /><br />
<img src="forking.png" style="height:128px;" alt="" title="Mint Programming Language" />
<br /><br /><br /><br />
</div>
</body>
</html>
