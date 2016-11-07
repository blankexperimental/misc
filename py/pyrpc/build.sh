#!/bin/sh

protoc --proto_path=. --python_out=. echo_service.proto