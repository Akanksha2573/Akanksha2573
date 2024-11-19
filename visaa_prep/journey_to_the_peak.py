def highest_altitude(N, heights):
    current_altitude = 0
    max_altitude = 0    
    for height in heights:
        current_altitude += height
        max_altitude = max(max_altitude, current_altitude)   
    return max_altitude
N = int(input())  
heights = list(map(int, input().split()))  
print(highest_altitude(N, heights))
