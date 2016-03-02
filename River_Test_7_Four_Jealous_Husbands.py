#!/usr/bin/python3
import timeit
import time
time_begin = timeit.default_timer()

start = ["Husband1","Husband2","Husband3","Husband4","Wife1", "Wife2", "Wife3", "Wife4"]
middle = []
end = []
side = "s"
solution = []
final_solution = []

def print_game():
    this_step = "Start: %s" %(start) + "\n"
    this_step = this_step + "Middle: %s" %(middle) + "\n"
    this_step = this_step + "End: %s" %(end) + "\n" + side + "\n"
    print (this_step)

def if_win(end):
    if len(end)==8:
        return True
    return False

def find(x, lst):
    if x in lst:
        return True
    else:
        return False

def last_num(str):
    return str[-1] 

def check_if_ok(new_start, new_end, new_middle):
    for wife in new_start:
        if "Wife" in wife:
            for husband in new_start:
                if "Husband" in husband and last_num(husband)==last_num(wife):
                    break
            else:
                for other_husband in new_start:
                    if "Husband" in other_husband:
                        return False
    for wife in new_end:
        if "Wife" in wife:
            for husband in new_end:
                if "Husband" in husband and last_num(husband)==last_num(wife):
                    break
            else:
                for other_husband in new_end:
                    if "Husband" in other_husband:
                        return False

    for wife in new_middle:
        if "Wife" in wife:
            for husband in new_middle:
                if "Husband" in husband and last_num(husband)==last_num(wife):
                    break
            else:
                for other_husband in new_middle:
                    if "Husband" in other_husband:
                        return False
    return True
                
                        
def move(new_start, new_end, new_middle, side, direction, x, y=None):
    if x==None:
        return False
    if x!="Husband1" and x!="Husband2" and x!="Husband3" and x!="Husband4" and x!="Wife1" and x!="Wife2" and x!="Wife3" and x!="Wife4" and y!="Husband1"and y!="Husband2" and y!="Husband3" and y!="Husband4" and y!="Wife1" and y!="Wife2" and y != "Wife3" and y != "Wife4" and y!= None:
        return False
    if y!=None:
        if x!=y:
            if find(x, new_start) and find(y, new_start) and side=="s" and direction=="g" and len(new_middle)<=2:
                new_start.remove(x)
                new_start.remove(y)
                new_middle.append(x)
                new_middle.append(y)
                return "m"
            elif find(x, new_end) and find(y, new_end) and side=="e"and direction=="b"and len(new_middle)<=2:
                new_end.remove(x)
                new_end.remove(y)
                new_middle.append(x)
                new_middle.append(y)
                return "m"
            elif find(x, new_middle) and find(y,new_middle) and side=="m":
                new_middle.remove(x)
                new_middle.remove(y)
                if direction=="g":
                    new_end.append(x)
                    new_end.append(y)
                    return "e"
                elif direction=="b":
                    new_start.append(x)
                    new_start.append(y)
                    return "s"
                else:
                    return False
            else:
                return False
        else:
            return False
    elif ("Husband"in x or "Wife"in x) and y==None:
        if find(x, new_start) and side=="s" and direction=="g" and len(new_middle)<=3:
            new_start.remove(x)
            new_middle.append(x)
            return "m"
        elif find(x,new_end) and side=="e" and direction=="b" and len(new_middle)<=3:
            new_end.remove(x)
            new_middle.append(x)
            return "m"
        elif find(x,new_middle) and side=="m":
            new_middle.remove(x)
            if direction=="g":
                new_end.append(x)
                return "e"
            elif direction=="b":
                new_start.append(x)
                return "s"
            else:
                return False
        else:
            return False
    else:
        return False
