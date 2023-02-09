# Configuration file for ipython.
from IPython.terminal.prompts import Prompts, Token


class MyPrompt(Prompts):
    def in_prompt_tokens(self, cli=None):
        tokens = [(Token.Prompt, "λ  ")]
        return tokens

    def out_prompt_tokens(self):
        tokens = [(Token.OutPrompt, "⮎  ")]
        return tokens


c = get_config()  # noqa

banner_start = "-" * 64 + "\n\n"
banner_welcome = "Welcome to the Palo Alto Networks Prisma SASE container\n\n\n"
banner_env = "Environment is being loaded from the /root/.panapi/config.yml file\n\n"
banner_session = "\tYou are authenticated with Prisma, use the `session` object to reference your active session\n"
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
    "from panapi import PanApiSession",
    "import pandas as pd",
    "from tabulate import tabulate",
    "session = PanApiSession()",
    "session.authenticate()",
]
# c.InteractiveShell.colors = "Linux"
c.InteractiveShell.xmode = "Context"
c.InteractiveShell.banner1 = banner_start + banner_welcome + banner_env
c.InteractiveShell.banner2 = banner_session + banner_end
c.TerminalInteractiveShell.prompts_class = MyPrompt
c.TerminalInteractiveShell.confirm_exit = False
c.TerminalInteractiveShell.editor = "vi"
c.TerminalInteractiveShell.highlighting_style = "gruvbox-dark"
c.PrefilterManager.multi_line_specials = True

c.AliasManager.user_aliases = [("ll", "ls -al")]

# c.InteractiveShellApp.extensions = ["myextension"]
# c.InteractiveShellApp.exec_files = ["mycode.py", "fancy.ipy"]
