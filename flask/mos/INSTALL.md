# Install Flask using the venv setup
http://flask.pocoo.org/docs/0.12/installation/
* sudo pip install virtualenv
* mkdir mos
* cd mos
* virtualenv venv
* . venv/bin/activate
* pip install Flask
* python> from flask import Flask


# Start MOS Microservice
* #> sh run_mos.sh 
* #> vim curl_mos_list.txt # contains the urls to be executed assuming defaults as 127.0.0.1:5000
* #> sh curl_mos.sh # execute the sample apis

