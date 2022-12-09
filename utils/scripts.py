import os, time, argparse
# from subprocess import check_output
from date import scripts, path

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--command', type=str, help=scripts['messages']['script_help'], nargs='*')
args = parser.parse_args()

def space(num):
    b = 0
    while b < num:
        print('\n')
        b+=1

def animation(large, start, message, sequence):
    empty = "-" * large
    character = "#"
    b = 0
    while start < large and b <large:
        aux = list(empty)
        aux[b] = character
        empty = ''.join(aux)
        print(f'[{empty}] {(b+1)*2}%', end='\r')
        if b == large-1 or start == 49:
            space(1)
            print(message)
        time.sleep(sequence)
        b+=1
        start+=1

def create_env():
    if os.path.exists(path+'.env'):
        animation(50, 0, scripts['messages']['create_env']['env_failed'], 0.03)
    else:
        env = open('.env', 'w')
        env.write(scripts['content']['create_env'])
        animation(50, 0, scripts['messages']['create_env']['env_success'], 0.03)

action = 0
while action < len(args.command):
    command = args.command[action]
    match command:
        case 'env':
            try:
                create_env(12351245)
            except:
                animation(50, 32, scripts['messages']['create_env']['env_failed_unexpected'], 0.07)
        case 'animation':
            space(1)
            animation(50, 0, "animation", 0.6)
        case _:
            print('\n')
            print(r"ERROR: could not find command: %r" %command)
            action+=len(args.command)
    action+=1