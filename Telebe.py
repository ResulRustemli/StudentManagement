allStudents = []

class Telebe:
    def __init__(self,_id,_name,_surname,_email,_contact):
        self.id=_id
        self.name=_name
        self.surname=_surname
        self.email=_email
        self.contact=_contact
        
    def showData(self):
        print(f"ID: {self.id} Name: {self.name} Surname: {self.surname} Email: {self.email} Contact: {self.contact}")

print("Telebe Melumat Sistemine Xosh Gelmishiniz")

def start():
    xususiEmr=int(input("""
    Asagdaki Emrlerden Birini Secin:

    1.Yeni tələbə əlavə edilməsi
    2.Tələbə koduna görə tələbə məlumatlarının silinməsi
    3.Tələbə koduna görə tələbə məlumatlarının dəyişdirilməsi
    4.Tələbə adına görə tələbə məlumatlarının göstərilməsi
    5.Bütün tələbə məlumatlarının göstərilməsi 

"""))
    if xususiEmr==1:
        telebeyeVerilenAd=input("Telebenin Databasedeki Adini daxil edin:  ")
        addStudent(telebeyeVerilenAd)
        start()
      
    elif xususiEmr==2:
        delStudentInfo()
    elif xususiEmr==3:
        changestudentInfo()
    elif xususiEmr==4:
        telebeninAdiInfo=input("Gostermek istediyiniz adi daxil edin:  ")
        showStudentInfo(telebeninAdiInfo)
        start()
        showStudentInfo()
    elif xususiEmr==5:
        showFullData()
        start()
    else:
        print("Duzgun Daxil Edin!")

def addStudent(telebeninDatabaseAdi):
    telebe_id= int(input("Telebe ID-si daxil edin: "))
    telebe_ad= input("Adini daxil edin: ")
    telebe_soyad= input("Soyadini daxil edin: ")
    telebe_email= input("Emaili daxil edin: ")
    telebe_contact= int(input("Nomreni daxil edin: "))
    
    telebeninDatabaseAdi=Telebe(telebe_id, telebe_ad, telebe_soyad, telebe_email, telebe_contact)
    allStudents.append(telebeninDatabaseAdi)
    print(f"{telebeninDatabaseAdi} adli telebe elave olundu")

    


def delStudentInfo():

    pass

def changestudentInfo():
    pass

def showStudentInfo(telebe_adi):
     for index in allStudents:
        if telebe_adi==index.name:
            print(f"ID:{index.id} / Name:{index.name} / Surname:{index.surname} / Email:{index.email} / Contact:{index.contact}")

def showFullData():
      for allData in allStudents:
        for key, value in allData.__dict__.items():
            print(f"{key} => {value}")
   

start()





