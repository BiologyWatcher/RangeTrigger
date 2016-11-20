#!/bin/bash

API="API KEY HERE"
MSG="$1"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="$MSG" -d body="$MSG"
