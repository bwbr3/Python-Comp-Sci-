print('****Welcome to the Lab grade calculator!****')

name = input('Who are you calculating grades for?')

lab_grade = float(input('Enter the Labs Grade? ==>'))

if lab_grade < 100:
    print('The lab value should have been 100 or less. It has been changed to 100.')
    lab_grade = 100
          
elif lab_grade < 0:
    print('')

    lab_grade = 0 
    
lab_exam = float(input('Enter the exams grade? ==>'))


if lab_exam < 100:
    print('The exam value should have been zero or greater. It has changed to 0.')
    lab_exam = 0

att = float(input('Enter the attentendce grade? ==>'))

if att < 100:
            print('We set it to 100')
            att = 100
we_gr = lab_grade * 0.7 + lab_exam * 0.2 + att * 0.1

if we_gr >= 90:
    print('A')
elif we_gr >= 80:
    print('B')
elif we_gr >= 70:
    print('C')
elif we_gr >= 60:
    print('D')
elif we_gr  < 60:
    print('F')

print('The weighted grade for',name,'is',we_gr,)
    
    
    

    

      








                      
          
