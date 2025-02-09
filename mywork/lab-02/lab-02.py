import requests
import csv
from xml.dom.minidom import parseString

### 8
retrieveTags=['TrainStatus',
              'TrainLatitude',
              'TrainLongitude',
              'TrainCode',
              'TrainDate',
              'PublicMessage',
              'Direction'
              ]

### 2
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# check it works
#print (doc.toprettyxml()) #output to console, all the data.

######################################
# if I want to store the xml in a file. You can comment this out later
#with open("trainxml.xml","w") as xmlfp:
#    doc.writexml(xmlfp)
######################################

### 4
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")

for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    #print (traincode) #--------Works----------------------

### 5
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainLongitude").item(0)
    trainlongitude = traincodenode.firstChild.nodeValue.strip()
    #print (trainlongitude) #--------Works----------------------


### 6-8
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-r
# adding the newline= '' parameter, for no blank lines in the file.
with open('week02_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()

        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)

### 9
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    
filtered_trains = []
for trainD in objTrainPositionsNodes:
    traincode = trainD.getElementsByTagName("TrainCode")[0].firstChild.nodeValue.strip()
    if traincode.startswith("D"):
        status = trainD.getElementsByTagName("TrainStatus")[0].firstChild.nodeValue.strip()
        latitude = trainD.getElementsByTagName("TrainLatitude")[0].firstChild.nodeValue.strip()
        longitude = trainD.getElementsByTagName("TrainLongitude")[0].firstChild.nodeValue.strip()
        date = trainD.getElementsByTagName("TrainDate")[0].firstChild.nodeValue.strip()
        message = trainD.getElementsByTagName("PublicMessage")[0].firstChild.nodeValue.strip()
        direction = trainD.getElementsByTagName("Direction")[0].firstChild.nodeValue.strip()
            
        filtered_trains.append([status, latitude, longitude, traincode, date, message, direction])

with open('week02_train_D.csv', mode='w', newline='') as train_file_2:
    train_writer_2 = csv.writer(train_file_2, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # train_writer.writerow(["TrainStatus", "TrainLatitude", "TrainLongitude", "TrainCode", "TrainDate", "PublicMessage", "Direction"])
    train_writer_2.writerows(filtered_trains)