# !usr/bin/python3.8

# Tree - Water - Food  - Wind - Pond_Kg
# Kg - g - centimeter - centimeter_change - Meter_chenage_DC
# Dc_chenage_Mter - Liter - mCubic_centimeters - Earth's Humans

# Create Def

from time import sleep

class star:
    def __init__(
            self, man, Year, Water_day, Age, meal,
            Numberـofـtoiletsـperـday, Windـspeedـperـmeter,
            pond, kg, g, Metr, centimeters, DC, liter,
            mCubic, objects_, text, path, Minutes):
        pass

    def Tree(man: int, Year: int):
        # Assumption
        man_o2 = man * 730_000
        # The amount of oxygen that humans consume
        Tree_o2 = 400_000_000_000 * 1_314_000
        # The amount of oxygen that trees produce
        # Year
        man_o2ـyear = man * 730_000 * Year
        # The amount of oxygen that humans consume Year
        Tree_o2_year = 400_000_000_000 * 1_314_000 * Year
        # The amount of oxygen that trees produce Yea

        return f'''
    \33[1m
    \033[94m
    The amount of oxygen that humans consume : \33[31m{man_o2}
    \033[94mThe amount of oxygen that trees produce : \33[31m{Tree_o2} 
    \33[32m
    *******************************************************************
    The amount of oxygen that humans consume Year: \33[31m{Year} : {man_o2ـyear}
    \33[32mThe amount of oxygen that trees produce Year: \33[31m{Year} : {Tree_o2_year} 

    \033[1mOwner : \033[35mhttps://github.com/ahSiber/
    '''
    # Tree(1000,199)

    def Water(Water_day: int, Age):
        # The amount of water entering should be in liters
        day_year = Water_day * 365
        # Water consumption per year
        year_all = day_year * 7_913_711_000
        # The amount of water consumed by the whole world based on your water consumption per day
        Age_wather = day_year * Age
        # you in \33[31m{Age} \033[34m, \33[31m{Age_wather} \033[34mYou have consumed
        return f"""
    \033[34m
    Water consumption per year : \33[31m{day_year} 
    \033[34mThe amount of water consumed by the whole world based on your water consumption per day : \33[31m{year_all} 
    \033[34myou in \33[31m{Age} \033[34m, \33[31m{Age_wather} \033[34mYou have consumed. 

    \033[1mOwner : \033[35mhttps://github.com/ahSiber/ 

    """

    # Water(10,12)

    def Food(meal: int, Age: int):
        food = meal * 365
        age = food * Age
        return f"""
    \33[32m
    Number of meals you eat per year (approximate) : \33[31m {food} 
    \33[32mEat a few meals in your lifetime (approximate) : \33[31m {age} 

    \033[1mOwner : \033[35mhttps://github.com/ahSiber/
    """

    # print(Food(3 , 16))

    def wc(Numberـofـtoiletsـperـday: int, age: int):
        Numberـof = Numberـofـtoiletsـperـday * 365
        # WC in Year
        number_of_age = Numberـof * age
        # Number of toilets you went to during your lifetime (approximate)
        return f"""
    \33[33m
    WC in Year : \33[31m{Numberـof} 
    \33[33mNumber of toilets you went to during your lifetime (approximate) : \33[31m{number_of_age} 

    \033[1mOwner : \033[35mhttps://github.com/ahSiber/
    """

    # print(wc(3 , 16))

    def Wind(Windـspeedـperـmeter: int):
        # Wind speed per meter
        Windـspeedـperـ = Windـspeedـperـmeter * 3.6
        # Wind speed in meters per second
        WindSpedn = Windـspeedـperـmeter / 3.6
        return F"""

    \33[37mWind speed per meter : \33[31m{Windـspeedـperـmeter} 
    \33[37mWind speed in meters per second : \33[31m{WindSpedn} 

    \033[1mOwner : \033[35mhttps://github.com/ahSiber/
    """

    # print(Wind(120))

    def Pond_Kg(pond: int):
        all_pond = pond * 0.453592
        # The amount obtained from pounds to kilograms
        pond_by_kg = pond * 453_592
        # The pound is equal
        return f"""
    \033[96m
    The amount obtained from pounds to kilograms : \33[31m{all_pond} Kg
    {pond} \033[96mThe pound is equal : \33[31m{pond_by_kg} g

    \033[1mOwner : \033[35mhttps://github.com/ahSiber/
    """
    # Pond_Kg(10)

    def Kg(kg: int):
        # Convert kilograms to grams
        gr = kg * 1000
        return f"\33[31m{gr} \033[35mg \033[34m<'https://github.com/ahSiber'>"

    def g(g: int):
        # Convert grams to kilograms
        kg_end = g / 1000
        return f"\33[31m{kg_end} \033[35mgrms \033[34m<'https://github.com/ahSiber'>"

    def centimeter(Metr):
        # Convert meters to centimeters
        mater = Metr * 100
        return F"\33[31m{mater} \033[35mcentimeters \033[34m<'https://github.com/ahSiber'>"

    def centimeter_change(centimeters):
        # Convert centimeters to meters
        mater = centimeters / 100
        return F"\33[31m{mater} \033[35mmeters \033[34m<'https://github.com/ahSiber'>"

    def Meter_chenage_DC(Meter):
        # Convert meters to decimetres
        Dc_meter = Meter * 10
        return f"\33[31m{Dc_meter} \033[35mDecimeter \033[34m<'https://github.com/ahSiber'>"

    def Dc_chenage_Mter(DC):
        # Convert decimeters to meters
        Dc_meter = DC / 10
        return f"\33[31m{Dc_meter} \033[35m Mter \033[34m<'https://github.com/ahSiber'>"

    def Liter(liter):
        # Convert cubic meters to cubic centimeters
        liters = liter * 1000000
        return f"\33[31m{liters}\033[35mCubic centimeters \033[34m<'https://github.com/ahSiber'>"

    def mCubic_centimeters(mCubic):
        # Convert cubic centimeters to cubic meters
        mClub = mCubic / 1000000
        return f"\33[31m{mClub} Liter \033[34m<'https://github.com/ahSiber'>"

    # print(mCubic_centimeters(10))

    def Decomposition_of_objects(objects_):
        obje = ['banana', "Plant", "Paper", "cotton", 'Rope']
        none = ['Clothing', 'shoes', 'Cigarettes']
        if objects_ == obje[0]:
            return "\33[31m2 Day and 10 day"
        elif objects_ == obje[1]:
            return "\33[31m2 month and 3 month"
        elif objects_ == obje[2]:
            return "\33[31m2 month and 5 month"
        elif objects_ == obje[3]:
            return "\33[31m1 month and 5 month"
        elif objects_ == obje[4]:
            return "\33[31m3 month and 1 year"
        elif objects_ == "Bottle":
            return "\33[31mIt does not decompose"
        elif objects_ == 'Glass':
            return "\33[31mIt does not decompose"
        elif objects_ == none[0]:
            return '\33[31m500 and 800 years'
        elif objects_ == none[1]:
            return '\33[31m20 and 50 years'
        elif objects_ == none[2]:
            return "\33[31m1 and 12 years"

    # print(Decomposition_of_objects('banana'))

    def serch_fars(text: str, path):
        with open('./fa_IR.dic', 'r') as red_file:
            text_send_def = red_file.read()
            if text in text_send_def:
                return f"\033[32mTrue {text} in list db"
            else:
                return "\033[31mnot fond"

    # Not support Fasri
    # print(serch_fars('hello' , "./color_random_txt/Main.file.py"))

    def secـMinu(Seconds):
        # Convert seconds to minutes
        sec = Seconds / 60
        int_sec = int(sec)
        return f"\033[31m{int_sec} \33[34mMinutes"

    # print(secـMinu(60))

    def Minu_sec(Minutes):
        # Convert minutes to seconds
        Minu = Minutes * 60
        int_Minu = int(Minu)
        return f"\033[31m{int_Minu} \33[34mSecond"

    # print(Minu_sec(10))

    def sun_proton(secands:float): 
        from math import pow 
        proton = 8.9 * pow(10,56) 
        return f"\033[31m {secands} Equivalent {proton * secands} Perton will be released." 

    # print(star.sun_proton(1))

    def Waterـsolubleـsolids(liter:float): 
        oz = 1.2
        # 34-35 g (1.2 oz) per liter
        return f"\033[31mValue obtained : {liter * oz}" 
    
    def covid_19(): 
        
        from bs4 import BeautifulSoup 
        from requests import get ,post
        # Metakhanid Library Requirements
        send_requsts = post(url="https://www.worldometers.info/coronavirus/?Si") 
        bs3 = BeautifulSoup(send_requsts.text , "html.parser")
        # Submit requests and extract requests from the desired site
        number = bs3.find(class_="maincounter-number") 

        covid_20 = ['']
        for x in number: 
            covid_20.append(x.text)
        number_orginal = covid_20[2]  
        
        # Print requests in output
        return(f"\033[31mStatistics of infected people in the world : {number_orginal}")
   
    def mHz(mHz):return (f"\033[31m {mHz} mHz equals : {mHz * 1}ks")
    def Hz(hz):return (f"\033[31m {hz} hz equals : {hz * 1}s" )
    def KHz(khz):return (f"\033[31m {khz} equals : {khz * 1}ms") 
    def Mhz(mhz):return (f"\033[31m {mhz} equals : {mhz * 1}μs")
    def Ghz(ghz):return(F"\033[31m {ghz} equals : {ghz * 1}ns")
    def THz(thz):return(f"\033[31m {thz} equals : {thz *1}ps")    

    def signas_info():
        return (f"""\033[31m
        Any 1 mhz equals : 1ks
        Any 1 hz equals : 1s
        Any 1 khz equals : 1ms
        Any 1 mhx equals : 1μs
        Any 1 ghz equals : 1ns
        Any 1 thz equals : 1ps
        """)

    # print(star.signas_info())
