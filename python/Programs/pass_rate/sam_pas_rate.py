import re

#**************************** Helper methods of pass rate *************************
def isSystemicValueCorrect(ssfv):
    valid = 0

    p = re.compile('^(\d{1,3}):(\d{1,2}):(\d{1,2})$')
    m = re.match(p, ssfv)
    if m:
        valid = 1        
    else:
        valid = 0
        
    return valid
    

def convertSystemicValueToSecs(ssfv):
    secs = 0
    p = re.compile('^(\d{1,3}):(\d{1,2}):(\d{1,2})$')
    m = re.match(p, ssfv)
    secs = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
    
    return  secs

def getPassRate(ttff, ert, status):
    pass_rate = "0.00"
    
    if ttff and ert:
        _ttffSecs = convertSystemicValueToSecs(ttff)
        _ertSecs = convertSystemicValueToSecs(ert)
        if(_ttffSecs > 0 and _ertSecs > 0):
            pass_rate = round(((_ttffSecs * 1.0) / _ertSecs),2)
            if(pass_rate > 1):
                pass_rate = "1.00"
        else:
            if status == "Passed":
                pass_rate = "1.00"
            else:
                pass_rate = "0.00"
    else:
        if status == "Passed":
            pass_rate = "1.00"
        else:
            pass_rate = "0.00"
            
    return pass_rate

#**************************** Helper methods of pass rate *************************

rn_ttff = "222:22:22"
rn_ert = "222:22:22"
rn_run_status = "failed"

if isSystemicValueCorrect(rn_ttff):    
    if isSystemicValueCorrect(rn_ert):
        print "ttff:%s\nert :%s\nrun status:%s"%(rn_ttff,rn_ert,rn_run_status)
        print"pass rate:%s"%getPassRate(rn_ttff, rn_ert, rn_run_status)
    else:
        print "qc-push log: Epected Run Time value '%s' is not in correct format. It should be in the format HHH:MM:SS\n(In this case you can set pass rate value based on run status. 1.00 for Passed run, 0 for other status runs.)"%rn_ert
else:
    print "qc_push log: Time To First Failure value '%s' is not in correct format. It should be in the format HHH:MM:SS\n(In this case you can set pass rate value based on run status. 1.00 for Passed run, 0 for other status runs.)"%rn_ttff
