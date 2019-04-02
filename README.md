# flask_system_reboot_service
This repository contains a Simple Flask web app that executes some bash shell scripts and reboots the system.

## Installation & Setup
1. Install virtualenv if not already installed
```
pip install virtualenv
```
2. Create a python3 virtualenv
```
virtualenv -p python3 venv
```
3. Activate the virtual environment
```
source venv/bin/activate
```
4. Clone the repository
```
git clone https://github.com/SummitStha/flask_system_reboot_service.git
```
5. Navigate into the project
```
cd flask_system_reboot_service/
```
6. Create a config.txt file using the config.example.txt file and put your credentials as required in the newly created config.txt file
```
mv config.example.txt config.txt
```
7. Inside your virtual environment, install the required python modules and packages using the requirements.txt file
```
pip install -r requirements.txt
```
8. Run the app
```
python boot.py
```

9. Open a browser of your choice and navigate to http://localhost:5000
