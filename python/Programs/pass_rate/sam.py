import re
def remove_duplicate_zapis(zapi_name,zapi_input):
    zapi_name_list=[]
    zapi_input_list=[]
    zapi_dictionary={}
    non_dup_zapi_name=None
    non_dup_zapi_input=None

    if zapi_name != None and zapi_input != None:        
        zapi_name_list=zapi_name.split('~')
        zapi_input_list=zapi_input.split('~')
        for i in range(0,len(zapi_name_list)):
            zapi_dictionary[zapi_name_list[i]]=zapi_input_list[i]
        
        for zp_name,zp_input in zapi_dictionary.iteritems():        
            if non_dup_zapi_name == None:
                non_dup_zapi_name=zp_name
                non_dup_zapi_input=zp_input
            else:
                non_dup_zapi_name=non_dup_zapi_name + "#" + zp_name
                non_dup_zapi_input=non_dup_zapi_input + "#" + zp_input
    else:
        non_dup_zapi_name=zapi_name
        non_dup_zapi_input=zapi_input      
        
    return non_dup_zapi_name,non_dup_zapi_input


  
  
zapi_name,zapi_input=remove_duplicate_zapis(zp_name,zp_input)        

print"\nAfter removing dup\n"

print"\nname:%s"%zapi_name
print"\ninput:%s"%zapi_input

