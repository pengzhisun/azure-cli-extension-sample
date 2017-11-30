# ==============================================================================
# File Name:    __init__.py
# Summary:
#    Defines the Azure CLI extension commands.
# See: 
#    https://github.com/Azure/azure-cli/blob/master/doc/extensions/authoring.md
# ==============================================================================

from azure.cli.core.help_files import helps

# Set command help message
# See:
#    https://github.com/Azure/azure-cli/blob/master/doc/authoring_help.md
helps['hello world'] = """
    type: command
    short-summary: Say hello world.
"""

# The command operator method
def helloworld():
    print('Hello World.') #pylint: disable-msg=C0325

# Set the command arguments
# See:
#    https://github.com/Azure/azure-cli/blob/master/doc/authoring_command_modules/authoring_commands.md
def load_params(_):
    pass

# Registering Commands
# See:
#    https://github.com/Azure/azure-cli/blob/master/doc/authoring_command_modules/authoring_commands.md
def load_commands():
    from azure.cli.core.commands import cli_command
    cli_command(__name__, 'hello world', 'azext_helloworldsample#helloworld')
