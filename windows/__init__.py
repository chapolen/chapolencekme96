from rich.live_render import LiveRender
from rich.console import Console
from rich.panel import Panel
import os, shutil
import sys

console = Console()

def hata (text):
   console.print(Panel(f'[bold red]{text}[/]',width=70),justify="center")    
   sys.exit()                     
def bilgi (text):
   console.print(Panel(f'[blue]{text}[/]',width=70),justify="center")  
def passed (text):
   console.print(Panel(f'[yellow]{text}[/]',width=70),justify="center") 
def noadded (text):
   console.print(Panel(f'[pink]{text}[/]',width=70),justify="center")  
def basarili (text):
   console.print(Panel(f'[bold green] {text}[/]',width=70),justify="center")                         
def onemli (text):
   console.print(Panel(f'[bold cyan]{text}[/]',width=70),justify="center")                         
def soru (soru):
   console.print(Panel(f'[bold pink]{soru}[/]',width=70),justify="center")                         
   return console.input(f"[bold pink]>> [/]")
def logo ():
   text = "█▀▀ █▀▀ █▀█ █▀▀ █▀▀ █▄█ █▄░█\n█▄▄ ██▄ █▀▄ █▄▄ ██▄ ░█░ █░▀█"
   console.print(Panel(f'[bold cyan]{text}[/]',width=90),justify="center") 
