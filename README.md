# Checklist :white_check_mark:

[![Build Status](https://travis-ci.org/joaogarciadelima/checklist.svg?branch=master)](https://travis-ci.org/joaogarciadelima/checklist)
[![Updates](https://pyup.io/repos/github/joaogarciadelima/checklist/shield.svg)](https://pyup.io/repos/github/joaogarciadelima/checklist/)
[![Python 3](https://pyup.io/repos/github/joaogarciadelima/checklist/python-3-shield.svg)](https://pyup.io/repos/github/joaogarciadelima/checklist/)

Para instalar Unix: 

```console
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```
Para instalar Windows:

```console
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
```

Para conferir qualidade de código:

```console
flake8 .
```