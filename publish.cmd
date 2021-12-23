call pelican content -o output -s publishconf.py
call ghp-import -m "Generate Pelican site" --no-jekyll -b master output
call git push origin master