class Doctor():
    
    def _init_(self):
        print("This is class Doctor")
        
    def BMI(weight, height):
        bmi = weight/(height*height)
        print("Your BMI is "+str(bmi))
        
    def heart_rate(heart_rates):
        if(heart_rates>60 and heart_rates<100):
            print("Great your heart rate is normal")
        else:
            print("Your heart rate does not seem normal, please visit the clinic")

class Patient(Doctor):

     def _init_(self,name, weight, height, heart_rates):
         self.patient_name = name
         self.patient_weight = weight
         self.patient_height = height
         self.patient_heart_rates = heart_rates
     def healthCheck(self):
          print("\n Patient Name: ", self.patient_name)
          Doctor.BMI(self.patient_weight, self.patient_height)
          Doctor.heart_rate(self.patient_heart_rates)
          
          
patient1 = Paitent("Swasti", 30,0.9144, 80)
paitent1.healthCheck()

patient2 = Paitent("Saanvi", 40, 1, 120)
patient2.healthCheck()          

 """
Created on Wed Dec 22 19:08:29 2021

@author: Admin
"""

