
import pprint as pp

if __name__ == '__main__':


    # Es2 *********+*********************************+

    students_registry = {}
    subjects = ['math', 'literature', 'geography']
    #each student has an ID a name and surname and a list of grades for each subject
    num_students = 2

    registering_over = False

    print('Insert the students information to end any iterative input just press "q"\n')
    i=1
    while not registering_over:
        ID = 'ICSS_%s'%i
        name = input('Student Name\n')
        if name == 'q':
            break

        sur = input('Student Surname\n')
        students_registry[ID]={}
        students_registry[ID]['Name']= name
        students_registry[ID]['Surname']= sur

        for sub in subjects:
            print('Grades in %s'%sub)
            students_registry[ID][sub] = []
            while True:
                grade = input('insert %s grade:\n'%sub)
                if grade == 'q':
                    break
                students_registry[ID][sub].append(grade)


        if i == num_students:
            registering_over = True
        i+=1

    pp.pprint(students_registry)

    # Es2.1 *********+*********************************+
    #extract some statistics
