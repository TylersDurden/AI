#!/bin/bash
echo ' Installing required libraries. '
# Start with python libraries 
pip install numpy 
pip install networkx
#pip install Pillow 
#pip install matplotlib

# Now language and misc libraries
pip install ntlk
pip install urllib2
pip install hashlib
pip install --upgrade google-api-python-client
