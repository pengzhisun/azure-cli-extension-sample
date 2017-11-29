# ==============================================================================
# File Name:    __init__.py
# Summary:
#    Defines the Azure CLI extension commands.
# See: 
#    https://packaging.python.org/tutorials/distributing-packages/#setup-py
#    https://github.com/pypa/sampleproject/blob/master/setup.py
#    https://packaging.python.org/en/latest/distributing.html
# ==============================================================================

from azure.cli.core.help_files import helps

helps['hello world'] = """
    type: command
    short-summary: Say hello world.
"""

def helloworld():
    print "Hello World."

def load_params(_):
    pass

def load_commands():
    from azure.cli.core.commands import cli_command
    cli_command(__name__, 'hello world', 'azext_helloworldsample#helloworld')
