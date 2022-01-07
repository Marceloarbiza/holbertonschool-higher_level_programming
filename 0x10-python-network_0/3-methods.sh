#!/usr/bin/env bash

curl -s -I "$1" | grep allow | cut -d' ' -f2-
