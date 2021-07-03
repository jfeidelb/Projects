#!/bin/bash

date=$(date '+%Y-%m-%d %H:%M')

echo "Uploading to GitHub..."
cd /a/Projects
git add .
git commit -m "$date"
git push -u origin main
exit