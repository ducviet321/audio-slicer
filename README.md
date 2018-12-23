# audio-slicer
This repo is made for manipulating audio file easily with command line. Use slicer1.py for setting a specific section and slicing into one file. Use slicer2.py for slicing the whole file into chunks. The output will be saved in the same directory that contains input file.
**The code only works for wav files.** 

## Dependency 
This code runs with [Pydub](https://github.com/jiaaro/pydub). You can install it by
```
pip install pydub
```

## Usage
Open terminal download this repot and go to directory where scripts are located.
```
git clone https://github.com/byjoohyunpark/audio-slicer.git
cd audio-slicer
```


### slicer1.py
Slicer1 can be used for extracting specific section of the input file. You can set the starting point(seconds) and target duration. For example, --starting_point=2 --target_length=10 means cut audio file from 2 to 12 seconds and create a 10-second file. Default settings for these two parameters are same as example below. 

Example: <br>
```
python slicer1.py --input_dir=/Users/joohyunpark/Desktop/input --file_name=test --starting_point=0 --target_length=10
```

Details: <br>
```
--input_dir  INPUT_DIR             Directory that contains input file. Must be a wav file.
--file_name  FILE_NAME             Name of input file.
--starting_point  STARTING_POINT   Starting point to slice input.
--target_length  TARGET_LENGTH     Desired duration of output.
```

### slicer2.py
Slicer2 can be used for slicing the whole input file into bunch of chunks. For this code you must specify the output directory. Default target_length is 30 seconds which means chopping the file into 30-second chunks.

Example: <br>
```
python slicer2.py --input_dir=/Users/joohyunpark/Desktop/input --file_name=test --output_dir=/Users/joohyunpark/Desktop/result --target_length=30
```

Details: <br>
```
--input_dir  INPUT_DIR             Directory that contains input file. Must be a wav file.
--file_name  FILE_NAME             Name of input file.
--output_dir  OUTPUT_DIR           Directory for results.
--target_length  TARGET_LENGTH     Desired duration of output.
```
