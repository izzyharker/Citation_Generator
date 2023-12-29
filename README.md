# bookcite
Python CLI program to generate book citations from an ISBN.

## Usage
```
python cite.py -f <isbn> [-s <style: mla, apa, chicago>]
```
The isbn number is required, the style is optional. Someday, this may be a package that can be installed with `pip`, but that day is not today.

## Dependencies
Built-in libraries `os`, `json` and `sys`, as well as the `requests` library. The latter can be installed with `pip`, by running the following in a terminal window (Mac or Linux). I haven't tested this on Windows yet.
```
pip install requests
```

## Current Support
MLA, APA, and Chicago citation styles. The default style is MLA.

## Notes
The citations appear correctly in the terminal. However, the proper italicization is not maintained when copy-pasting into Google Docs or Word. So, it is not 100% accurate in that when copy-pasting, some formatting must be fixed afterwards. However, the words themselves are correct.