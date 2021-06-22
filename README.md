# pythonREST
A small REST service developed using Python and Flask that calculates a special math

## Requirements
```
1) python 3.8.2+
2) pip 19.2.3+
3) Flask 2.0.1 (This will be installed in the virtual environment)
```
## Steps to start the endpoint
 ```
 1) git clone https://github.com/bvsravikiran/pythonREST.git
 2) cd pythonREST
 3) python3 -m venv envpyrest
 4) source envpyrest/bin/activate
 5) pip install -r requirements.txt
 6) export FLASK_APP=specialmath/app
 7) flask run
 ```
 At this point, you will most likely see the following message printed out on the terminal.
 ```
 * Serving Flask app 'specialmath/app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
If you see the above message, that means the server has started successfully. At this point, you can either of the following
- Click on the above URL to open it in a browser.
- Open a new terminal and type the following.
```
curl http://127.0.0.1:5000/specialmath/7
```
- Once you are done testing, stop the server by clicking ctrl+c (on Windows) or command+. (on Mac).
- Deactivate the virtual environment created earlier by typing
```
deactivate
```

## Testing
Sample Input  | Sample Output
------------- | -------------
http://127.0.0.1:5000/specialmath/0  | 0
http://127.0.0.1:5000/specialmath/1  | 1
http://127.0.0.1:5000/specialmath/7  | 79
http://127.0.0.1:5000/specialmath/17 | 10926
http://127.0.0.1:5000/specialmath/90 | 19740274219868223074
http://127.0.0.1:5000/specialmath/-1  | Call with a valid number in the URL. Example: http://127.0.0.1:5000/specialmath/7
http://127.0.0.1:5000/specialmath/abc  | Call with a valid number in the URL. Example: http://127.0.0.1:5000/specialmath/7
http://127.0.0.1:5000/specialmath  | Call with a valid number in the URL. Example: http://127.0.0.1:5000/specialmath/7
http://127.0.0.1:5000/abc  | Call with a valid number in the URL. Example: http://127.0.0.1:5000/specialmath/7
http://127.0.0.1:5000  | Call with a valid number in the URL. Example: http://127.0.0.1:5000/specialmath/7

