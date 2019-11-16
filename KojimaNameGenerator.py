Prefix = ""
Suffix = ""
Final_Name = ""
Personal_Info = {"Name" : "",
             "Occupation" : "",
             "Pet" : "",
             "Childhood" : "",
             "Stab_Object" : "",
             "Talent" : "",
             "Carrots" : "",
             "Intan_Fear" : "",
             "Tan_Fear" : "",
             "Last_Thing" : "",
             "Body_State" : "",
             "Matter" : "",
             "Name_Sound" : "",
             "Zodiac" : "",
             "Personality" : ""}

Kojima_Info = {"Film_Char" : "",
               "Kubrick" : "",
               "Joy_Div" : "",
               "NPR" : "",
               "War_Is_Bad" : "",
               "Mikkelsen" : ""}

Dice_Result = 0

import random

def Roll_Dice(MaxNum):
    Dice_Outcome = random.randint(1, MaxNum)
    return Dice_Outcome

def Man_Condition():
    Value = Roll_Dice(4)
    if Value == 4:
        Suffix = "-man"
    else:
        Suffix = ""
    return Suffix

def Condition_Condition():
    Value = Roll_Dice(8)
    if Value == 6:
        Prefix = "Big"
        
    if Value == 7:
        Prefix = "Old"
       
    if Value == 8:
        Prefix = Personal_Info["Body_State"]
        
    else:
        Prefix = ""
        
    return Prefix
        
def Kojima_Condition():
    Value = Roll_Dice(100)
    if Value == 69:
        Special_Name = "Hideo Kojima"
    else:
        Special_Name = ""
    return Special_Name
    
def Name_Category():
    Value = Roll_Dice(20)
    
    if Value == 1:
        Category = "Normal"
    elif (Value >=2 and Value <=6):
        Category = "Occupational"
    elif (Value >=7 and Value <=10):
        Category = "Horny"
    elif (Value >=11 and Value <=13):
        Category = "The"
    elif (Value >=14 and Value <=17):
        Category = "Cool"
    elif (Value >=18 and Value <=19):
        Category = "Violent"
    else:
        Category = "Subtext"
        
    return Category
    

def Normal_Name(Special_Name_Check, Prefix, Suffix):
    Name = Personal_Info["Name"]
    Final_Name = Prefix + " " + Name + " " + Suffix
    if Special_Name_Check == "Hideo Kojima":
        Final_Name = Special_Name_Check
    
    return Final_Name

def Occupational_Name(Special_Name_Check, Prefix, Suffix):
    Last_Name = Personal_Info["Occupation"]
    Value = Roll_Dice(4)
    
    if Value == 1:
        First_Name = Personal_Info["Personality"]
    elif Value == 2:
        First_Name = Personal_Info["Talent"]
    elif Value == 3:
        First_Name = Personal_Info["Name_Sound"]
    else:
        First_Name = Kojima_Info["Film_Char"]
    
    Final_Name = Prefix + " " + First_Name + " " + Last_Name + " " + Suffix
    if Special_Name_Check == "Hideo Kojima":
        Final_Name = Special_Name_Check
    
    return Final_Name

def Horny_Name(Special_Name_Check, Prefix, Suffix):
    Last_Name = Personal_Info["Pet"]
    Value = Roll_Dice(4)
    
    if Value == 1:
        First_Name = Personal_Info["Matter"]
    elif Value == 2:
        First_Name = "Naked"
    elif Value == 3:
        First_Name = Personal_Info["Talent"]
    else:
        First_Name = Personal_Info["Zodiac"]
    
    Final_Name = Prefix + " " + First_Name + " " + Last_Name + " " + Suffix
    if Special_Name_Check == "Hideo Kojima":
        Final_Name = Special_Name_Check
    
    return Final_Name

def The_Name(Special_Name_Check, Prefix, Suffix):
    First_Name = "The "
    Value = Roll_Dice(4)
    
    if Value == 1:
        Last_Name = Personal_Info["Intan_Fear"]
    elif Value == 2:
        Last_Name = Personal_Info["Tan_Fear"]
    elif Value == 3:
        Last_Name = Personal_Info["Childhood"]
    else:
       Last_Name = Kojima_Info["War_Is_Bad"]
    
    Final_Name = First_Name + " " + Prefix + " " + Last_Name + " " + Suffix
    if Special_Name_Check == "Hideo Kojima":
        Final_Name = Special_Name_Check
    
    return Final_Name
    
