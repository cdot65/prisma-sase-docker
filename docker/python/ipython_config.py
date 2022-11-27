# Configuration file for ipython.
from IPython.terminal.prompts import Token


c = get_config()  # noqa

banner_start = "-" * 64 + "\n\n"
banner_welcome = "Welcome to the Palo Alto Networks SDK container\n\n\n"
banner_env = "Variables are being loaded from the /home/python/.env file\n\n"
banner_url = "\tPANURL = your panorama instance\n"
banner_user = "\tPANUSER = your panorama username\n"
banner_pass = "\tPANPASS = your panorama password\n"
banner_end = "\n" + "-" * 64 + "\n"

PANORANGE = "#F04E23"
PANCYAN = "#00C0E8"
c.TerminalInteractiveShell.highlighting_style_overrides = {
    Token.Prompt: PANORANGE,
    Token.PromptNum: PANORANGE,
    Token.OutPrompt: PANCYAN,
    Token.OutPromptNum: PANCYAN,
}

c.TerminalIPythonApp.display_banner = True
c.InteractiveShellApp.log_level = 20
c.InteractiveShellApp.exec_lines = [
    "import os",
    "import xml.etree.ElementTree as ET",
    "from dotenv import load_dotenv",
    "load_dotenv('/home/python/.env')",
    "PANURL = os.environ.get('PANURL', 'panorama.lab')",
    "PANUSER = os.environ.get('PANUSER', 'automation')",
    "PANPASS = os.environ.get('PANPASS', 'mysecretpassword')",
]
# c.InteractiveShell.colors = "Linux"
c.InteractiveShell.xmode = "Context"
c.InteractiveShell.banner1 = banner_start + banner_welcome + banner_env
c.InteractiveShell.banner2 = banner_url + banner_user + banner_pass + banner_end
c.TerminalInteractiveShell.confirm_exit = False
c.TerminalInteractiveShell.editor = "vi"
c.TerminalInteractiveShell.highlighting_style = "gruvbox-dark"
c.PrefilterManager.multi_line_specials = True

c.AliasManager.user_aliases = [("ll", "ls -al")]

# c.InteractiveShellApp.extensions = ["myextension"]
# c.InteractiveShellApp.exec_files = ["mycode.py", "fancy.ipy"]
