import argparse
import binascii

# Add arguments to parser and parse command line
parser = argparse.ArgumentParser(description='XOR two files')
parser.add_argument('mode')
parser.add_argument('key')
parser.add_argument('source_file')
parser.add_argument('dest_file')
args = parser.parse_args()

# Process key arg
key = int('0x' + args.key,16)

if args.mode == "encrypt":
    with open(args.source_file,mode='rb') as source_file:
        with open(args.dest_file,mode='wb') as dest_file:
            data = source_file.read()
            for byte in data:
                processed = key ^ byte
                dest_file.write(binascii.unhexlify(hex(processed).split('x')[-1]))
elif args.mode == "decrypt":
    with open(args.source_file,mode='rb') as source_file:
        with open(args.dest_file,mode='w') as dest_file:
            data = source_file.read()
            for byte in data:
                processed = key^byte
                dest_file.write(chr(processed))