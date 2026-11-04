#!/bin/bash
# Production start script for Render

echo "🚀 Starting Annadata Saathi API..."

# Use gunicorn with our configuration
exec gunicorn main:app \
    --config gunicorn.conf.py \
    --log-level info
