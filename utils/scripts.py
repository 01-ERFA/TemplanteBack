import os, time, argparse, getpass, shutil
from subprocess import check_output
from date import scripts, path

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--command', type=str, help=scripts['messages']['script_help'], nargs='*')
args = parser.parse_args()

def space(num):
    b = 0
    while b < num:
        print('\n')
        b+=1

def animation(large, start, short_end , message, sequence):
    if start != 0:
        empty = "#" * start + "-" * (large-start)
    else:
        empty = "-" * large
    character = "#"
    b = start
    while short_end < large and b <large:
        aux = list(empty)
        aux[b] = character
        empty = ''.join(aux)
        print(f'[{empty}] {(b+1)*2}%', end='\r')
        if b == large-1 or short_end == large-1:
            space(1)
            print(message)
        time.sleep(sequence)
        b+=1
        short_end+=1

def create_env():
    if os.path.exists(path+'.env'):
        animation(50, 0, 39, scripts['messages']['create_env']['env_failed'], 0.03)
    else:
        space(1)
        print(scripts['messages']['create_env']['start_message'])
        user = getpass.getpass(scripts['messages']['create_env']['user'])
        pswd = getpass.getpass(scripts['messages']['create_env']['pswd'])
        db_name = getpass.getpass(scripts['messages']['create_env']['db_name'])
        secret_key = getpass.getpass(scripts['messages']['create_env']['secret_key'])
        space(1)
        env = open('.env', 'w')
        env_content=scripts['content']['create_env']['comment']+scripts['content']['create_env']['developing']+scripts['content']['create_env']['database_url_start']+user+":"+pswd+scripts['content']['create_env']['database_url_end']+db_name+scripts['content']['create_env']['line_separator']+scripts['content']['create_env']['database_name']+db_name+scripts['content']['create_env']['line_separator']+scripts['content']['create_env']['secret_key']+secret_key+scripts['content']['create_env']['line_separator']
        env.write(env_content)
        animation(50, 0, 0, scripts['messages']['create_env']['env_success'], 0.05)
        
def delete_env():
    if os.path.exists(path+'.env'):
        try:
            os.remove(path+'.env')
            animation(50, 0, 0, scripts['messages']['delete_env']['env_success'], 0.05)
        except:
            animation(50, 0, 32, scripts['messages']['create_env']['env_failed_unexpected'], 0.07)
    else:
        animation(50, 0, 41, scripts['messages']['delete_env']['env_failed'], 0.03)

def flask_init():
    try:
        check_output(scripts['commands_developing']['flask_init'])
        animation(50, 0, 0, scripts['messages']['flask']['init']['flask_success'], 0.03)
    except:
        animation(50, 0, 34, scripts['messages']['flask']['init']['failed_exist'], 0.07)



action = 0
while action < len(args.command):
    command = args.command[action]
    match command:
        case 'flask_init':
            try:
                flask_init()
            except:
                animation(50, 0, 37, scripts['messages']['flask']['init']['failed_unexpected'], 0.07)
        case 'animation':
            space(1)
            animation(50, 5, 0, "animation", 0.6)
        case 'create_env':
            try:
                create_env()
            except:
                animation(50, 0, 32, scripts['messages']['create_env']['env_failed_unexpected'], 0.07)
        case 'delete_env':
            try:
                delete_env()
            except:
                animation(50, 0, 43, scripts['messages']['delete_env']['env_failed_unexpected'], 0.07)
        case _:
            print('\n')
            print(r"ERROR: could not find command: %r" %command)
            action+=len(args.command)
    action+=1