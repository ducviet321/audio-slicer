import sys, getopt
from pydub import AudioSegment


input_dir = ''
file_name = ''
target_length = 10
starting_point = 0


def main(argv):
    global input_dir, target_length, starting_point, file_name

    try:
        opts, args = getopt.getopt(argv,"hi:s:",["input_dir=","file_name=","target_length=", "starting_point="])
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help':
            print 'test.py --input_dir=<input_dir> --file_name=file_name --target_length=10 --starting_point=0'
            sys.exit()
        elif opt in ("-i", "--input_dir"):
            input_dir = arg
            print('file path : ' +input_dir)
        elif opt in ("-f", "--file_name"):
            file_name = arg
            print('file name : ' + file_name)
        elif opt in ("-l", "--target_length"):
            target_length = arg
            print('target length : ' + target_length)
        elif opt in ("-s", "--starting_point"):
            starting_point = arg
            print('starting point : ' + starting_point)


if __name__ == "__main__":
    main(sys.argv[1:])


song = AudioSegment.from_wav("%s/%s.wav" % (input_dir, file_name))
cut = song[float(starting_point) * float(target_length) *1000: (float(starting_point)+1) * float(target_length) *1000]
cut.export("%s/%s-%dsec.wav" % (input_dir, file_name, float(target_length)), format="wav")
print("done")