##############################################        
'''while(not if_win(end)):
    print_game()
    input1 = input("input1: ")
    input2 = input("input2: ")
    if input2=="":
        input2=None
    if input1=="":
        input1=input2
        input2=None
    direction = input("direction: ") 
    new_start = [] + start
    new_end = [] + end
    new_middle = [] + middle
    new_side = move(new_start, new_end, new_middle, side, direction, input1, input2)
    if new_side == False:
        continue
    if check_if_ok(new_start, new_end, new_middle):
        start = [] + new_start
        end = [] + new_end
        middle = [] + new_middle
        side = "" + new_side
print("Congratulations, you won!")'''
##############################################
def step_to_list(step):
    outcome = [ [ ], [ ], [ ],""]
    line = 0
    for i in range(len(step)):
        if step[i]=="\n":
            line+=1
            continue
        if step[i].isnumeric():
            if step[i-1]=="e" and line<=2:
                outcome[line].append("Wife%s"%(step[i]))
            elif step[i-1]=="d" and line<=2:
                outcome[line].append("Husband%s"%(step[i]))
    outcome[3]=step[-2]
    for i in range(3):
        outcome[i].sort()    
    return outcome
#####
combination_codes = []
for a in range(1,5):
    for b in range(1,5):
        if b!=a:
            for c in range(1,5):
                if c!=a and c!=b:
                    for d in range(1,5):
                        if d!=a and d!=b and d!=c:
                            combination_codes.append(str(a)+str(b)+str(c)+str(d))
#####
def code_step(other_st,code):
    outcome = [[],[],[],other_st[3]]
    for i in range(3):
        for item in other_st[i]:
            if item[0]=="W":
                outcome[i].append("Wife%s"%( code[int(last_num(item))-1] ))
            elif item[0]=="H":
                outcome[i].append("Husband%s"%( code[int(last_num(item))-1] ))
        outcome[i].sort()
    return outcome
#####
def check_similar(step, step_list):
    st = [] + step_to_list(step)
    for item in step_list:
        other_st = [] + step_to_list(item)
        #'''
        need_to_check = True
        for i in range (0,3):
            if st[3]!=other_st[3]:
                need_to_check = False
                break
            if len(other_st[i])!=len(st[i]):
                need_to_check = False
                break
        if not need_to_check:
            continue
        #'''
        for code in combination_codes:
            if st==code_step(other_st,code):
                return True
    return False
#####
def steps_over_limit(new_steps, limit):
    if len(new_steps)>limit:
        return True
    return False        
