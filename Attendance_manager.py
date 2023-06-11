


# attendance manager

from tabulate import tabulate





no_of_subjects=["Transform Calculus, Fourier Series And Numerical Techniques 18MAT31 ","Data Structures and Applications 18CS32 ","Analog and Digital Electronics 18CS33 ","Computer Organization 18CS34 ","Software Engineering 18CS35 ","Discrete Mathematical Structures 18CS36 ","Constitution of India, Professional Ethics and Cyber Law 18CPC39 "]

no_of_labs=["Analog and Digital Electronics Laboratory 18CSL37 ","Data Structures Laboratory 18CSL38 "]
print("  ")

print(""" 
Wᴇʟᴄᴏᴍᴇ ᴛᴏ ᴀᴛᴛᴇɴᴅᴀɴᴄᴇ ᴍᴀɴᴀɢᴇʀ ᴠ1.0
""")
print(" ")
print("""\
░█████╗░████████╗████████╗███████╗███╗░░██╗██████╗░░█████╗░███╗░░██╗░█████╗░███████╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝████╗░██║██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔════╝
███████║░░░██║░░░░░░██║░░░█████╗░░██╔██╗██║██║░░██║███████║██╔██╗██║██║░░╚═╝█████╗░░
██╔══██║░░░██║░░░░░░██║░░░██╔══╝░░██║╚████║██║░░██║██╔══██║██║╚████║██║░░██╗██╔══╝░░
██║░░██║░░░██║░░░░░░██║░░░███████╗██║░╚███║██████╔╝██║░░██║██║░╚███║╚█████╔╝███████╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝

░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝
     
     ᴀᴛᴛᴇɴᴅᴀɴᴄᴇ ᴍᴀɴᴀɢᴇʀ
     """)
print("  ")
print("""
𝘤𝘩𝘦𝘤𝘬 𝘢𝘵𝘵𝘦𝘯𝘥𝘢𝘯𝘤𝘦 𝘧𝘰𝘳 𝘺𝘰𝘶𝘳 𝘪𝘯𝘵𝘦𝘳𝘯𝘢𝘭𝘴
""")
print("          ")
print("""Tʏᴘᴇ ʏ ғᴏʀ YES ᴀɴᴅ ɴ ғᴏʀ NO""")
print("")
s0=input("""
ᴄʜᴇᴄᴋ ᴀᴛᴛᴇɴᴅᴀɴᴄᴇ ғᴏʀ sᴜʙᴊᴇᴄᴛs ?
""")
print("")
l0=input("""
ᴄʜᴇᴄᴋ ᴀᴛᴛᴇɴᴅᴀɴᴄᴇ ғᴏʀ ʟᴀʙs ?
""")
print("")



def subject():
     s1=int(input(no_of_subjects[0]))
     print("          ")
     s2=int(input(no_of_subjects[1]))
     print("          ")
     s3=int(input(no_of_subjects[2]))
     print("          ")
     s4=int(input(no_of_subjects[3]))
     print("          ")
     s5= int(input(no_of_subjects[4]))
     print("          ")
     s6= int(input(no_of_subjects[5]))
     print("          ")
     s7=int(input(no_of_subjects[6]))
     print("          ")
     def formula(num):
      return (num / 12) * 100  # this is the formula


     subject_attendance= [s1,s2,s3,s4,s5,s6,s7]
     attendance_in_all_subjects= []
     for num in subject_attendance :
               attendance_in_all_subjects.append(formula(num))
     attendance_subj=['%.2f' % elem for elem in attendance_in_all_subjects]
     table_subjects= ["SUBJECTS", "ATTENDANCE (IN %)"]
     table_data=[no_of_subjects,attendance_subj]
     print("")
     print(tabulate([table_subjects,['Maths 18MAT31',attendance_subj[0]],['DSA 18CS32',attendance_subj[1]],['ADE 18CS33',attendance_subj[2]],['CO 18CS34',attendance_subj[3]],['SE 18CS35',attendance_subj[4]],['DMS 18CS36',attendance_subj[5]],['CPC 18CPC39',attendance_subj[6]]],tablefmt="fancy_grid"))
     print("")
     
 


def labs():
     l1=int(input(no_of_labs[0]))
     print("          ")
     l2=int(input(no_of_labs[1]))
     print("          ")
     lab_attendance=[l1,l2]
     def formula1(fun):
          return(fun/6)*100

     attendance_in_labs=[]

     for fun in lab_attendance :
          attendance_in_labs.append(formula1(fun))
     attendance_labs=['%.2f' % elem for elem in attendance_in_labs]
     table_labs=["LABS","ATTENDNCE (IN %)"]
     table_data=[no_of_labs,attendance_labs]
     print("")
     print(tabulate([table_labs,['ADE lab 18CSL37',attendance_labs[0]],['DSA lab 18CSL38',attendance_labs[1]]],tablefmt="fancy_grid"))
     
     print("")
   
          

def sub_and_lab():
     print("")
     subject()
     print("")
     labs()

if (s0=="y"or s0=="Y") and (l0=="y"or l0=="Y") :
     subject()
     labs()
elif (s0=="y"or s0=="Y") and (l0=="n"or l0=="N"):
     subject()
elif (s0=="N"or s0=="n") and (l0=="y"or l0=="Y"):
     labs()
elif (s0=="n"or s0=="N") and (l0=="n"or l0=="N"):
        

        print(""" 
        
ᴀᴛᴛᴇɴᴅᴀɴᴄᴇ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ
        """)

else:
     print("""
      ʏᴏᴜ ᴡɪʟʟ ʙᴇ ʀᴇᴅɪʀᴇᴄᴛᴇᴅ
      """)
     sub_and_lab()





print(""" 
        
████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗      ██╗░░░██╗░█████╗░██╗░░░██╗
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝      ╚██╗░██╔╝██╔══██╗██║░░░██║
░░░██║░░░███████║███████║██╔██╗██║█████═╝░      ░╚████╔╝░██║░░██║██║░░░██║
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░      ░░╚██╔╝░░██║░░██║██║░░░██║
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗      ░░░██║░░░╚█████╔╝╚██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝      ░░░╚═╝░░░░╚════╝░░╚═════╝░
        """)


input("""Pʀᴇss Eɴᴛᴇʀ ᴛᴏ ᴇxɪᴛ""")
