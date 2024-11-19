# Glass3k

Glass3k is a lightweight Windows utility that allows you to adjust the transparency (opacity) of any open window.

## Installation

An already compiled version of Glass3k can be found in the github releases page.
Or you can build from source. See the build section below.

## Build from source

To build Glass3k from source you need Python installed.

1. Install dependencies

```bash
  pip install -r requirements.txt
```

2. Build the executable

```bash
  pyinstaller --onefile --icon=glass3k.ico glass3k.py
```
