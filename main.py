"""
Main.
Create pre_dir_files, clone project. 
Run asyncio and rm dirs.
"""
import os 
import asyncio

from get_hash import main
from clone_dir import get_clone_dir


PRE_DIR_FILES = 'pre_dir_files'
HEAD = 'HEAD'
CLONE_REPO = 'https://gitea.radium.group/radium/project-configuration.git'

cmd_poerty_shell = 'poetry shell'
os.system(cmd_poerty_shell)

cmd_create_run_tests = 'python -m unittest tests.py'
os.system(cmd_create_run_tests)

cmd_create_pre_clone = 'ls -a > pre_dir_files'
os.system(cmd_create_pre_clone)

cmd_clone = f'git clone {CLONE_REPO}'
os.system(cmd_clone)

clone_dir, clone_dir_git = get_clone_dir(PRE_DIR_FILES)

asyncio.run(main(clone_dir_git, HEAD))

cmd_rm = f'rm -rf pre_dir_files {clone_dir}'
os.system(cmd_rm)
