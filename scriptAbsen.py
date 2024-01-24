import json
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def matkul():
    data = json.load(open('link_matkul.json'))
    x = datetime.datetime.now()
    sekarang = x.strftime("%w")
    jam = x.strftime("%H:%M")
    if sekarang == '1':
        if jam >= '11:40' and jam < '14:10':
            ket = "Hari Senin"
            matkul_sekarang = data['monday1']
        elif jam >= '14:10' and jam < '16:40':
            ket = "Hari Senin"
            matkul_sekarang = data['monday2']
        else:
            ket ="Jadwal Pelajaran Belum Mulai atau sudah Selesai"
            matkul_sekarang = 0
    elif sekarang == '2':
        if jam >= '09:10' and jam < '10:50':
            ket = "Hari Selasa"
            matkul_sekarang = data['tuesday1']
        else:
            ket ="Jadwal Pelajaran Belum Mulai atau sudah Selesai"
            matkul_sekarang = 0
    elif sekarang == '3':
        if jam >= '07:30' and jam < '10:00':
            ket = "Hari Rabu"
            matkul_sekarang = data['wednesday1']
        else:
            ket ="Jadwal Pelajaran Belum Mulai atau sudah Selesai"
            matkul_sekarang = 0
    elif sekarang == '5':
        if jam >= '09:10' and jam < '11:40':
            ket = "hari Jum'At"
            matkul_sekarang = data['friday1']
        elif jam >= '13:20' and jam < '16:40':
            ket = "hari Jum'At"
            matkul_sekarang = data['friday2']
        else:
            ket = "Jadwal Pelajaran Belum Mulai atau sudah Selesai"
            matkul_sekarang = 0
    else:
        ket ='Hari Libur'
        matkul_sekarang = 0

    return ket, matkul_sekarang

def do_absen(matkul_sekarang):
    if matkul_sekarang == 0:
        print(ket)
    else:
        PATH = "C:\Drivers\chromedriver.exe" #path your chromedriver
        driver = webdriver.Chrome(PATH)
        LOGIN_URL = "http://elearning.bsi.ac.id/login" #URL website e-learning change this section
        driver.get(LOGIN_URL)
        data = json.load(open('akun.json'))
        username_mhs = data['username']
        password_mhs = data['password']

        #you need to inspect form login and find the input id of username and password
        #example 
        #<input type="text" id="username" name="username" required>
        #<input type="text" id="password" name="password" required>
        username = driver.find_element_by_id("username") # you need to change this variabel match with id in your login page
        username.send_keys(username_mhs)

        password = driver.find_element_by_id("password") # you need to change this variabel match with id in your login page
        password.send_keys(password_mhs)
        password.send_keys(Keys.ENTER)

        driver.get(matkul_sekarang)

        time.sleep(3)
        
        #find the xpath exactly position of button login and change this path
        absen = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div/form/center/button")
        absen.click()

        #find the xpath exatcly find element of textarea with matching with listCourse
        komen = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div/form/center/textarea")
        komen.send_keys("Sudah Absen Hari ini")
        #find the xpath exactly as a button absen/hadir
        kirim = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div/form/center/button")
        kirim.click()

# Call the matkul function
ket, matkul_sekarang = matkul()

# Call the do_absen function with the matkul_sekarang value
do_absen(matkul_sekarang)
