users_input = int(input("Enter a score: "))
print("Enter -1 or -2 to stop")

pass_mark = 0
fail_mark = 0




while users_input != 1 and users_input != 2:
    if users_input >= 50:
        pass_mark += 1
    if users_input < 50:
        fail_mark += 1
    users_input = int(input("Enter a score: "))
    print("Enter -1 or -2 to stop")

print("The amount of pass is", pass_mark)
print("The amount of fail is", fail_mark )
    
    
    

