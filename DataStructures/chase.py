"""

given year is leap year or not

validate
    - 4 digit number
    - leap = divisible by 4 and not divisible by 100
    - 400 is okay

    e.g 2400 is leap year
    2500 is not

    2504 is leap year

"""

class ErrorCode(Enum):
    NotFourDigit = 1
    DivisibleBy100 = 2
    Success = 0


def check_leap_year(n)->(bool,ErrorCode):

    # is it 4 digit and not staring with 0

    if n<1000 or n>9999:
        return False,ErrorCode.NotFourDigit
    
    if n%400==0:
        return True,ErrorCode.Success
    
    if n%4==0:
        if n%100==0:
            retu
    if n%100==0:
        return True,ErrorCode.Success
    

    return False,

def main():
    

    # build infrastruture - developer producticity, deployment CI/CD 
    # why they are failing
    # python, react js
    # tablue, grapana
    # 



    


    



