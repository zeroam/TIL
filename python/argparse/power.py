import argparse
parser = argparse.ArgumentParser()
parser.add_argument('x', type=int, help='the base')
parser.add_argument('y', type=int, help='the exponent')
# action='count'를 통해 -v 옵션의 갯수를 리턴 받을 수 있다.
# ex) -vv -> 2, -v -> 1, 기본값은 0으로 설정(default=0)
parser.add_argument('-v', '--verbosity', action='count', default=0)
args = parser.parse_args()
answer = args.x ** args.y
if args.verbosity >= 2:
    print(f'Running "{__file__}"')
if args.verbosity >= 1:
    print(f'{args.x}^{args.y} == ', end='')
print(answer)