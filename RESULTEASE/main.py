from PIL import Image
import matplotlib.pyplot as plt
import pywhatkit
from datetime import datetime
import json
import random
import time
import os
import pyttsx3


# To use text to speak
def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


students = {
    "S01": {"Name": "PHANI CHARAN", "Rollno": "22BD1A1201", "Section": "IT", "Gender": "Male", "Password": "Kmit123@"},
    "S02": {"Name": "AADITYA KULKARNI", "Rollno": "22BD1A1202", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S03": {"Name": "AARYA PATEL", "Rollno": "22BD1A1203", "Section": "IT", "Gender": "Male", "Password": "Kmit123@"},
    "S04": {"Name": "AIMAN ZAREEN", "Rollno": "22BD1A1204", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S05": {"Name": "AITHA VARSHIKA", "Rollno": "22BD1A1205", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S06": {"Name": "ALLAGONDA CHARAN REDDY", "Rollno": "22BD1A1206", "Section": "IT", "Gender": "Male",
            "PasswordS": "Kmit123@"},
    "S07": {"Name": "ANUMANDLA LAXMI PRANITHA", "Rollno": "22BD1A1207", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S08": {"Name": "BANDI ROHITH REDDY", "Rollno": "22BD1A12008", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S09": {"Name": "BANDI SUHANI PATEL", "Rollno": "22BD1A1209", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S10": {"Name": "BOOTLA MEGHANEEL SUDHAMSH", "Rollno": "22BD1A1210", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S11": {"Name": "BURANDODDI REDDIGARI SOHITH KUMAR REDDY", "Rollno": "22BD1A1211", "Section": "IT",
            "Gender": "Male", "Password": "Kmit123@"},
    "S12": {"Name": "CHILIVERY SRIPAD", "Rollno": "22BD1A1212", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S13": {"Name": "CHINTHAPALLY AJAY KUMAR", "Rollno": "22BD1A1213", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S14": {"Name": "CHUNDURU SATYA SAI RUTVIK", "Rollno": "22BD1A1214", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S15": {"Name": "D SIDDHARTH", "Rollno": "22BD1A1215", "Section": "IT", "Gender": "Male", "Password": "Kmit123@"},
    "S16": {"Name": "DEEPTHI VIJAY ACHARYA", "Rollno": "22BD1A1216", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S17": {"Name": "DRONA VENKATA SRIVANI", "Rollno": "22BD1A1217", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S18": {"Name": "ERRA UMESH CHANDRA", "Rollno": "22BD1A1218", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S19": {"Name": "G SHIVA SHANKAR REDDY", "Rollno": "22BD1A1219", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S20": {"Name": "GANJI TEJASWINI", "Rollno": "22BD1A1220", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S21": {"Name": "GARIGE HIMANI", "Rollno": "22BD1A1221", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S22": {"Name": "GAUTHAM KEDIA", "Rollno": "22BD1A1222", "Section": "IT", "Gender": "Male", "Password": "Kmit123@"},
    "S23": {"Name": "GEEREDDY JASHWANTH REDDY", "Rollno": "22BD1A1223", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S24": {"Name": "GUDABOINA SAI PRANEETH", "Rollno": "22BD1A1224", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S25": {"Name": "J JAHNAVI", "Rollno": "22BD1A1225", "Section": "IT", "Gender": "Female", "Password": "Kmit123@"},
    "S26": {"Name": "JULAKANTI LEENA SANJANA", "Rollno": "22BD1A1226", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S27": {"Name": "KADARI KOUSHIK REDDY", "Rollno": "22BD1A1227", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S28": {"Name": "KATRAPALLI SIDDHARTH", "Rollno": "22BD1A1228", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S29": {"Name": "KESHABOINA RAHUL", "Rollno": "22BD1A1229", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S30": {"Name": "KEVARLA RITHIKA", "Rollno": "22BD1A1230", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S31": {"Name": "KONCHADA JASMITH", "Rollno": "22BD1A1231", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S32": {"Name": "KOPPULA SURYA PRAKASH REDDY", "Rollno": "22BD1A1232", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S33": {"Name": "MADIRAJU VENKATA RADHA KRISHNA", "Rollno": "22BD1A1233", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S34": {"Name": "MANDAL AKSHITA", "Rollno": "22BD1A1234", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S35": {"Name": "MANDAVA VENKATA SAI SANTHOSH", "Rollno": "22BD1A1235", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S36": {"Name": "MANTRI YESHWANTH", "Rollno": "22BD1A1236", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S37": {"Name": "MATROJU SHRESTA", "Rollno": "22BD1A1237", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S38": {"Name": "MD ALTHAF", "Rollno": "22BD1A1238", "Section": "IT", "Gender": "Male", "Password": "Kmit123@"},
    "S39": {"Name": "MOHD MUSHRAF AHMED", "Rollno": "22BD1A1239", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S40": {"Name": "MUSTI LALITH SRINANDAN", "Rollno": "22BD1A1240", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S41": {"Name": "MUTNURI VIJAYA SASANK RAO", "Rollno": "22BD1A1241", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S42": {"Name": "NAGUBANDI PRANITHA", "Rollno": "22BD1A1242", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S43": {"Name": "NITISH NARVA", "Rollno": "22BD1A1243", "Section": "IT", "Gender": "Male", "Password": "Kmit123@"},
    "S44": {"Name": "NUKALA YASHASRI REDDY", "Rollno": "22BD1A1244", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S45": {"Name": "PEDDIREDDY SREENADH REDDY", "Rollno": "22BD1A1245", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S46": {"Name": "PRADYUMNA REDDY KANTHALA", "Rollno": "22BD1A1246", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S47": {"Name": "REPALA SAHAN", "Rollno": "22BD1A1247", "Section": "IT", "Gender": "Male", "Password": "Kmit123@"},
    "S48": {"Name": "RISHIKA SIRNAM", "Rollno": "22BD1A1248", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S49": {"Name": "SAGI SAI NIKHIL", "Rollno": "22BD1A1249", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S50": {"Name": "SAI SANTOSH YELLENKI", "Rollno": "22BD1A1250", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S51": {"Name": "SAKETH MOTHE", "Rollno": "22BD1A1251", "Section": "IT", "Gender": "Male", "Password": "Kmit123@"},
    "S52": {"Name": "SATYA AKSHAY TIRUMANI", "Rollno": "22BD1A1252", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S53": {"Name": "SESHA SAI PRATIEK YEGGINA", "Rollno": "22BD1A1253", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S54": {"Name": "SREE CHARAN REDDY MANNE", "Rollno": "22BD1A1254", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S55": {"Name": "SRIKAR NARSINGOJU", "Rollno": "22BD1A1255", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S56": {"Name": "SUDHEEP BHASKAR YADAV", "Rollno": "22BD1A1256", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S57": {"Name": "SURAPANENI YASHASWINI", "Rollno": "22BD1A1257", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S58": {"Name": "T HARINA SURI", "Rollno": "22BD1A1258", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S59": {"Name": "TANGALLAPALLY SRIKAR", "Rollno": "22BD1A1259", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S60": {"Name": "TELUKOTI VISHAL SAI", "Rollno": "22BD1A1260", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S61": {"Name": "TUNGA SURYA SIMHA REDDY", "Rollno": "22BD1A1261", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S62": {"Name": "U V N VARDHAN", "Rollno": "22BD1A1262", "Section": "IT", "Gender": "Male", "Password": "Kmit123@"},
    "S63": {"Name": "VARDAAN BHATIA", "Rollno": "22BD1A1263", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S64": {"Name": "VELUVALI SRIKAR", "Rollno": "22BD1A1264", "Section": "IT", "Gender": "Male",
            "Password": "Kmit123@"},
    "S65": {"Name": "VOODA SRUTHI", "Rollno": "22BD1A1265", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"},
    "S66": {"Name": "MEDISHETTY RITHIKA", "Rollno": "22BD1A1266", "Section": "IT", "Gender": "Female",
            "Password": "Kmit123@"}
}

# To dump the structured data into json file
# with open("data.json","w") as f:
#     json.dump(students,f,indent=2)

# Loading the data to make changes
with open("data.json", "r") as f:
    data = json.load(f)

# To display the Result


def disres(img_name):
    # Set the figure size
    fig = plt.figure(figsize=(13, 7))

    # Open the image file
    img = Image.open(img_name)

    f = {"family": "cambria", "size": 40}
    # Display the image using matplotlib
    plt.title("RESULT", fontdict=f)
    plt.imshow(img)
    plt.axis('off')  # Turn off axes
    plt.show()


# To send otp to given number
def send_otp(ph_num):
    # Get the current time
    current_time = datetime.now().strftime("%H:%M:%S")
    h, m, s = current_time.split(":")
    s = int(s)

    # To Generate random otp
    otp = str(random.randint(1000, 9999))

    while s > 45:
        current_time = datetime.now().strftime("%H:%M:%S")
        h, m, s = current_time.split(":")
        s = int(s)
    pywhatkit.sendwhatmsg('+91' + ph_num, "Your OTP is {}".format(otp), int(h), int(m) + 1)
    return otp


# To check if a password is valid or not
def validpass(s):
    if len(s) >= 8:
        if not any(i.islower() for i in s):
            return False
        if not any(i.isdigit() for i in s):
            return False
        if not any(i.isupper() for i in s):
            return False
        if not any(i in "!@#$%^&*,.~" for i in s):
            return False
        return True
    else:
        return False


# To change the Password
def changepass(s):
    print("Please change your Password")
    speak("Please change your Password")
    if "Phno" not in data["S" + s[-2::]]:
        speak("Enter Mobile number to receive OTP to")
        mob = input("Enter Mobile number to receive OTP:")
        data["S" + s[-2::]]["Phno"] = mob
    else:
        mob = data["S" + s[-2::]]["Phno"]
    t1 = send_otp(mob)
    speak("Enter otp to change password")
    t2 = input("Enter OTP to change Password:")
    while t1 != t2:
        speak("OTP doesn't match!! Try again")
        print("OTP doesn't match!! Try again")
        t1 = send_otp(mob)
        speak("Enter otp to change password")
        t2 = input("Enter OTP to change Password:")

    speak("Enter New Password")
    np = input("Enter New Password:")
    # To check if entered password is a valid one
    while not validpass(np):
        speak("Password doesn't match all the Requirementss!!")
        print("Password doesn't match all the Requirements!!")
        speak("Please check and enter the password:")
        np = input("Please check and enter the password:")

    speak("Confirm the password:")
    cpa = input("Confirm the password:")

    # Confirm the first entered password
    while np != cpa:
        speak("Password doesn't Match\nRe-enter the password:")
        cpa = input("Password doesn't Match\nRe-enter the password:")

    # Updates password
    data["S" + s[-2::]]["Password"] = np
    speak("Password has been changed successfully")
    print("Password has been changed successfully")
    speak("Press any key to continue")
    t = input("Press any key to continue:")
    if t:
        time.sleep(2)
        os.system("cls")
        return


# To analyse the results
def result_analysis(student_index):
    # Marks of 66 students in 8 subjects (example data)
    marks = [

        [10, 10, 10, 10, 9, 7, 8, 10, 9.03],  # 1
        [10, 10, 10, 10, 9, 9, 9, 9, 9.35],  # 2
        [8, 10, 10, 10, 5, 7, 8, 9, 8.05],  # 3
        [10, 10, 10, 10, 9, 8, 9, 10, 9.35],  # 4
        [10, 10, 8, 10, 0, 5, 5, 7, 0],  # 5
        [10, 9, 9, 9, 8, 5, 5, 6, 7, 6.84],  # 6
        [8, 9, 10, 10, 5, 0, 6, 8, 0],  # 7
        [10, 10, 10, 10, 9, 9, 10, 10, 9.68],  # 8
        [10, 9, 10, 10, 9, 9, 9, 9, 9.30],  # 9
        [10, 10, 10, 9, 7, 7, 8, 9, 8.41],  # 10
        [10, 10, 10, 9, 9, 8, 7, 9, 8.73],  # 12
        [10, 10, 10, 10, 6, 7, 8, 8, 8.22],  # 13
        [7, 10, 10, 8, 0, 6, 6, 6, 0],  # 14
        [7, 10, 10, 8, 0, 0, 0, 5, 0],  # 15
        [10, 10, 10, 10, 7, 9, 9, 10, 9.19],  # 16
        [7, 9, 8, 9, 0, 0, 6, 6, 0],  # 17
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 18
        [9, 9, 8, 8, 5, 5, 7, 7, 6.84],  # 19
        [10, 10, 10, 9, 9, 9, 8, 9, 9.05],  # 20
        [9, 10, 10, 10, 0, 6, 6, 7, 0],  # 21
        [10, 10, 10, 10, 6, 7, 9, 8, 8.38],  # 22
        [10, 10, 10, 10, 7, 8, 8, 9, 8.70],  # 23
        [10, 10, 10, 10, 8, 7, 8, 9, 8.70],  # 24
        [10, 10, 10, 9, 9, 8, 8, 8, 8.73],  # 25
        [10, 10, 10, 10, 9, 9, 7, 10, 9.19],  # 26
        [10, 10, 10, 10, 9, 10, 10, 10, 9.84],  # 27
        [7, 10, 10, 10, 6, 6, 5, 8, 7.32],  # 28
        [10, 9, 9, 8, 8, 0, 6, 9, 0],  # 29
        [10, 10, 10, 9, 7, 8, 7, 9, 8.41],  # 30
        [8, 9, 9, 8, 5, 0, 6, 5, 0],  # 31
        [10, 9, 10, 10, 8, 9, 7, 10, 8.97],  # 32
        [9, 9, 9, 8, 7, 7, 7, 8, 7.73],  # 33
        [9, 10, 10, 10, 7, 8, 8, 10, 8.78],  # 34
        [8, 9, 10, 9, 8, 6, 6, 8, 7.7],  # 35
        [9, 10, 10, 8, 8, 9, 7, 9, 8.51],  # 36
        [10, 10, 10, 10, 8, 8, 8, 10, 9.03],  # 37
        [10, 9, 10, 8, 6, 6, 7, 7, 7.41],  # 38
        [10, 9, 10, 9, 9, 9, 7, 9, 8.84],  # 39
        [10, 9, 10, 9, 10, 7, 10, 7, 8.84],  # 40
        [7, 9, 10, 9, 7, 6, 5, 8, 7.3],  # 41
        [10, 10, 10, 9, 10, 10, 9, 8, 9.38],  # 42
        [10, 10, 10, 8, 8, 7, 8, 9, 8.43],  # 43
        [9, 10, 10, 10, 7, 8, 7, 8, 8.3],  # 44
        [10, 9, 10, 8, 8, 8, 7, 9, 8.38],  # 45
        [10, 9, 10, 10, 5, 5, 7, 8, 7.51],  # 46
        [9, 9, 10, 8, 5, 5, 7, 0, 0],  # 47
        [9, 10, 10, 8, 7, 8, 7, 9, 8.19],  # 48
        [9, 10, 10, 8, 8, 7, 7, 7, 7.86],  # 49
        [10, 10, 9, 8, 8, 6, 8, 7, 7.86],  # 50
        [10, 10, 10, 8, 7, 6, 7, 8, 7.78],  # 51
        [10, 10, 10, 9, 7, 8, 8, 7, 8.24],  # 52
        [10, 10, 10, 8, 7, 6, 8, 8, 7.95],  # 53
        [10, 9, 10, 8, 7, 7, 8, 6, 7.74],  # 54
        [10, 10, 10, 10, 8, 7, 8, 9, 8.7],  # 55
        [10, 10, 10, 9, 8, 7, 7, 6, 7.92],  # 56
        [10, 10, 10, 10, 8, 9, 9, 8, 9.03],  # 57
        [8, 9, 10, 9, 5, 5, 6, 8, 7.05],  # 58
        [10, 9, 10, 9, 9, 7, 8, 8, 8.51],  # 59
        [7, 9, 10, 9, 10, 7, 7, 9, 8.43],  # 60
        [10, 9, 10, 8, 7, 8, 8, 8, 8.22],  # 61
        [10, 10, 10, 10, 9, 9, 9, 10, 9.51],  # 62
        [10, 9, 10, 9, 9, 7, 8, 6, 8.19],  # 63
        [10, 10, 10, 10, 10, 10, 9, 10, 9.84],  # 64
        [10, 10, 10, 10, 10, 9, 9, 9, 9.51],  # 65
        [10, 9, 10, 9, 9, 8, 10, 8, 9],  # 66
        # ... add marks for other students here
    ]

    # Student for whom you want to plot the performance
    while 1:
        try:
            if 1 <= student_index <= 66:
                student_index -= 1
                break
            else:
                print("Invalid input!!")

        except ValueError:
            print("Invalid input!!")

    def calper(j):
        s = 0
        for i in marks:
            if marks[student_index - 1][j] < i[j]:
                s += 1
        perf = (s / 66) * 100
        return perf

    # Define subject names
    subject_names = [
        'PPS LAB', 'ELCS LAB', 'CHEM LAB', 'EWS',
        'ACT', 'CHEM', 'PPS', 'EG', 'TOTAL'
    ]

    # Create pie charts for each subjectf 
    f = {"family": "cambria", "size": 40}
    fig, axs = plt.subplots(3, 3, figsize=(7, 7))
    axs = axs.flatten()

    plt.suptitle("RESULT ANALYSIS", fontdict=f)

    # for i, performance in enumerate(student_performance):
    for k in range(9):
        performance = calper(k)
        axs[k].pie([100 - performance, performance], labels=['Better', 'Worse'], autopct='%1.1f%%')
        axs[k].set_title(subject_names[k], pad='-400', fontsize='8')
    plt.legend(["Better", "Worse"], loc=(1, 0))
    plt.tight_layout()
    plt.show()
    return


def login():
    # To check if a Username exists or not
    speak("Enter your Roll Number:")
    s = input("Enter Your Roll Number:")
    while ("S" + s[-2::]) not in data or (s[:8] != "22BD1A12"):
        print("No details found!! Please try again")
        speak("No details found. Please try again")
        speak("Enter your Roll Number:")
        s = input("Enter Your Roll Number:")

    speak("Enter Your password:")
    pa = input("Enter Your password:")

    # To change the password
    if pa == "Kmit123@":
        changepass(s)
        return
    else:
        # To check if the login details finds a match in existing data
        while pa != data["S" + s[-2::]]["Password"]:
            print("Password doesn't match:")
            speak("Password doesn't match:")
            print("1.Try again")
            speak("Press 1 to try again")
            print("2.Forgot Password")
            speak("Press 2 if you forgot your password")
            speak("Enter Your option")
            a = int(input("Enter Your Option:"))
            if a == 1:
                speak("Please check your password and try again:")
                pa = input("Please check your password and try again:")
            elif a == 2:
                changepass(s)
                return
        else:
            speak("Login Successfull...")
            print("Login Successfull...")
        time.sleep(2)
        os.system("cls")

        while 1:
            print("Welecome to Kmit Results zone...")
            speak("welcome to Kmit results zone")
            print("1.Result")
            speak("Press 1 for Result")
            print("2.Result Analysis")
            speak("Press 2 for Result Analysis")
            print("3.Return Homepage")
            speak("Press 3 to return to Homepage")
            speak("Enter Your option")
            n = int(input("Enter your option:"))
            if n == 1:
                disres(s + ".png")
                time.sleep(2)
                os.system("clear")
            elif n == 2:
                result_analysis(int(s[-2:]))
                time.sleep(2)
                os.system("clear")
            elif n == 3:
                time.sleep(2)
                os.system("clear")
                return


def homepage():
    while 1:
        print("Welcome to KMIT")
        speak("Welcome to KMIT")
        print("1.Login")
        speak("Press 1 for Login")
        print("2.View details")
        speak("Press 2 to view your details")
        print("3.Exit")
        speak("Press 3 to Exit")
        speak("Enter your option")

        a = int(input("Enter your option:"))

        if a == 1:
            login()

        elif a == 2:
            k = 0
            speak("Enter your Roll Number:")
            s = input("Enter Your Roll Number:")
            while ("S" + s[-2::]) not in data or (s[:8] != "22BD1A12"):
                print("No details found!! Please try again")
                speak("No details found. Please try again")
                speak("Enter your Roll Number:")
                s = input("Enter Your Roll Number:")
            else:
                print(data["S" + s[-2::]])
            speak("Press any key to continue")
            t = input("Press any key to continue:")
            if t:
                time.sleep(2)
                os.system("cls")
                continue

        elif a == 3:
            print("Thanks for visiting :)")
            speak("Thanks for visiting")
            return


homepage()

# Dumping the changed data
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
