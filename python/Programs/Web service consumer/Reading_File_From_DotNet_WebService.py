from SOAPpy import WSDL
server = WSDL.Proxy('http://rtpqcmercuryb.rtp.netapp.com/almntf_webservice/Service1.asmx?WSDL')
print server.HelloWorld()
file ='C:\ALM_UIR_RUN\logs\sam.log'
print server.ReadSampleFile(fileName=file)
