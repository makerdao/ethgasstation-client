#!/bin/sh

py.test --cov=ethgasstation_client --cov-report=term --cov-append tests/
