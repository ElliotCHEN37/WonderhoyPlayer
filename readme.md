# WonderhoyPlayer
A python wonderhoy player

# Download
Just go to the release page and download it

# Config File
You can create a config file called `config.json`<br>
The file format should be like:
```json
{
  "trans": "translation.qm",
  "mode": "0"
}
```
`"trans"` means the path to the translation file, if this key is empty or the path is n/a, the program won't load the translation<br>
> support both absolute path and relative path
> 

`"mode"` means the playing mode<br>
set `"mode` to `"0"` will disable the infinite mode when program launched<br>
set `"mode"` to `"1"` will enable the infinite mode when program launched
>You still can disable or enable the infinite mode later after program launched
>

# Requiremnts
-Python 2.7 or higher<br>
-Needed packages were listed at requirements.txt, you can install them by running the following command<br>
`cd path\to\the\folder`<br>
`pip install -r requirements.txt`<br>
-[ffmpeg](https://ffmpeg.org/download.html)

# Build for Windows
1. Clone this repo
2. run `cd path\to\folder`
3. run `pip install -r requirements.txt` and `pip install pyinstaller`
4. run `pyinstaller build.spec`

# MacOS
Unfortunately, I don't have a Mac so I can't test this program on MacOS, but you can build it yourself

# 面相中國大陸使用者
可以考慮通過捐贈來支持我
![cn_user](cn.JPG)