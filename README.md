# TechNova2021: Change My Tune

Linux systems:
1. `source env/bin/activate`
2. `cd examples/multires-lyrics-search`
3. `pip3 install -r requirements.txt` (you may need to also run `pip3 install wheel` and re-install these requirements)
4. `pip3 install flask`
5. (`sudo python3 app.py -t index`) -> if workspace is already there, may not be needed
6. `sudo python3 app.py -t query`
7. If you haven't previously, follow https://cloud.google.com/docs/authentication/getting-started and set `export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json`"
8. cd static/static, run FLASK_ALL="app.py" flask run

Previously,
7. cd static, run `python3 -m http.server 9000`
8. go to `localhost:9000`
