#!/bin/bash
# a network proy
curl -s -I "$1" | grep Allow | cut -d" " -f2-
