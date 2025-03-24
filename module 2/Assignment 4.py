# Convert Miles to Kilometers 
def miles_to_km(miles):
    return miles * 1.60934
try:
    miles = float(input('Enter miles driven: '))
    km = miles_to_km(miles)
    print(f'Total miles: {miles} = {km:.2f} km')
except ValueError:
    print("Please enter a valid number")