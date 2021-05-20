#!/bin/bash

cd /source
uvicorn main:app --reload --host 0.0.0.0