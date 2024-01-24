# Auto Absen Project
this project built and run with [python](https://www.python.org/) develope by indra bayu inspired from [sahrulprograming](https://github.com/sahrulprograming/)

# Preparation
before you run the program on your terminal you need to install a few driver <br>
1. intal uptodate your [chrome](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&oco=1)
2. instal [webdriver](https://chromedriver.chromium.org/downloads) for chrome, for sure install match with yoyr chrome version
3. instal library python [selenium](https://pypi.org/project/selenium/)

# Configuration
you need to change state variabel before you used in json file <br>
1. Change username and password in account.json<br>
    ```python
    {
      "username" : "username", // change username with your username
      "password" : "Password"  // change pasword with your password
    }
    ```
2. change course in listCourse.json
     ```python
    {
      "monday1": "math", // change math with your actual course
      "monday2": "chemistry",
    }
    ```
3. if the day and hours deferent with my mine you need to change it as you needed, im using day with section number<br>
   0 = minggu, 1 = senin, 2 = selasa, 3 = rabu, 4 = kamis, 5 = jum'at, 6 = sabtu
4. and last you need to change the URL and also some code to check captcha and fix your xpath 
   
