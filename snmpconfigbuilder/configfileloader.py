import csv

def loadCSV(filename,targetVariable):
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0: line_count += 1
                else:
                    targetVariable.append([row[0],row[1],row[2]])
            print(f'Processed {line_count} lines.')
    except:
        print("Could not read CSV File!")


