# password-generator

A simple password generator for secure and customizable passwords.

---

![Python](https://img.shields.io/badge/python-3.12-blue)

--- 
## Description

Password-generator is a light-weight Python tool to generate strong secure passwords.
You can customize length , include symbols, numbers, and letters to create secure password for your account or your projects.

---

## Installation

- via git:
Clone the repository and install it in editable mode:
```bash
git clone https://github.com/amiri-x/password-generator.git
cd password-generator
pip install -e .
```

- via pip(directly):
```bash
pip install git+https://github.com/amiri-x/password-generator.git
```


## Usage 
After the installation succeed, now your can use/run it:

1. As python module:
```python 
from pwgenx.generator import generate

password = generate(8)
print("Generated Password:", password) 

# e.g output: Generated Password: aBps@#42 
 ```


2. As CLI tool
```bash
pwgenx # password with 8 characters by default
```
```bash
pwgenx -h # to see guide and info 
```

