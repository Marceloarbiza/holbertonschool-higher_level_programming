#!/bin/bash
# a network proy
curl -so /dev/null "$1" -w "%{size_download}"
