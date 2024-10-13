import subprocess

def run_job(cmd):
    ret = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return ret.stdout.decode('UTF-8')

if __name__ == '__main__':
    # Run the Python script
    msg = run_job("python3 script.py").rstrip()  # Change "script.py" to your Python file name
    if msg == "Hello World!":
        print("Correct!")
    else:
        print("Error. The correct answer is `Hello World!`, but your output is:")
        print("```")
        print(msg)
        print("```")
