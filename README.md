# audio-slicer
This repo is made for manipulating audio file. Use slicer1.py for setting a specific section and slicing into one file. Use slicer2.py for slicing the whole file into chunks. 
**The code only works for wav files.** 

## Dependency 
This code runs with [Pydub](https://github.com/jiaaro/pydub). You can install it easily by
```
pip install pydub
```

## Usage
### slicer1

Example: <br>
```
python slicer1.py --input_dir=/Users/joohyunpark/Desktop/test --file_name=test --target_length=10 --starting_point=0
```
