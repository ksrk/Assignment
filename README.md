##Installing and Running
1. Python flask application developed using python 3.7.1, Make sure similar
   version running on the machine where code will be executed
2. Create virtual environment(https://virtualenv.pypa.io/en/latest/userguide/)
    >virtualenv -p python3 trails_env
3. Activate the  virtual environment
    >source trails_env/bin/activate
4. Navigate to root of source code folder where 'setup.py' or README.md available
    > cd <path_to_root>
5. Install the dependency packages
    > pip install -r requirements.txt
6. Install the source distribution as below
    > pip install dist/trails-1.0-py3-none-any.whl
7. Run the program
    > run.py or > python run.py

##Viewing the program output
1. Open web browser
2. Enter the web address to see the list of stores and coordinates
    http://127.0.0.1:5000/stores
3. Enter the web address to filter the store with raidus and postcode
    http://127.0.0.1:5000/stores/<postcode>/<radius>
    **Assumption made here that postcode query will be done on json data, no
      other postcode work


##Troubleshooting
1.Application or program not able to start?
    Sometimes networt port(used here 5000) not available, use network utility
    to find the program and close, then start the application. Other way is 
    restart the os then start the application.