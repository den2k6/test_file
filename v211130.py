#! /usr/bin/env python3
import sys

def main():
  print(sys.version)
  if len(sys.argv) != 2:
    print(f'Usage: python3 {sys.argv[0]} <filename>\n')
    exit()
  else:
    target_file = sys.argv[1]

  try:
    with open(target_file) as fi, open('python_out.txt', 'w') as fo:
      fo.write(fi.read())
  except  FileNotFoundError as e:
    print(f'File({target_file}) not found.\n{e}\n')
  except Exception as e:
    print(e)

if __name__ == '__main__':
  main()
