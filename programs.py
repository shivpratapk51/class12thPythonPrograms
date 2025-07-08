import random
import requests as r
from dotenv import load_dotenv
import os
import json
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


    
    
   


