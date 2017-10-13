# jsonRestEndpoint
This is used to test New Relic Webhook payload
This is a python script that uses Flask to accept and parse the Json payload.
What I have done is started this script and opened my local firewall to test the json payload
The resulting script will print the request on the screen and show the payload.

1. Install python based on your OS.
2. Follow the pip instrunctions from here https://pip.pypa.io/en/stable/installing/ to install pip
3. Install Flask pip install Flask or sudo pip install Flask depending on how you want it installed
4. At a commandline enter export FLASK_APP=app.py
5. While in the Directry enter python -m flask run --host=0.0.0.0

The following will be displayed

* Serving Flask app "app"
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

To test New Relic Webhook just make sure the server the app is on has access to the internet for incoming calls on port 5000
Configure the webhook to point to the server we just setup and you should see a json payload print on the screen of the server
