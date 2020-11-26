# myabb_cli

## Setup

if virtualenv is not installed, install it using:
```bash
pip3 install virtualenv
```

Create virtual environment

```bash
virtualenv -p python3 myenv
```
Activate the created virtual environment

```bash
source myenv/bin/activate
```

Install requirements from requirements.txt

```bash
pip3 install -r requirements.txt
```

create a .env file and copy contents of .env.example to it. Then replace your_username and your_password with your username and password respectively.

## Usage

```bash
python3 myabb_automation.py
```
