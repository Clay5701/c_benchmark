import subprocess
import time

def main():
    # IMPORTANT: EDIT THESE VARIABLES TO REFLECT YOUR WORKSPACE

    # Name of C program to be tested
    c_program = "benchmark_test.c"

    # Desired name of the generated executable
    executable = "benchmark_test"

    #Command line arguments to be passed when run
    arguments = ["input.txt", "output.txt"]

    # File to store user inputs
    # !!! Every line in the file represents one unique user input !!!
    input_file = "input.txt"

    user_input = get_input(input_file)

    help()

    while True:
        selection = input("Enter operation code: ")

        match selection[0].lower():
            case 'h':
                help()

            case 'r':
                compile(c_program, executable)
                run(executable, arguments, user_input)
            
            case 'b':
                benchmark(c_program, executable, arguments, user_input)
            
            case 'q':
                print("Exiting...")
                break

            case _:
                print("Invalid operation code.")
        print()

# -----FUNCTION DEFINITIONS-----

def help():
    print("List of operation codes:")
    print("\t'h' for help;")
    print("\t'r' for compile and run;")
    print("\t'b' for performance benchmark;")
    print("\t'q' to quit.")

# Gets simulated user input from given input file
def get_input(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    
        result = ''.join(line.strip() + "\n" for line in lines)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return

    return result

# Compiles given C program
def compile(filename, executable_name):
    try:
        compile_cmd = f"gcc {filename} -o {executable_name}"
        subprocess.run(compile_cmd, check=True, text=True, capture_output=True)

    except subprocess.CalledProcessError as e:
        print(f"Compilation failed:\n{e.stderr}")

# Runs generated executable
def run(executable_name, args=[], input=None, print_flag=True):
    try:
        run_cmd = [f"./{executable_name}"] + args

        start_time = time.perf_counter()
        run = subprocess.run(run_cmd, input=input, check=True, text=True, capture_output=True)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        if print_flag:
            print(run.stdout)

        return elapsed_time

    except subprocess.CalledProcessError as e:
        print(f"Error ocurred:\n{e.stderr}")
        return float('inf')

# Runs a performance benchmark
def benchmark(filename, executable_name, arguments, user_input):
    compile(filename, executable_name)

    while True:
        try:
            trials = int(input("Enter number of trials: "))
            if trials == 0:
                print("Number of trials cannot be zero.")
            else:
                break

        except ValueError:
            print("Please enter an integer.")
    
    times = []
    
    for i in range(trials):
        elapsed_time = run(executable_name, arguments, user_input, print_flag=False)
        times.append(elapsed_time)
    
    avg_time = sum(times) / len(times)
    print(f"Average time: {avg_time}")
    print(f"Max time: {max(times)}")
    print(f"Min time: {min(times)}")
    
if __name__ == "__main__":
    main()