def Cool_Name(Special_Name_Check, Prefix, Suffix):
    First_Name = Kojima_Info["Mikkelsen"]
    Value = Roll_Dice(6)
    
    if Value == 1:
        Last_Name = Kojima_Info["Kubrick"]
    elif Value == 2:
        Last_Name = Kojima_Info["War_Is_Bad"]
    elif Value == 3:
        Last_Name = Personal_Info["Joy_Div"]
    elif Value == 4:
        Last_Name = Personal_Info["Talent"]
    elif Value == 5:
        Last_Name = Personal_Info["Intan_Fear"]
    else:
        Last_Name = Personal_Info["Name_Sound"]
        
    Final_Name = Prefix + " " + First_Name + " " + Last_Name + " " + Suffix
    if Special_Name_Check == "Hideo Kojima":
        Final_Name = Special_Name_Check
    
    return Final_Name

def Violent_Name(Special_Name_Check, Prefix, Suffix):
    First_Name = Personal_Info["Stab_Object"]
    
    Value = Roll_Dice(4)
    
    if Value == 1:
        Last_Name = Kojima_Info["NPR"]
    elif Value == 2:
        Last_Name = Personal_Info["Matter"]
    elif Value == 3:
        Last_Name = Kojima_Info["War_Is_Bad"]
    else:
        Last_Name = Personal_Info["Tan_Fear"]
        
    Final_Name = Prefix + " " + First_Name + " " + Last_Name + " " + Suffix
    if Special_Name_Check == "Hideo Kojima":
        Final_Name = Special_Name_Check
    
    return Final_Name

def Subtext_Name(Special_Name_Check, Prefix, Suffix):
    Name = Personal_Info["Last_Thing"]
    
    Final_Name = Prefix + " " + Name + " " + Suffix
    if Special_Name_Check == "Hideo Kojima":
        Final_Name = Special_Name_Check
    
    return Final_Name

def Main():
    
    Suffix = Man_Condition()
    Prefix = Condition_Condition()
    Special_Name = Kojima_Condition()
    
    Category = Name_Category()
    
    if Category == "Normal":
        Finished_Name = Normal_Name(Special_Name, Prefix, Suffix)
    elif Category == "Occupational":
        Finished_Name = Occupational_Name(Special_Name, Prefix, Suffix)
    elif Category == "Horny":
        Finished_Name = Horny_Name(Special_Name, Prefix, Suffix)
    elif Category == "The":
        Finished_Name = The_Name(Special_Name, Prefix, Suffix)
    elif Category == "Cool":
        Finished_Name = Cool_Name(Special_Name, Prefix, Suffix)
    elif Category == "Violent":
        Finished_Name = Violent_Name(Special_Name, Prefix, Suffix)
    else:
        Finished_Name = Subtext_Name(Special_Name, Prefix, Suffix)
    
    return Finished_Name
    

# Actual Questions
Personal_Info["Name"] = str(input("What is your full name? "))
Personal_Info["Occupation"] = str(input("What is your occupation? (Single -er noun) "))
Personal_Info["Pet"] = str(input("What was your pet's specific breed/species? If you never had one just state the one you wish you had. "))
Personal_Info["Childhood"] = str(input("Your most embarassing childhood memory in TWO WORDS. "))
Personal_Info["Stab_Object"] = str(input("What is the object you’d least like to be stabbed by? "))
Personal_Info["Talent"] = str(input("What is something you are good at? (Verb ending in -ing) "))
Personal_Info["Carrots"] = str(input("How many carrots do you believe you could eat in one sitting, if someone,like, forced you to eat as many carrots as possible? "))
Personal_Info["Intan_Fear"] = str(input("What is your greatest intangible fear? (e.g. death, loneliness, fear itself) "))
Personal_Info["Tan_Fear"] = str(input("What is your greatest tangible fear? (e.g. horses) "))
Personal_Info["Last_Thing"] = str(input("What is the last thing you did before starting this worksheet? "))
Personal_Info["Body_State"] = str(input("What condition is your body currently in? (single word answer) "))
Personal_Info["Matter"] = str(input("Favorite state of matter? "))
Personal_Info["Name_Sound"] = str(input("A word your name kind of sounds like? (e.g. Brian -> Brain) "))
Personal_Info["Zodiac"] = str(input("What is your Zodiac sign? "))
Personal_Info["Personality"] = str(input("If you had to define your personality in one word, what would it be? "))
Kojima_Info["Film_Char"]= str(input("Who is your favorite film character? (NOTE: must be played by Kurt Russell) "))
Kojima_Info["Kubrick"]= str(input("What is the last word of the title of your favorite Kubrick film? "))
Kojima_Info["Joy_Div"]= str(input("What is the first word in the title of your favorite Joy Division album? "))
Kojima_Info["NPR"]= str(input("What is a scientific term you picked up from listening to NPR once? "))
Kojima_Info["War_Is_Bad"]= str(input("What is a piece of military hardware you think looks cool even though war is bad? "))
Kojima_Info["Mikkelsen"]= str(input("What is something you’d enjoy watching Mads Mikkelsen do? ONE WORD ONLY "))

# Run the program
Name = Main()
print(Name)

    
    
        