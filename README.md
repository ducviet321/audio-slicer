# Audio-slicer
Use slicer.py for slicing multiple files in a directory into chunks to use as data training for **so-vits-svc**. The output will be saved in the same directory that contains input file.
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

Slicer can be used for slicing the whole input file into bunch of chunks. For this code you must specify the output directory. Default target_length is 30 seconds which means chopping the file into 30-second chunks.

Example: <br>
```
python slicer.py --input_dir=/Users/joohyunpark/Desktop/input --file_name=test --output_dir=/Users/joohyunpark/Desktop/result --target_length=30
```

Details: <br>
```
--input_dir  INPUT_DIR             Directory that contains input file. Must be a wav file.
--file_name  FILE_NAME             Name of input file.
--output_dir  OUTPUT_DIR           Directory for results.
--length  TARGET_LENGTH     Desired duration of output.
```
