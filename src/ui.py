from rich.console import Console
console=Console()

def run_cli(engine):
    console.print('[bold green]Mission Control AI[/bold green]')
    while True:
        q=input('❯ ')
        if q=='/exit': break
        if q=='/status':
            console.print(engine.status_snapshot())
            continue
        console.print(engine.analyze(q))
