
def L1aL2sL3aAZ(name):
    name[1]='ُ'
    name[3]='َ'
    name[7]=''
    name1= name.insert(4, 'يْ')
    name[10]= ''
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
    name[6]= 'َ'
    name[7]= 'ة'
    name[8]= ''
    name[9]= ''
    name[10]= ''
    name2 =str.join(name)
    print("صيغة الترخيم    "+name2)

def  MoNsL1aL2eL3(name_1):
    name_1[9]=''
    name_1[2]= name_1[4]
    name_1[3]=  name_1[5]
    name_1[4] =name_1[6]
    name_1[5]=name_1[7]
    name_1[6]= name_1[8]
    name_1[7] =name_1[9]
    name_1[8]= ''
    name_1[9] = ''
    name1= name_1.insert(4, 'ي')
    name1= name_1.insert(5, 'ْ')
    str =""
    name1 =str.join(name_1)
    print("صيغة التصغير   " +name1)
    name1= name_1.insert(8, 'ي')
    name1= name_1.insert(9,'')
    str =""
    name1 =str.join(name_1)
    print("صيغة التصغير   " +name1)

    
def MoNsL1aL2eL3_2(name_2):
        name_2[9]=''
        name_2[0]= name_2[4]
        name_2[1]=  'ُ'
        name_2[2] =name_2[6]
        name_2[3]='َ'
        name_2[4]= name_2[8]
        name_2[5] =name_2[9]
        name_2[6]= ''
        name_2[7] = ''
        name_2[8]= ''
        name_2[9] = ''
        name3= name_2.insert(4, 'ي')
        name3= name_2.insert(5, 'ْ')
        str =""
        name3 =str.join(name_2)
        print("صيغة الترخيم    "+name3)
    
def L1oL2aYsL3eL4 (name):
    if(name[5]=='ّ'):
        name[1]='ُ'
        name[3]='َ'
        name[5]='ِ'
        name[6]=''
        name[7] = name[len(name)-2]
        name1= name.insert(4, 'ي')
        name1= name.insert(5, 'ْ')
        str =""
        name1 =str.join(name)
        print("صيغة التصغير   " +name1)

    else:
        name[1]='ُ'
        name[3]='َ'
        name[5]='ِ'
        name[7] = ''
        name1= name.insert(4, 'ي')
        name1= name.insert(5, 'ْ')
        str =""
        name1 =str.join(name)
        print("صيغة التصغير   " +name1)
def L1oL2aYsL3eUL4(name):
    name[1]='ُ'
    name[3]='َ'
    name[5]='ِ'
    name[9]=''
    name[8]=''
    name1= name.insert(4, 'ي')
    name1= name.insert(5, 'ْ')
    name1= name.insert(8, 'ي')
    name1= name.insert(9,'')
    name[11]=''
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def L1oL2aYsL3eUL4_2(name):
    name[1]='ُ'
    name[3]='َ'
    name[5]='ِ'
    name[9]=''
    name[8]=''
    name1= name.insert(4, 'ي')
    name1= name.insert(5, 'ْ')
    name[10]=''
    name[11]=''
    name[len(name)-3]=''
    str =""
    name1 =str.join(name) 
    print("صيغة التصغير    "+name1)   
