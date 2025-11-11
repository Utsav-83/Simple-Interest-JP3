import sys
if len(sys.argv) == 3:
    script_name = sys.argv[0]
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
    print("User provided input values:")
else:
    principal = 1000.0
    rate = 5.0
    time = 1.0
    print("No input given - using default values:")
    
si = (principal * rate * time) / 100
print("Principal Amount:", principal)
print("Rate of Interest:", rate)
print("Time (in years):", time)
print("Simple Interest:", si)