import click,sys
import crypton as cr
import notesManager

def getPassword():
    tries = 0
    passw = ''
    while tries < 3:
        passw = click.prompt('Please enter the password', hide_input=False)
        if passw == '' or len(passw) < 3:
            print('Please enter a valid password. Password must be greater than 6 chars')
        else:
            return passw
        tries += 1
    sys.exit(1)


@click.group()
def cli1():
    pass

@cli1.command()
@click.option('-a', '--append', required=False, is_flag=False, help='Appends a note')
@click.option('-t', '--title',  required=False, is_flag=False, help='The title of the note')
@click.option('-l', '--list',   required=False, is_flag=True,  help='Reads the notes')
@click.option('-r', '--read',   required=False, is_flag=False, type=int, help='Reads a note by idx field')
@click.option('-n', '--new',    required=False, is_flag=True,  help='Creates a new notebloc')
@click.option('-t', '--all',    required=False, is_flag=True,  help='Lists all notes')
@click.option('-d', '--dump',    required=False, is_flag=True, help='Dumps the content')
@click.option('-q', '--remove',    required=False, is_flag=False, type=int, help='Removes a note by idx')
def notes(append,list,read,new,title,dump,all,remove):
    """Manage the notes"""
    nm = notesManager.NotesManager()
    if new:
        nm.new(getPassword())
    elif append:
        if not title:
            print("[ERROR] Has de especificar el titulo de la nota con --title ")
            sys.exit(1)
        nm.appendNote(getPassword(),append,title)
    elif list:
        nm.listNotes(getPassword())
    elif read:
        nm.readNote(getPassword(),read)
    elif dump:
        nm.dump(getPassword())
    elif all:
        nm.readAll(getPassword())
    elif remove:
        nm.removeIdx(getPassword(),remove)

cli = click.CommandCollection(sources=[cli1])

if __name__ == '__main__':
    cli()
