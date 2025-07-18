import json
import random
import string
import requests as r
from dotenv import load_dotenv
import os
import cv2
load_dotenv()

def factorial(num):
    a = 1
    i = 1
    while i <= num:
        a = a * i
        i += 1   
    return a 




def maxValueOfList(L):
    max = L[0]
    for a in L:
        if a >max:
            max = a
    return max


def listChange(L):
    for i in range(len(L)):
        if L[i]%2==0:
            L[i] = L[i]*2
        if L[i]%3==0:
            L[i] = L[i]*3
        else:
            L[i] = L[i]*5
    return(L)
        


    
    
def tupleMaker(*n):
    total = 0
    for i in n:
        total += i
    return total

def simpleCalculator(opr:str, num1:int,num2:int):
    if (opr =="+"):
        return (num1)+(num2)
    elif (opr=="-"):
        return (num1)-(num2)
    elif (opr=="*"):
        return (num1)*(num2)
    elif (opr=="/"):
        return (num1)/(num2)
    elif (opr=="**"):
        return (num1)**(num2)
    else:
        return("You have enter invalid oprerator or invalid number!!!")
    
    
def checkLenOfStr(str1:str,str2:str):
    if (len(str1)==len(str2)):
        return True
    else:
        return False
    
def sqrtOfNthRoot( number:int,root:int=2):
    result = number**(1/root)
    return result

def randomThreeNumber(firstNumber:int, secondNumber:int):
    numberList = []
    def generateNumber(firstNumber, secondNumber):
        value = random.randint(firstNumber,secondNumber)
        return value
    
    for i in range(0,3):
        value = generateNumber(firstNumber,secondNumber)
        numberList.append(value)
    return numberList


def checkMinimumOnesDigit(firstNumber:int, secondNumber:int):
    str1 = str(firstNumber)
    str2 = str(secondNumber)
    if(str1[-1]>str2[-1]):
        return int(str1)
    elif(str1[-1]<str2[-1]):
        return int(str2)
    else:
        return("Numbers have equal one's digits.")
    
def generateSeries(firstNumber:int, secondNumber:int):
    equalPart = (firstNumber + secondNumber)/4
    seriesList = []
    seriesList.append(firstNumber)
    number= firstNumber
    for i in range(1,4):
        number += equalPart
        seriesList.append(number)
    return seriesList


def getWeatherData(city:str):
    key = os.getenv("API_KEY")
    response = r.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric")
    data =response.json()
    temp = round((data["main"]["temp"])-1,2)
    str = f"Current weather of {city} is {temp}°C."
    return str


def readFile(path:str, mode:str):
    fileHandler = open(path,mode)
    data = fileHandler.read()
    print(data)
    fileHandler.close()

# readFile("hii.txt","r")

# def openCV():
#     face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#     webcam = cv2.VideoCapture(0)  # 0 for webcam, or use 'video.mp4'

#     while True:
#         _,img = webcam.read()
#         cv2.imshow("Face Detection",img)
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray,1.5, 4)
#         for(x,y,w,h)in faces:
#             cv2.rectangle(img, (x,y), ())
#         key = cv2.waitKey(10)
#         if key ==27:
#             break
#     webcam.release()
#     cv2.destroyAllWindows()
    
# openCV()
    
    
def countLinesWithSpecificWord(word:str , fileName:str):
    fileHandler = open(fileName,"r")
    strList  = fileHandler.readlines()
    count = 0
    def check(wordList):
        for i in wordList:
            if i == word.upper() or i == word.lower() or i == word.capitalize():
                return True
    for i in strList:
        wordList = i.split()
        if check(wordList):
            count +=1       
    print(count)

countLinesWithSpecificWord("it","start.txt")

def countWord(word:str,fileName:str):
    fileHandler = open(fileName,"r")
    
    #Method 1 -->>
        #data = fileHandler.read()
        # wordList = data.split()
        # count = 0
        # for i in wordList:
        #      if i == word.upper() or i == word.lower() or i == word.capitalize():
        #          count +=1
        # print(count)
        
        
    #Method 2 -->>
        # str = " "
        # count = 0
        # while str:
        #     str = fileHandler.readline()
        #     wordList = str.split()
        #     for i in wordList:
        #            if i == word.upper() or i == word.lower() or i == word.capitalize():
        #               count +=1
        # print(count)
        
        
        
    #Method 3 -->>
    lineList = fileHandler.readlines()
    count = 0
    for i in lineList:
        wordList = i.split()
        for j in wordList:
            if j == word.upper() or j == word.lower() or j == word.capitalize():
                       count +=1
    print(count)
 
 
 
 
  
    

def countVowelsAndConsonant(fileName:str):
    fileHandler = open(fileName, "r")
    data  = fileHandler.read()
    def charList(data:str):
        charList = []
        wtSpaceStr = data.replace(" ","")
        for i in wtSpaceStr:
            charList.append(i)
        return charList
    vowelList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    consonantList = [c for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' if c.lower() not in 'aeiou']
    def specialChar():
        listSpecialChar = list(string.punctuation)
        for i in ["â","€","”","™"]:
            listSpecialChar.append(i)
        return listSpecialChar
    specialCharList =specialChar()
    whiteSpaceChar = list(string.whitespace)
    numberList = ["0","1","2","3","4","5","6","7","8","9"]
    countVowel = 0
    countConsonant = 0
    countSpecialChar = 0
    countWhiteSpace = 0
    countNumber =0
    for i in charList(data):
        if i in vowelList:
            countVowel += 1
        elif i in consonantList:
            countConsonant +=1
        elif i in specialCharList:
            countSpecialChar +=1
        elif i in whiteSpaceChar:
            countWhiteSpace += 1
        elif i in numberList:
            countNumber +=1
        else:
            print(f"Error in ${i}")
    
        
    detail = {
        "Vowels":countVowel,
        "Consonants":countConsonant,
        "SpecialCharacters":countSpecialChar,
        "WhitespaceCharacters":countWhiteSpace,
        "Numbers":countNumber
    }
    jsonData = json.dumps(detail)
    return jsonData

detail =countVowelsAndConsonant("start.txt")

T-9[-E0]]=0E0S0EW-RW[9WOWORP[=-NB9E0-L]]

