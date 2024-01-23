import math

def generate_sin_table(start, end, num_entries):
    table = []

    for i in range(num_entries):
        x = start + (end - start) * i / (num_entries - 1)
        sin_value = math.sin(x)
        table.append((x, sin_value))

    return table

def print_sin_table(table):
    print("x\t| sin(x)")
    print("------------------")
    for entry in table:
        print(f"{entry[0]:.3f}\t| {entry[1]:.3f}")

def main():
    start_x = 0
    end_x = 2 * math.pi
    num_entries = 1000

    sin_table = generate_sin_table(start_x, end_x, num_entries)
    print_sin_table(sin_table)

if __name__ == "__main__":
    main()
