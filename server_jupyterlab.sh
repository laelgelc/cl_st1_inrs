#!/bin/bash

nohup jupyter-lab --ip 0.0.0.0 --no-browser --allow-root &

echo "Update the 'GELCSG' inbound rule for port 8888 with the IP address of your computer"
echo "Run 'https://<Public IPv4 DNS>:8888' on your browser and provide the following server token:"
jupyter server list
