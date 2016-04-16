from cfgutils import read_commands, read_config
import output

import subprocess
import argparse

def execute():
    """Takes a code and a target address to find the correct command object
    from the config.json file, appends the target and executes it."""

    parser = argparse.ArgumentParser(description=read_config("description"))
    parser.add_argument('-c', '--code', help='Tool-specific command code')
    parser.add_argument('-t', '--target', help="Target address")
    args = parser.parse_args()

    if args.code and args.target:
        command_obj = read_commands(args.code)
        exec_cmd =  command_obj["command"] + " " + args.target

        bytes_output = subprocess.check_output([exec_cmd], shell=True)
        str_output = bytes_output.decode('utf-8')

        command_obj["target"] = args.target
        command_obj["result"] = output.format(str_output, args.code)
        return command_obj

print(execute())
