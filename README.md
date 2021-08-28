# TechNova2021
1. `source env/bin/activate`
2. `cd examples/multires-lyrics-search`
3. `pip3 install -r requirements.txt` (you may need to also run `pip3 install wheel` and re-install these requirements)
4. (`sudo python3 app.py -t index`) -> if workspace is already there, may not be needed
5. `sudo python3 app.py -t query`
6. cd static, run `python -m http.server 9000`
7. go to `localhost:9000`
