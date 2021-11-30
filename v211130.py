#! /usr/bin/env python3
import sys

def main():
  if len(sys.argv) != 3:
    print('Convert shift-jis file to utf-8 file.')
    print(f'Usage: python3 {sys.argv[0]} <in-file(shift-jis)> <out-file(utf-8)>\n')
    exit()
  else:
    infile = sys.argv[1]
    outfile = sys.argv[2]
 
  try:
    with open(infile, encoding='shift_jis') as fi, open(outfile, 'w') as fo:
    # with open(infile) as fi, open(outfile, 'w', encoding='shift_jis') as fo:
      fo.write(fi.read())
  except  FileNotFoundError as e:
    print(f'File({infile}) not found.\n{e}\n')
  except Exception as e:
    print(e)

if __name__ == '__main__':
  main()
