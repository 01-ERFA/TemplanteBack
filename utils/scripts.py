import os, time, argparse, getpass, shutil
from subprocess import check_output

from date import scripts
from setup import engine, get_db_name, path, exist_env, exist_migrations

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--command', type=str, help=scripts['messages']['script_help'], nargs='*')
args = parser.parse_args()

def space(num):
    b = 0
    while b < num:
        print('\n')
        b+=1

def concat_str(main, strings):
    b = 0
    result = main
    try:
        while b < len(strings):
            result = result + strings[b]
            b+=1
        return result
    except:
        print('Error: first expected a string and then a list in the parameters')

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
    if exist_env:
        animation(50, 0, 39, scripts['messages']['create_env']['env_failed'], 0.03)
    else:
        try:
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
        except:
            animation(50, 0, 32, scripts['messages']['create_env']['env_failed_unexpected'], 0.07)
        
def delete_env():
    if exist_env:
        try:
            os.remove(path+'.env')
            animation(50, 0, 0, scripts['messages']['delete_env']['env_success'], 0.05)
        except:
            animation(50, 0, 32, scripts['messages']['create_env']['env_failed_unexpected'], 0.07)
    else:
        animation(50, 0, 41, scripts['messages']['delete_env']['env_failed'], 0.03)

def flask_init():
    try:
        check_output(scripts['commands']['commands_developing']['flask_init'])
        animation(50, 0, 0, scripts['messages']['flask']['init']['flask_success'], 0.03)
    except:
        animation(50, 0, 44, '', 0.07)

def flask_migrate():
    if exist_env:
        check_output(scripts['commands']['commands_developing']['flask_migrate'])
        animation(50, 0, 0, scripts['messages']['flask']['migrate']['flask_success'], 0.03)
    else:
        animation(50, 0, 47, scripts['messages']['create_env']['create'], 0.04)
def flask_upgrade():
    if exist_env:
        check_output(scripts['commands']['commands_developing']['flask_upgrade'])
        animation(50, 0, 0, scripts['messages']['flask']['upgrade']['flask_success'], 0.03)
    else:
        animation(50, 0, 46, scripts['messages']['create_env']['create'], 0.04)

def db_drop(db_name):
    command = scripts['commands']['commands_db']['drop_start']+db_name+scripts['aux_symbols']['semicolon']
    if engine != None:
        engine.execute(command)
    else:
        msg = scripts['messages']['db']['others']['engine_failed']
        animation(50, 0, 35, msg, 0.04)

def db_create(db_name):
    command = scripts['commands']['commands_db']['create_start']+db_name+scripts['aux_symbols']['semicolon']
    if engine != None:
        engine.execute(command)
    else:
        msg = scripts['messages']['db']['others']['engine_failed']
        animation(50, 0, 35, msg, 0.04)
    
def db_reset():
    if exist_env:
        if exist_migrations:
            if engine != None:
                msg = ''
                result_actions = []
                try:
                    db_drop(get_db_name)
                    result_actions.append(scripts['messages']['db']['db_drop']['success'])
                    result_actions.append(scripts['aux_symbols']['line_separator'])
                except:
                    result_actions.append(scripts['messages']['db']['db_drop']['failed'])
                    result_actions.append(scripts['aux_symbols']['line_separator'])
                try:
                    db_create(get_db_name)
                    result_actions.append(scripts['messages']['db']['db_create']['success'])
                    result_actions.append(scripts['aux_symbols']['line_separator'])
                except:
                    result_actions.append(scripts['messages']['db']['db_create']['failed'])
                    result_actions.append(scripts['aux_symbols']['line_separator'])
                try:
                    shutil.rmtree(path+'migrations')
                    result_actions.append(scripts['messages']['db']['others']['remove_migrations_success'])
                    result_actions.append(scripts['aux_symbols']['line_separator'])
                except:
                    result_actions.append(scripts['messages']['db']['others']['remove_migrations_failed'])
                    result_actions.append(scripts['aux_symbols']['line_separator'])
                try:
                    command = scripts['commands']['commands_db']['others']['reset_migrations']['init']
                    check_output(command)
                    command = scripts['commands']['commands_db']['others']['reset_migrations']['migrate']
                    check_output(command)
                    command = scripts['commands']['commands_db']['others']['reset_migrations']['upgrade']
                    check_output(command)                    
                    result_actions.append(scripts['messages']['db']['others']['reset_migrations_success'])
                    result_actions.append(scripts['aux_symbols']['line_separator'])
                except:
                    result_actions.append(scripts['messages']['db']['others']['reset_migrations_failed'])
                    result_actions.append(scripts['aux_symbols']['line_separator'])
                msg = concat_str(msg, result_actions)
                animation(50, 0, 0, msg, 0.03)
                
            else:
                msg = scripts['messages']['db']['others']['engine_failed']
                animation(50, 0, 35, msg, 0.04)
        else:
            msg = scripts['messages']['db']['others']['not_migrations_file']+(scripts['aux_symbols']['line_separator']*2)+scripts['messages']['db']['others']['drop_suggest']+scripts['aux_symbols']['line_separator']+scripts['messages']['db']['others']['create_suggest']+scripts['aux_symbols']['line_separator']+scripts['messages']['db']['others']['start_migrations']
            animation(50, 0, 40, msg, 0.03)
    else:
        msg = scripts['messages']['create_env']['create']
        animation(50, 0, 43, msg, 0.03)

action = 0
while action < len(args.command):
    command = args.command[action]
    match command:
        case 'db_reset':

            db_reset()

        case 'flask_upgrade':
            try:
                flask_upgrade()
            except:
                animation(50, 0, 38, '', 0.06)
        case 'flask_migrate':
            try:
                flask_migrate()
            except:
                animation(50, 0, 37, '', 0.07)
        case 'flask_init':
            try:
                flask_init()
            except:
                animation(50, 0, 37, scripts['messages']['flask']['init']['failed_unexpected'], 0.07)
        case 'animation':
            space(1)
            animation(50, 5, 0, "animation", 0.06)
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