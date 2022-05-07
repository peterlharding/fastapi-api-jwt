#!/bin/sh
#
# -----------------------------------------------------------------------------

which python

uvicorn --host=0.0.0.0 --app-dir src app.main:app --log-level debug


