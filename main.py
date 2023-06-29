import subprocess
import sys
import zipfile
import io
from pathlib import Path
from os import listdir


import requests
import time



if len(sys.argv) == 4 and sys.argv[3] == "-o":
    pb_id = "".join(letter for letter in "".join(
        sys.argv[1:]).lower() if letter.isalnum())
    samples_url = f"https://open.kattis.com/problems/{sys.argv[1]}/file/statement/samples.zip"
    r = requests.get(samples_url)
    r.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        for file in z.filelist:
            file_path = Path(file.filename)
            print("-------------------------")
            if file_path.suffix == ".in":
                test_input = z.read(file).decode("utf-8")
                test_answer = z.read(f"{file_path.stem}.ans").decode("utf-8")
                t1 = time.time()
                p = subprocess.run([sys.executable, sys.argv[2]],
                                   input=test_input, encoding="utf-8", capture_output=True)
                print(time.time() - t1, "ms")
                if p.returncode != 0:
                    print("Error:", p.stderr)
                print("Sample input:\n", test_input, sep="")
                if p.stdout != test_answer:
                    print("Wrong answer!")
                    print("Expected:,", len(test_answer), "\n", test_answer, sep="")
                    print("Got:", len(p.stdout), "\n", p.stdout, sep="")
                else:
                    print("Good answer!")
                    print("Answer:\n", p.stdout, sep="")

    # ./venv/bin/python3 main.py citations Ex1.py -o
else:
    if len(sys.argv) < 3:
        fileToExec = "Ex2.py"
    else:
        fileToExec = sys.argv[2]

    # get all file names in Test folder
    test_files = listdir("Test")

    for file in test_files:
        file_path = Path(file)
        if file_path.suffix == ".in":
            test_input = open(f"Test/{file_path}", "r").read()
            test_answer = open(f"Test/{file_path.stem}.ans", "r").read()
            t1 = time.time()
            p = subprocess.run([sys.executable, fileToExec],
                               input=test_input, encoding="utf-8", capture_output=True)
            print(time.time() - t1, "ms")
            if p.returncode != 0:
                print("Error:", p.stderr)
            print("Sample input:\n", test_input, sep="")
            if p.stdout != test_answer:
                print("Wrong answer!")
                print("Expected:,", len(test_answer), "\n", test_answer, sep="")
                print("Got:", len(p.stdout), "\n", p.stdout, sep="")
            else:
                print("Good answer!")
                print("Answer:\n", p.stdout, sep="")