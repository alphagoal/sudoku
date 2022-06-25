import time
import copy
from control import start
from solver_ver1 import print_board, confirm_change,  sqaure_list,column_list, ops,sol_bo,countdown



#If needed, make a better design on the strict rules of formatting check

# define problem
#prob=[[0,0,6,0,9,0,2,0,0],[0,0,0,7,0,2,0,0,0],[0,9,0,5,0,8,0,7,0],[9,0,0,0,3,0,0,0,6],[7,5,0,0,0,0,0,1,9],[1,0,0,0,4,0,0,0,5],[0,1,0,3,0,9,0,8,0],[0,0,0,2,0,1,0,0,0],[0,0,9,0,8,0,1,0,0]]
  #<--- This is deep copy (will not update any changes)
#org_bo=list(prob) or org_bo= prob.copy() <--- This is shallow copy (will reflect value change)
#org_bo=prob <--- This is clone (will reflect all change)


#Problem exist: When firstly type 2, then the wrong file name, then type case_2.txt, there will be error.
#Lesson: Remember for every recursion scenario, you need to have the right return value or treatment
#--- applying all to "try...except", "if ...elif...else"

#start()
prob=start()

while prob ==False:
    prob=start()

if prob!="end":
    org_bo=copy.deepcopy(prob)

    print("\nsudoku challenge - original board:".upper(),"\n")
    print_board(prob)

    input("\nPlease press 'Enter' to start analyze ......")

    start=time.time()

    bo_sol=sol_bo(prob)

    print("")
    print("\nsudoku challenge - original board:".upper(),"\n")
    print_board(org_bo)
    print("\nsudoku challenge - solution:".upper(),"\n")

    print_board(bo_sol)
    print("")
    duration = round(time.time()-start,2)
    print(f"[Finished in {duration} seconds]" )

    input("\nPlease press 'Enter' to exit ......")
    print("\n\n\n~~ Bye Bye ~~\n\n\n")
    #time.sleep(3)
    countdown(5)





"""
prob_sq=sqaure_list(prob)
prob_col=column_list(prob)

print("")
print("Confirming if the values need changes...\n(0=No; 1=Yes)\n")
confirm_list=confirm_change(prob)
count_line=0
for line in confirm_list:
    count_line+=1
    print(f"Confirm Row {count_line}:",line)

print("\n")
print("Analyzing squares...")
count_line=0
for line in prob_sq:
    count_line+=1
    print(f"Square {count_line} is:",line)

print("")
print("Analyzing columns...")
count_line=0
for line in prob_col:
    count_line+=1
    print(f"Column {count_line} is:",line)
print("")

"""
