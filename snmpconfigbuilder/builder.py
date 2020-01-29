#The builder takes a TXT file with OIDs and if necessary a device type.
import sys
import snmpconfigbuilder.configfileloader

def validateArguments(arguments):
    if(len(arguments) < 2):
        print("Too few arguments - you must provide at least a model file!")
        return False
    else:
        return True

if __name__ == '__main__':
    if(not validateArguments(sys.argv)):
        print("Incorrect arguments - please try again!")
    inputFile = sys.argv[1]
    baseModel = sys.argv[2]
    print("Will now generate a YAML template from file " + inputFile + " with base model " + baseModel)
    config = []
    snmpconfigbuilder.configfileloader.loadCSV(inputFile,config)
    if(len(config) == 0): sys.exit(-1)
