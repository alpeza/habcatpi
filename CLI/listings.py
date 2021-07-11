import os


def examineYaml(yamlfile):
    print('Holi')

def listDirsInFolder(folder):
    folders=[]
    files = os.listdir(folder)
    for file in files:
        print('- ' + file)
