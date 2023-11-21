
import pprint as pp
import json

if __name__ == '__main__':

    student_registry = {}
    sub_list = ['math', 'geo', 'lit']

    print("let's insert some student info:\n")

    i=0
    while True:
        stud_id = 'ID_%s'%i
        name= input('name?\n')
        if name == 'q':
            break
        student_registry[stud_id]={}
        student_registry[stud_id]['name'] = name
        student_registry[stud_id]['surname'] = input('surname?\n')
        for sub in sub_list:
            student_registry[stud_id][sub]=[]

            while True:
                grade = input('what is your %s grade?:\n'%sub)
                if grade == 'q':
                    break
                student_registry[stud_id][sub].append(int(grade))


        i+=1




    pp.pprint(student_registry)

    with open('students.json','w') as fp:
        json.dump(student_registry,fp)

    stud_reg = json.load(open('students.json'))
    val = '{"key":"value"}'


    #
    # for key, value in student_registry.items():
    #     grade_cnt = 0
    #     for sub in sub_list:
    #         grade_cnt+= len(value[sub])
    #         avg = sum(value[sub])/len(value[sub])
    #         k = sub +'_avg'
    #         student_registry[key][k]=avg
    #     student_registry[key]['grade_counts'] = grade_cnt

    # # Es2 *********+*********************************+
    #
    # students_registry = {}
    # subjects = ['math', 'literature', 'geography']
    # #each student has an ID a name and surname and a list of grades for each subject
    # num_students = 2
    #
    # registering_over = False
    #
    # print('Insert the students information to end any iterative input just press "q"\n')
    # i=1
    # while not registering_over:
    #     ID = 'ICSS_%s'%i
    #     name = input('Student Name\n')
    #     if name == 'q':
    #         break
    #
    #     sur = input('Student Surname\n')
    #     students_registry[ID]={}
    #     students_registry[ID]['Name']= name
    #     students_registry[ID]['Surname']= sur
    #
    #     for sub in subjects:
    #         print('Grades in %s'%sub)
    #         students_registry[ID][sub] = []
    #         while True:
    #             grade = input('insert %s grade:\n'%sub)
    #             if grade == 'q':
    #                 break
    #             students_registry[ID][sub].append(grade)
    #
    #
    #     if i == num_students:
    #         registering_over = True
    #     i+=1
    #
    # pp.pprint(students_registry)

    # Es2.1 *********+*********************************+
    #extract some statistics
