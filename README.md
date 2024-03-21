Python Exercises

1. Instructions to setup Python environment:
```bash
# Create virtual environment to install pip dependencies specific to project
python3 -m venv .venv
```


For fresh installations:
```bash
# Required packages
pip3 install scrapy==2.4 shub scrapy-crawlera  google-cloud-storage scrapy-sessions 
# Pinned dependencies due to newer versions being incompatible with scrapy 2.4 
pip3 install Twisted==22.10.0
pip3 install pyopenssl==22.0.0
pip3 install parsel==1.7.0
```

With `requirements.txt`:
```
pip3 install -r requirements.txt
```


2. crawler is in the tackleworld directory
3. crawler is in the surfboardempire directory
4. Python code is in regex.py