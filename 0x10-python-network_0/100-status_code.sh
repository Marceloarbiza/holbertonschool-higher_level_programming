#!/bin/bash
# a network proy
curl -s -o /dev/null -w "%{http_code}" "$1"
