# p15.py
# Analyzes temperature trends for highs, lows, increasing/decreasing days, and streaks.
# hottest temperature
# coldest temperature
# number of increasing days
# number of decreasing days
# longest increasing streak
def analyze_temperature(temps):
    hottest_temp=0
    lowest_temp=temps[0]
    increasing_days=0
    decreasing_days=0
    current_streak=0
    longest_increasing_streak=0
    for i in temps:
        if i > hottest_temp:
            hottest_temp=i
        if i<lowest_temp:
            lowest_temp=i
    for j in range(1,len(temps)):
        if temps[j]>temps[j-1]:
            increasing_days+=1
        
        if temps[j]<temps[j-1]:
            decreasing_days+=1
        if temps[j]>temps[j-1]:
            current_streak+=1
        else:
            current_streak=0
        if current_streak>longest_increasing_streak:
         longest_increasing_streak=current_streak
            


    return hottest_temp,lowest_temp,increasing_days,decreasing_days,longest_increasing_streak





print(analyze_temperature([30,32,35,33,31,34,36]))