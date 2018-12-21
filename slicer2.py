import sys, getopt
from pydub import AudioSegment


input_dir = ''
file_name = ''
output_dir = ''
target_length = 30


def main(argv):
    global input_dir, target_length, file_name, output_dir

    try:
        opts, args = getopt.getopt(argv,"hi:s:",["input_dir=","file_name=","output_dir=", "target_length="])
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help':
            print 'test.py --input_dir=<input_dir> --file_name=file_name --output_dir=<output_dir> --target_length=30 '
            sys.exit()
        elif opt in ("-i", "--input_dir"):
            input_dir = arg
            print('file path : ' +input_dir)
        elif opt in ("-f", "--file_name"):
            file_name = arg
            print('file name : ' + file_name)
        elif opt in ("-o", "--output_dir"):
            output_dir = arg
            print('output dir : ' + output_dir)
        elif opt in ("-l", "--target_length"):
            target_length = arg
            print('target length : ' + target_length)


if __name__ == "__main__":
    main(sys.argv[1:])



song = AudioSegment.from_wav("%s/%s.wav" % (input_dir, file_name))

i = 0
while i < len(song)/(float(target_length)*1000) :
    print(i)
    seconds = float(target_length) * 1000 * i
    seconds2 = float(target_length) * 1000 * (i+1)
    cut = song[seconds:seconds2]
    cut.export("%s/%s-%dsec-%d.wav" % (output_dir, file_name, float(target_length), i), format="wav")
    i += 1


print("done")

