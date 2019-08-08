# GetScraped v3 🚒
Don't Worry About It! But if you'd like to know, it scrapes emails from CSV's containing website addresses. The program pulls the html, uses a regexp match, and removes /  cleans up duplicates.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies (see below).

```bash
git clone https://github.com/kendalled/GetScraped.git
```

## Usage
Put many csv files containing URL's in the src/Data Folder. 
Then:
```bash
pip3 install pandas
pip3 install lxml
pip3 install unicodecsv
```
Then, Run the Following:
```bash
python3 getscrapedall.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update issues as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)