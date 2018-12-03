import urllib.request
from bs4 import BeautifulSoup

def get_daily_horoscope(sign):
    #get horoscope from website
    #https://www.astrology.com/horoscope/daily/SIGN.html
    #https://astrologyanswers.com/horoscopes/SIGN-daily-horoscope/
    response1 = urllib.request.urlopen("https://www.astrology.com/horoscope/daily/today/"+sign.lower()+".html")
    soup1 = BeautifulSoup(response1)
    data1 = soup1.html.body.findAll('p')
    horoscope1 = data1[0]

    response2 = urllib.request.urlopen("https://astrologyanswers.com/horoscopes/"+sign.lower()+"-daily-horoscope/")
    soup2 = BeautifulSoup(response2)
    data2 = soup2.html.body.findAll('p')
    horoscope2 = data2[0]

    print("Astrology.com: \n")
    print(horoscope1)
    print("\n\n")

    print("Astrology Answers: \n")
    print(horoscope2)
    print("\n\n")

def get_yesterdays_horoscope(sign):
    response1 = urllib.request.urlopen("https://www.astrology.com/horoscope/daily/yesterday/"+sign.lower()+".html")
    soup1 = BeautifulSoup(response1)
    data1 = soup1.html.body.findAll('p')
    horoscope1 = data1[0]
    print("Astrology.com: \n")
    print(horoscope1)
    print("\n\n")

    response2 = urllib.request.urlopen("https://astrologyanswers.com/horoscopes/"+sign.lower()+"-daily-horoscope/yesterday/")
    soup2 = BeautifulSoup(response2)
    data2 = soup2.html.body.findAll('p')
    horoscope2 = data2[0]
    print("Astrology Answers: \n")
    print(horoscope2)
    print("\n\n")


def get_tomorrows_horoscope(sign):
    response1 = urllib.request.urlopen("https://www.astrology.com/horoscope/daily/tomorrow/"+sign.lower()+".html")
    soup1 = BeautifulSoup(response1)
    data1 = soup1.html.body.findAll('p')
    horoscope1 = data1[0]
    print("Astrology.com: \n")
    print(horoscope1)
    print("\n\n")

    response2 = urllib.request.urlopen("https://astrologyanswers.com/horoscopes/"+sign.lower()+"-daily-horoscope/tomorrow/")
    soup2 = BeautifulSoup(response2)
    data2 = soup2.html.body.findAll('p')
    horoscope2 = data2[0]
    print("Astrology Answers: \n")
    print(horoscope2)
    print("\n\n")

def show_zodiac_dates():
    print("\n\nLook for your birth date: ")
    print("Aries: March 21 - April 19")
    print("Taurus: April 20 - May 20")
    print("Gemini: May 21 - Jun 20")
    print("Cancer: June 21 - July 22")
    print("Leo: July 23 - August 22")
    print("Virgo: August 23 - September 22")
    print("Libra: September 23 - October 22")
    print("Scorpio: October 23 - November 21")
    print("Sagittarius: November 22 - December 21")
    print("Capricorn: December 22 - January 19")
    print("Aquarius: January 10 - February 18")
    print("Pisces: February 19 - March 20\n\n")


def check_zodiac_sign(function):
    choice = input("\nDo you know your zodiac sign? (Yes/No)\n")
    if choice.lower() == "yes":
        valid_signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra'
                       ,'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
        sign = input("Enter your zodiac sign: \n")

        if sign.lower() in valid_signs:
            function(sign)
        else:
            print("Check your spelling and re-enter your sign please.")
            check_zodiac_sign()
    elif choice.lower() == "no":
        show_zodiac_dates()
        check_zodiac_sign(function)
    else:
        print("Your input is invalid. Please try again, and make sure to answer yes or no.\n")
        check_zodiac_sign(function)

def check_chinese_sign(function):
    choice = input("Do you know your chinese zodiac sign? (Yes/No)\n")
    if choice.lower() == "yes":
        valid_signs = ['rat', 'ox', 'tiger', 'rabbit', 'dragon', 'snake',
                       'horse', 'sheep', 'monkey', 'rooster', 'dog', 'pig']
        sign = input("Please Enter your chinese zodiac sign: \n")

        if sign.lower() in valid_signs:
            function(sign)
        else:
            print("Please check the spelling of your sign, and enter it again.")
            check_chinese_sign(function)
    elif choice.lower() == "no":
        show_chinese_dates()
        check_chinese_sign(function)
    else:
        print("Your input is invalid. Please try again, and make sure to answer either yes or no.\n")
        check_chinese_sign(function)


def get_chinese_horoscope(sign):
    #https://www.astrology.com/horoscope/daily-chinese/SIGN.html
    response = urllib.request.urlopen("https://www.astrology.com/horoscope/daily-chinese/"+sign.lower()+".html")
    soup = BeautifulSoup(response)
    data = soup.findAll('p')
    horoscope = data[0]

    print("Astrology.com: ")
    print(horoscope)
    print("\n\n")


def show_chinese_dates():
    print("Look for your birth year: ")
    print("Rat: 2008, 1996, 1984, 1972, 1960, 1948, 1936")
    print("Ox: 2009, 1997, 1985, 1973, 1961, 1949, 1937")
    print("Tiger: 2010, 1998, 1986, 1974, 1962, 1950, 1938")
    print("Rabbit: 2011, 1999, 1987, 1975, 1963, 1951, 1939")
    print("Dragon: 2012, 2000, 1988, 1976, 1964, 1952, 1940")
    print("Snake: 2013, 2001, 1989, 1977, 1965, 1953, 1941")
    print("Horse: 2014, 2002, 1990, 1978, 1966, 1954, 1942")
    print("Sheep: 2015, 2003, 1991, 1979, 1967, 1955, 1943")
    print("Monkey: 2016, 2004, 1992, 1980, 1968, 1956, 1944")
    print("Rooster: 2017, 2005, 1993, 1981, 1969, 1957, 1945")
    print("Dog: 2018, 2006, 1994, 1982, 1970, 1958, 1946")
    print("Pig: 2019, 2007, 1995, 1983, 1971, 1959, 1947")


def present_prompt():
    #Ask the user if they would like their horoscope
    #Then ask what sign (star, chinese, hindu, celtic)
    print("\n\nWelcome! Please enter a valid choice from the menu below:")

    choice = input("1)Daily Zodiac Horoscope\n2)Daily Chinese Horocope\n3)Yesterday's Zodiac Horoscope\n4)Tomorrow's Zodiac Horoscope\n5)Quit\n")

    if choice == '1':
        check_zodiac_sign(get_daily_horoscope)
    elif choice == '2':
        check_chinese_sign(get_chinese_horoscope)
    elif choice == '3':
        check_zodiac_sign(get_yesterdays_horoscope)
    elif choice == '4':
        check_zodiac_sign(get_tomorrows_horoscope)
    elif choice == '5':
        print("Goodbye!")
        return
    else:
        print("That wasn't a valid choice. Please try again")
        present_prompt()

    choice = input("Would you like to read it again?(Yes/No)\n")
    if choice.lower() == "yes":
        present_prompt()
    else:
        print("Goodbye!")


def __main__():
    present_prompt()