def L1oL2aYsL3aH(name):
    name[1]='ُ'
    name[3]='َ'
    name[5]='َ'
    name1= name.insert(4, 'ي')
    name1= name.insert(5, 'ْ')
    name1= name.insert(8, 'ة')
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def L1oL2aYsL3(name):
    name[1]='ُ'
    name[3]='َ'
    name[5]=''
    name1= name.insert(4, 'ي')
    name1= name.insert(5, 'ْ')
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def L1oUaYsL3aH(name):
    name[1]='ُ'
    name[3]='َ'
    name[5]='َ'
    name1= name.insert(4, 'ي')
    name1= name.insert(5, 'ْ')
    name1= name.insert(8, 'ة')
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def L1oOaYsL3aH(name):
    name[1]='ُ'
    name[3]='ْ'
    name[5]='َ'
    name1= name.insert(2, 'و')
    name1= name.insert(3, 'َ')
    name1= name.insert(8, 'ة')
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def L1oOaYsL3aH_2(name):
    name[1]='ُ'
    name[3]='َ'
    name[2]='و'
    name1= name.insert(4, 'ي')
    name1= name.insert(5, 'ْ')
    name[7]='َ'
    name1= name.insert(8, 'ة')
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def L1oUaYsL3 (name):
    name[1]='ُ'
    name[3]='َ'
    name[5]=''
    name1= name.insert(4, 'ي')
    name1= name.insert(5, 'ْ')
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def L1oOaYsL3_2(name):
    name[1]='ُ'
    name[3]='َ'
    name[2]='ي'
    name[5]=''
    name1= name.insert(4, 'ي')
    name1= name.insert(5, 'ْ')
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def L1oUaYsL3_2(name):
    name[1]='ُ'
    name[3]='َ'
    name[2]='و'
    name[5]=''
    name1= name.insert(4, 'ي')
    name1= name.insert(5, 'ْ')
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def AAoL2aYsL3aH(name):
    name[1]='ُ'
    name[3]='َ'
    name[5]='َ'
    name1= name.insert(4, 'ي')
    name1= name.insert(5, 'ْ')
    name1= name.insert(8, 'ة')
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def AAoL2aYsL3 (name):
    name[1]='ُ'
    name[3]='َ'
    name[5]=''
    name1= name.insert(4, 'ي')
    name1= name.insert(5, 'ْ')
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def L1oL2aYsL2aH(name):
    name[1]='ُ'
    name[3]='َ'
    name1= name.insert(4, 'ي')
    name1= name.insert(5, 'ْ')
    name1= name.insert(6, name[2])
    name1= name.insert(7, 'َ')
    name1= name.insert(8, 'ة')
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def L1oL2aYsL2(name):
    name[1]='ُ'
    name[3]='َ'
    name1= name.insert(4, 'ي')
    name1= name.insert(5, 'ْ')
    name1= name.insert(6, name[2])
    name1= name.insert(7, '')
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def L1oL2aYvaH(name):
    name[1]='ُ'
    name[3]='َ'
    name[4]='ي'
    name[5]='َّ'
    name1= name.insert(6, 'ة')
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)
def L1oL2aYv (name):
    name[1]='ُ'
    name[3]='َ'
    name[4]='ي'
    name[5]='ّ'
    str =""
    name1 =str.join(name)
    print("صيغة التصغير   " +name1)

name = input("  ادخل الاسم الذي تريد تصغيره أو صفر للخروج ")
list_name = list(name)
list_name_2 = list(name)
while(name != '٠'):

 if (len(name)==6 or name[3]=='ّ'):
    input_1 = input("ادخل ١ إذا كان المدخل مؤنث و٢ إذا كان المدخل مذكر ")
    if (input_1 == "١"):
    
        if( name[2]=='و' or name[2]== 'ي'):
         input_2 = input("ادخل ١ اذا كانت الياء أصيلة و ٢ إذا كانت العين أصلها واو")
         if(input_2 == "١"):
            L1oUaYsL3aH(list_name)
         elif (input_2 == "٢"):
            L1oOaYsL3aH(list_name)
         else:
            print('المدخل غير صحيح')
        elif (name[2]== 'ا'):
            L1oOaYsL3aH_2(list_name)
        elif(name[0]== 'أ'):
            AAoL2aYsL3aH(list_name)
        elif(name[3]=='ّ'):
            L1oL2aYsL2aH(list_name)
        elif(name[4]=='ى'or name[4]=='ا' or name[4]=='و'):
            L1oL2aYvaH(list_name)
        else:
            L1oL2aYsL3aH(list_name)

          
       
    elif ( input_1=="٢"):
        if(  name[2]=='و' or name[2]== 'ي'):
          L1oUaYsL3(list_name)
        elif(name[2]== 'ا' ):
            input_2 = input("ادخل ١ اذا كانت أصل الألف واو  و ٢ إذا كانت أصل الألف ياء")
            if(input_2 == "٢"):
              L1oOaYsL3_2(list_name)
            elif (input_2 == "١"):
              L1oUaYsL3_2(list_name)
            else:
              print('المدخل غير صحيح')
        elif(name[0]== 'أ'):
            AAoL2aYsL3(list_name)
        elif(name[3]=='ّ'):
            L1oL2aYsL2(list_name)
        elif(name[4]=='ى'or name[4]=='ا' or name[4]=='و'):
            L1oL2aYv(list_name)
        else:
            L1oL2aYsL3(list_name)

    else:
        print('المدخل غير صحيح')


 else:
    
    if (len(name)> 8 ):
        if( name[8] == "ء"):
            L1aL2sL3aAZ(list_name) 
        elif (name[0]== 'م' and name[1]=='ُ'):
            MoNsL1aL2eL3(list_name)
            MoNsL1aL2eL3_2(list_name_2)
        elif(len(name)==10):
            L1oL2aYsL3eUL4(list_name)
            L1oL2aYsL3eUL4_2(list_name_2)
        elif(len(name)==9):
            L1oL2aYsL3eL4(list_name)

    elif(len(name)==8 ):
        L1oL2aYsL3eL4(list_name)


    else:
         print('المدخل غير صحيح')
         
 name = input("  ادخل الاسم الذي تريد تصغيره أو صفر للخروج ")
 list_name = list(name)
 list_name_2 = list(name)
 





    



