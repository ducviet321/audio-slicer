import sys
import getopt
import os
from pydub import AudioSegment


input_dir = ''
file_name = ''
output_dir = ''
length = 30


def main(argv):
    global input_dir, length, file_name, output_dir

    try:
        opts, args = getopt.getopt(argv, "hi:s:", ["input_dir=", "output_dir=", "length="])
    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))
        sys.exit(2)

    for opt, arg in opts:
        if opt == '--help':
            print('slicer.py --input_dir=<input_dir> --output_dir=<output_dir> --length=10 ')
            sys.exit()
        elif opt in ("-i", "--input_dir"):
            input_dir = arg
            print('file path : ' + input_dir)
        elif opt in ("-f", "--file_name"):
            file_name = arg
            print('file name : ' + file_name)
        elif opt in ("-o", "--output_dir"):
            output_dir = arg
            print('output dir : ' + output_dir)
        elif opt in ("-l", "--length"):
            length = arg
            print('length : ' + length)


if __name__ == "__main__":
    main(sys.argv[1:])


# List all files in the input directory
files = os.listdir(input_dir)

# Filter files ending with ".wav"
wav_files = [file for file in files if file.endswith(".wav")]

# Process each WAV file
for i, file_name in enumerate(wav_files):
    print(f"Processing {i}. {file_name}")
    file_path = os.path.join(input_dir, file_name)
    song = AudioSegment.from_wav(file_path)

    i = 0
    while i < len(song) / (float(length) * 1000):
        print(i)
        seconds = float(length) * 1000 * i
        seconds2 = float(length) * 1000 * (i+1)
        cut = song[seconds:seconds2]
        export_path = os.path.join(output_dir, f"{file_name}-{float(length)}sec-{i}.wav")
        cut.export(export_path, format="wav")
        i += 1

print("Completed")
