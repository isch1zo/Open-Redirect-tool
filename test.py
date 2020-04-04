
def CheckInterest(checkit):
    white_list = ['=http','%3dhttp','%3dhttps','=https','%3D%2F','=/']
    for i in white_list:
        if i.lower() in checkit.lower():
            return True
    
    print(checkit)
    return False

print(CheckInterest("https://ischizo.com?redirect=http://google.com"))
print(CheckInterest("https://ischizo.com?redirect%3dhttp://google.com"))
print(CheckInterest("https://ischizo.com?redirect%3dhttps://google.com"))
print(CheckInterest("https://ischizo.com?redirectgoogle.com")) #False
print(CheckInterest("https://ischizo.com?redirect=https://google.com"))
print(CheckInterest("https://ischizo.com?redirect=/google.com"))
print(CheckInterest("https://ischizo.com?redirect%3d%2fgoogle.com"))
