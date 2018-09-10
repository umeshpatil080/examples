from SOAPpy import WSDL
server = WSDL.Proxy('http://localhost:3948/Service1.asmx?WSDL')
print server.HelloWorld() # works correctly - just prints a hello message
a=server.anotherSimpleMethod(firstNum=3, secondNum=4) 
print a
b=server.Add(1,2)# does not work - returns zero
print b
print server.Add(a=1,b=2)
print server.simpleMethod(srt="Sam")

file ='C:\sqlnet.log'
print server.ReadSampleFile(fileName = file)

