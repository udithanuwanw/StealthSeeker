<!DOCTYPE html>
<html lang="en">
<body>

<h1>StealthSeeker Chrome Extension</h1>

<p>This Chrome extension, named StealthSeeker, is designed to collect various sensitive user data while active in the browser. It captures cookies, local storage, session storage, indexed DB, cache storage, usernames, and passwords used during browsing sessions. Additionally, it includes a keylogger functionality to log all keystrokes.</p>

<h2>Functionality</h2>

<p>Upon installation and activation, the extension begins to collect data from the browser. It organizes the gathered data into folders categorized by UserID and then by visited domain. Within each domain folder, it lists all the information related to that domain, including cookies, storages, usernames, and passwords.</p>

<p>The extension runs a local Flask server (server.py) to receive and process the collected data. It also includes a Python script (chromepass.py) to extract and decrypt saved Chrome passwords from the user's system.</p>
<h2>Installation</h2>

<p>1. Install Python:</p>
<ul>
  <li>Download and install Python from the official website: <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a></li>
</ul>

<p>2. Install the required libraries:</p>
<ul>
  <li>Open a terminal or command prompt.</li>
  <li>Navigate to the project directory.</li>
  <li>Run the following command to install the required libraries:</li>
</ul>

<pre><code>pip install -r requirements.txt</code></pre>
<h2>Usage</h2>

<p>1. Install the extension in your Chrome browser.</p>
<p>2. Run the server.py locally.</p>
<p>3. Activate the extension.</p>
<p>4. The extension will start collecting data from your browsing sessions.</p>

<h2>Security and Privacy</h2>

<p>It's important to note that this extension collects sensitive user data, including passwords, which may pose privacy and security risks. Ensure that you handle and store this data responsibly and securely.</p>

<h2>Disclaimer</h2>

<p>This project is for educational purposes only. Do not use this extension for malicious purposes or without proper consent from users.</p>

<h2>Contributing</h2>

<p>Contributions to improve the extension's functionality or security are welcome. Please submit pull requests or open issues on the GitHub repository.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License. Feel free to modify and distribute it according to the terms of the license..</p>

</body>
</html>
