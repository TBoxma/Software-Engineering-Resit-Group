from src.frontend.cli import CLI

def serve_cli():
    cli_program = CLI("command_line_interface")
    cli_program.start()

if __name__ == '__main__':
    serve_cli()