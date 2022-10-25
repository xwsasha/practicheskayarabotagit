def openFile():
    try:
        f1=open('data.txt', 'r')
        while True:
            data = f1.readline().split("-")
            print(data)
            if data[0] == '':
                break
            return data
        f1.close()
    except IOError:
        print(IOError.with_traceback())

def dateMonth():
    data2=openFile()
    print(data2)
    data1=['31', '12', '1900']
    if int(data2[0]) < int(data1[0]):
        data1[0] = data2[0]
    if int(data2[1]) < int(data1[1]):
        data1[1] = data2[1]
    print(data1[0], "-", data1[1])











