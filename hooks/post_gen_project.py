import shutil
import subprocess

shutil.rmtree('licenses')

git_commands = [
    'git init -q',
    'git add .',
    'git reset -q README.md',
    'git add -N README.md',
]

for git_command in git_commands:
    subprocess.run(git_command, check=True, shell=True)

{%- if cookiecutter.install_dependencies_now == "y" %}
def print_formatted(message: str) -> None:
    width = max((len(line) for line in message))
    print('', width * '-', *message, width * '-', sep='\n')

install_commands = [
    'yarn set version stable',
    'yarn plugin import https://mskelton.dev/yarn-outdated/v3',
    'yarn install',
    'yarn clean-install',
    'git add .yarn .yarnrc.yml package.json yarn.lock',
]

try:
    for install_command in install_commands:
        subprocess.run(install_command, check=True, shell=True)
except subprocess.CalledProcessError as e:
    print_formatted([
        f'Shell command failed with exit code {e.returncode}.',
        'Go to the {{ cookiecutter.project_slug }}'
            ' directory and re-run:',
        *[
            f'    {command}'
            for command in ['nvm use'] + install_commands
        ],
    ])
{%- endif %}
