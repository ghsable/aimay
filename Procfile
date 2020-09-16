web: gunicorn --workers $(($(grep -c processor /proc/cpuinfo)*2+1)) aimay.__main__:app
