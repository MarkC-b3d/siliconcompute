<<<<<<< HEAD
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
import os
from os import system, name
import subprocess


def init():
    # for windows
    if name == 'nt':
        _ = system('cls')
        deploy = Panel(Text("Deploy Silicon Render Node v1.0", style="bold green", justify="Left"))
        prod_panel = Panel(Text("<===================| EXPERIMENTAL BUILD |===================>", style="bold red", justify="center"))
        print(deploy)
        print(prod_panel)
        dir_check()
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        _ = system('cls')
        deploy = Panel(Text("Deploy Silicon Render Node v1.0", style="bold green", justify="Left"))
        prod_panel = Panel(Text("<===================| EXPERIMENTAL BUILD |===================>", style="bold red", justify="center"))
        print(deploy)
        print(prod_panel)
        dir_check()


def dir_check():
    if os.path.isdir('./silicon'):
        console = Console()
        text = Text("Silicon Directory Exists...skipping")
        text.stylize("bold blue")
        console.print(text)
    else:
        git_clone()


def git_clone():
    console = Console()
    text = Text("Downloading Silicon....")
    text.stylize("bold blue")
    subprocess.Popen("git clone https://github.com/MarkC-b3d/silicon")
    console.print(text)

def finish():
    finish_panel = Panel(Text("Silicon Deployment Complete", style="bold red", justify="center"))
    finish_panel2 = Panel(Text("Please run snap_blender.sh", style="bold red", justify="center"))
    print(finish_panel)
    print(finish_panel2)

init()
=======
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
import os
from os import system, name
import subprocess


def init():
    # for windows
    if name == 'nt':
        _ = system('cls')
        deploy = Panel(Text("Deploy Silicon Render Node v1.0", style="bold green", justify="Left"))
        prod_panel = Panel(Text("<===================| EXPERIMENTAL BUILD |===================>", style="bold red", justify="center"))
        print(deploy)
        print(prod_panel)
        dir_check()
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        _ = system('cls')
        deploy = Panel(Text("Deploy Silicon Render Node v1.0", style="bold green", justify="Left"))
        prod_panel = Panel(Text("<===================| EXPERIMENTAL BUILD |===================>", style="bold red", justify="center"))
        print(deploy)
        print(prod_panel)
        dir_check()


def dir_check():
    if os.path.isdir('./silicon'):
        console = Console()
        text = Text("Silicon Directory Exists...skipping")
        text.stylize("bold blue")
        console.print(text)
    else:
        git_clone()


def git_clone():
    console = Console()
    text = Text("Downloading Silicon....")
    text.stylize("bold blue")
    subprocess.Popen("git clone https://github.com/MarkC-b3d/silicon")
    console.print(text)
    
init()
>>>>>>> 1c12ffd011bae4336b4ec51855acea445a16d0ae
