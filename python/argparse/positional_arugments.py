import argparse
parser = argparse.ArgumentParser()
# echo 라는 positional 인자값 추가
parser.add_argument('echo', help='echo the string you use here')
args = parser.parse_args()
print(args.echo)