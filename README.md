# Test_Task-LD_Flask

HOW TO USE THIS PROJECT

- CONFIGURATION : 

    Download Chromedriver and add to executable_path likes :

        driver = webdriver.Chrome(executable_path = r'D:/chromedriver/chromedriver.exe') 

- TO USE :

    In project folder, tab : 

        D:\Test_Task LD_Flask> cd app
        D:\Test_Task LD_Flask\app> set  "FLASK_APP = app:flask_app.py"
        D:\Test_Task LD_Flask\app> set "FLASK_ENV=development"
        D:\Test_Task LD_Flask\app> flask run
    
    In browser, tab : http://127.0.0.1:5000/distance/<from address>/<to address> likes : 
        http://127.0.0.1:5000/distance/paris/moscow

    The result can be seen in browser and example.log file, example : 
        {"distance":"2,840 km"}

- TO TEST :

    In case, from or to address is null, the distance is 0
             from and to address is same, the distance is 0
             in other, the distance likes {"distance":"2,840 km"}

    