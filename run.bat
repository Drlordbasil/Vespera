Sure! Here is an example of the run.bat file contents:

```
@echo off
echo Installing required packages...
pip install -r requirements.txt

echo Running the program...
python main.py

echo Program execution completed.
pause
```

Save the above contents in a file named `run.bat`. Now, when the user executes the `run.bat` file, it will install the required packages using `pip` and then run the `main.py` program.