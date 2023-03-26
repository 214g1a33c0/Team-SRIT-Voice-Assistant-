import subprocess
input("Please press enter to install required libraries")
print("Packages are dowloading..\n\nWait for few minutes..\n\n")
try:
	subprocess.run(["pip", "install", "-r", "requirements.txt"])
except KeyboardInterrupt:
    print("Oops! you stoped forcely")
    exit(0)
