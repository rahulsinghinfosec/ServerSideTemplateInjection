# ServerSideTemplateInjection
I've tried to emulate Server Side Template Injection using flask web-framework.
<h1>Server-Side Template Injection </h1> <br>
Server-side template injections (SSTI) are vulnerabilities that let the attacker inject code into such server-side templates. In simple terms, the attacker can introduce code that is actually processed by the server-side template. This may result in remote code execution (RCE)
<hr>
<h2>Steps</h2>
<p>pip3 install Flask</p>
<p>pip3 install virtualenv</p>
<h5>On Linux </h5>

<ul>
  <li>mkdir SSTIProject </li>
  <li>cd SSTIProject </li>
  <li>python3 -m venv venv</li>
 </ul>
 
<h5>On Windows </h5>

<ul>
  <li>mkdir SSTIProject </li>
  <li>cd SSTIProject </li>
  <li>p3 -m venv venv</li>
 </ul>
 
<p><b>Windows:</b> set FLASK_APP=hello.py</p>
<p><b>Linux:</b> export FLASK_APP=hello.py</p>
<p>All you have to do now is run</p>
<p>flask run</p> 
