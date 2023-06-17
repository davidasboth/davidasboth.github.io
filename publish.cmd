call poetry run pelican content -o output -s publishconf.py
call poetry run ghp-import -m "Generate Pelican site" --no-jekyll -b master output
call git push origin master