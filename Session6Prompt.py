import math

def print_sin(x):       #creates a sine function
    return math.sin(x)  #returns the value of sin(x)

def print_cos(x):       #creates a cosine function
    return math.cos(x)  #returns the value of cos(x)

def generate_sin_cos_table(start, end, num_entries):
    table = []

    for i in range(num_entries):
        x = start + (end - start) * i / (num_entries - 1)
        sin_value = print_sin(x)
        cos_value = print_cos(x)
        table.append((x, sin_value, cos_value))

    return table

def print_sin_cos_table(table):
    print("x\t| sin(x)\t| cos(x)")
    print("----------------------------------")
    for entry in table:
        print(f"{entry[0]:.3f}\t| {entry[1]:.3f}\t| {entry[2]:.3f}")

def main():
    start_x = 0
    end_x = 2 * math.pi
    num_entries = 1000

    sin_cos_table = generate_sin_cos_table(start_x, end_x, num_entries)
    print_sin_cos_table(sin_cos_table)

if __name__ == "__main__":
    main()
    
for i in range(10):
    x = i * (2 * math.pi)
    sin_value = print_sin(x)
    cos_value = print_cos(x)
    print(f"{x:.3f}\t| {sin_value:.3f}\t| {cos_value:.3f}")