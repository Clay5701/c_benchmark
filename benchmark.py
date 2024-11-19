import subprocess
import time

def main():
    c_program = "project6_tokenizer.c"
    executable = "project6_tokenizer"
    arguments = ["input.txt", "output.txt"]

    compile(c_program, executable)

    trials = 50
    times = []

    for i in range(trials):
        elapsed_time = run(executable, arguments)
        times.append(elapsed_time)
    
    avg_time = sum(times) / len(times)
    print(f"Average time: {avg_time}")
    print(f"Max time: {max(times)}")
    print(f"Min time: {min(times)}")

def compile(filename, executable_name):
    try:
        compile_cmd = f"gcc {filename} -o {executable_name}"
        compile = subprocess.run(compile_cmd, check=True, text=True, capture_output=True)

    except subprocess.CalledProcessError as e:
        print(f"Error ocurred:\n{e.stderr}")
    
def run(executable_name, args=[]):
    try:
        run_cmd = [f"./{executable_name}"] + args

        start_time = time.perf_counter()
        run = subprocess.run(run_cmd, check=True, text=True, capture_output=True)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        return elapsed_time

    except subprocess.CalledProcessError as e:
        print(f"Error ocurred:\n{e.stderr}")
        return None
    
if __name__ == "__main__":
    main()