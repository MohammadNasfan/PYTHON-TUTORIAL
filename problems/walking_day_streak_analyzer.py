# p7.py
# Analyzes walking steps to compute streaks, walking days, and skipped days.
#i have to do is calculate longest walking streak
# current walking streak
# total walking days
# skipped days

def analyze_streaks(steps):
    total_walkingdays=0
    skipped_days=0
    current_streak=0
    longest_streak=0

    for i in steps:
        
        if i==0:
            skipped_days+=1
        if i!=0:
            total_walkingdays+=1
        if i>0:
            current_streak+=1
        else:
            current_streak=0
        if current_streak>longest_streak:
            longest_streak=current_streak
        
            
    return{"longest streak":longest_streak,
           "current streak":current_streak,
            "walking days":total_walkingdays,
            "skipped days":skipped_days,}




print(analyze_streaks([4000,5000,0,7000,8000,9000,0,3000]))
        
        
            
        
        
        
        
            
        
            
         
        
            