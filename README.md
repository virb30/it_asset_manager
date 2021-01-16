# Description

Script to collect PC info, format to JSON and send to remote server over http.
Collects infos:
- System version
- PC name
- CPU Architecture
- CPU count
- CPU brand
- Total Memory
- Disk partitions
- Boottime

# How to Develop

Clone this repository
Create virtual env
Install dependencies
Run tests
Start coding

```console
git clone git@github.com:virb30/it_asset_manager.git it_asset_manager
python -m venv .venv
pip install -r requirements.txt
python -m unittest
```

# How to Use
Run `python asset_manager.py`