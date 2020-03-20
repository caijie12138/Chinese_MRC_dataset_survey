import json
import argparse

def take_a_look(data_file):
    with open(data_file,'r') as reader:
        for line in reader.readlines():
            print(line)



if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_file',required=True,help='the file path that you want take a look')
    args = parser.parse_args()
    take_a_look(args.data_file)