#####    
def find_solution(start,end,middle,side,steps,limit):
    #
    if timeit.default_timer()-find_solution_time_begin > time_limit:
        return "Takes too long"
    #   
    start.sort()
    middle.sort()
    end.sort()
    this_step = "Start: %s" %(start) + "\n"
    this_step = this_step + "Middle: %s" %(middle) + "\n"
    this_step = this_step + "End: %s" %(end) + "\n" + side + "\n"
    if steps_over_limit(steps, limit):
        return
    if check_similar(this_step, steps):
        return
    if if_win(end):
        solution.insert(0,this_step)
        return True
    new_steps = [] + steps
    new_steps.append(this_step)
    
    if side=="s":
        for i in range(0, len(start)):
            new_start = [] + start
            new_end = [] + end
            new_middle = [] + middle
            new_side = move(new_start, new_end, new_middle, side, "g", start[i], None)
            if new_side != False and check_if_ok(new_start,new_end,new_middle):
                find_it = find_solution(new_start, new_end,new_middle,new_side, new_steps,limit)
                if find_it==True:
                    solution.insert(0,this_step)
                    return True
                elif find_it=="Takes too long":
                    return "Takes too long"
            for k in range(i+1, len(start)):
                loopnew_start = [] + start
                loopnew_end = [] + end
                loopnew_middle = [] + middle
                loopnew_side = move(loopnew_start, loopnew_end, loopnew_middle, side,"g", start[i], start[k])
                if loopnew_side != False and check_if_ok(loopnew_start,loopnew_end, loopnew_middle):
                    find_it =  find_solution(loopnew_start, loopnew_end, loopnew_middle, loopnew_side, new_steps,limit)
                    if find_it==True:
                        solution.insert(0,this_step)
                        return True
                    elif find_it=="Takes too long":
                        return "Takes too long"
    if side=="e":
        for i in range(0, len(end)):
            new_start = [] + start
            new_end = [] + end
            new_middle = [] + middle
            new_side = move(new_start, new_end, new_middle, side, "b", end[i], None)
            if new_side != False and check_if_ok(new_start,new_end,new_middle):
                find_it = find_solution(new_start, new_end,new_middle,new_side, new_steps,limit)
                if find_it==True:
                    solution.insert(0,this_step)
                    return True
                elif find_it=="Takes too long":
                    return "Takes too long"
            for k in range(i+1, len(end)):
                loopnew_start = [] + start
                loopnew_end = [] + end
                loopnew_middle = [] + middle
                loopnew_side = move(loopnew_start, loopnew_end, loopnew_middle, side,"b", end[i], end[k])
                if loopnew_side != False and check_if_ok(loopnew_start,loopnew_end, loopnew_middle):
                    find_it= find_solution(loopnew_start, loopnew_end, loopnew_middle, loopnew_side, new_steps,limit) 
                    if find_it==True:
                        solution.insert(0,this_step)
                        return True
                    elif find_it=="Takes too long":
                        return "Takes too long"
    if side=="m":
        for i in range(0, len(middle)):
            new_start = [] + start
            new_end = [] + end
            new_middle = [] + middle
            new_side = move(new_start, new_end, new_middle, side, "g", middle[i], None)
            if new_side != False and check_if_ok(new_start,new_end,new_middle):
                find_it= find_solution(new_start, new_end,new_middle,new_side, new_steps,limit) 
                if find_it==True:
                    solution.insert(0,this_step)
                    return True
                elif find_it=="Takes too long":
                    return "Takes too long"
            new_start = [] + start
            new_end = [] + end
            new_middle = [] + middle
            new_side = move(new_start, new_end, new_middle, side, "b", middle[i], None)
            if new_side != False and check_if_ok(new_start,new_end,new_middle):
                find_it= find_solution(new_start, new_end,new_middle,new_side, new_steps,limit)
                if find_it==True:
                    solution.insert(0,this_step)
                    return True
                elif find_it=="Takes too long":
                    return "Takes too long"
            for k in range(i+1, len(middle)):
                loopnew_start = [] + start
                loopnew_end = [] + end
                loopnew_middle = [] + middle
                loopnew_side = move(loopnew_start, loopnew_end, loopnew_middle, side,"g", middle[i], middle[k])
                if loopnew_side != False and check_if_ok(loopnew_start,loopnew_end, loopnew_middle):
                    find_it = find_solution(loopnew_start, loopnew_end, loopnew_middle, loopnew_side, new_steps,limit)
                    if find_it==True:
                        solution.insert(0,this_step)
                        return True
                    elif find_it=="Takes too long":
                        return "Takes too long"
                loopnew_start = [] + start
                loopnew_end = [] + end
                loopnew_middle = [] + middle
                loopnew_side = move(loopnew_start, loopnew_end, loopnew_middle, side,"b", middle[i], middle[k])
                if loopnew_side != False and check_if_ok(loopnew_start,loopnew_end, loopnew_middle):
                    find_it = find_solution(loopnew_start, loopnew_end, loopnew_middle, loopnew_side, new_steps,limit)
                    if find_it==True:
                        solution.insert(0,this_step)
                        return True
                    elif find_it=="Takes too long":
                        return "Takes too long"
##########################################################################
limit = 50
while(limit>0):
    print("Solving for move less than or equal to %s"%(limit),end="")
    loopbegin=timeit.default_timer()
    time_limit = 30
    find_solution_time_begin = timeit.default_timer()
    answer = find_solution(start,end,middle,side,[], limit)
    if answer==True:
        final_solution = [] + solution
        solution = []
        print(", takes %.3f seconds"%(timeit.default_timer()-loopbegin))
        limit=len(final_solution)-2
        continue
    elif answer=="Takes too long":
        print(", has stopped because it exceeds the %s-second-limit."%(time_limit)+"\n", end="\n")
        break
    print(", takes %.3f seconds"%(timeit.default_timer()-loopbegin))
    limit-=1
    
if len(final_solution)==0:
    print("No Solution")
else:
    for x in range(0,len(final_solution)):
        print("%s."%(x+1),end="\n")
        print(final_solution[x])

time_stop = timeit.default_timer()
print("It takes %.3f seconds to solve the puzzle in total." %(time_stop-time_begin))
   



    




    
