import click,sys
import config
import listings

#--- UPDATE
@click.group()
def cli2():
    pass
@cli2.command()
@click.option('-e', '--habcatev', required=False, is_flag=True, help='Update de habcatev')
@click.option('-c', '--components', required=False, is_flag=True, help='Update de componentes')
def update(habcatev,components):
    """Realiza el update de librerías"""

#--- DEVICES
@click.group()
def cli4():
    pass
@cli4.command()
def devices():
    """Lista los dispositivos habcat"""
    listings.listDirsInFolder(config.devices_path)


#--- COMPONENTS
@click.group()
def cli5():
    pass
@cli5.command()
def components():
    """Lista los componentes habcat"""
    listings.listDirsInFolder(config.components_path)



#--- STOP
@click.group()
def cli3():
    pass
@cli3.command()
@click.option('-d', '--device', required=True, is_flag=False, help='Dispositivo a ejecutar')
def stop(device):
    """Para un dispositivo"""
    print('Parando ' + device + ' ...')

#--- RUN
@click.group()
def cli1():
    pass
@cli1.command()
@click.option('-d', '--device', required=True, is_flag=False, help='Dispositivo a ejecutar')
def run(device):
    """Ejecuta un dispositivo"""
    print('Launching ' + device + ' ...')


cli = click.CommandCollection(sources=[cli1,cli2,cli3,cli4,cli5])

if __name__ == '__main__':
    cli()
