'''
Created on Dec 9, 2017

@author: teb15
'''


import csv

logLibCal = 'source.csv'
logOutput = 'formatted_output.csv'
headerFile = 'headerFile.csv'

def createTemplateCSV(headerFile):  #yeah we could have just read in a source file but this gives an output reference file too
    headerInfo = (
        "Item ID",
        "Item Name",    
        "First Name",    
        "Last Name",    
        "Email",    
        "Account",    
        "From Date",    
        "From Time",    
        "To Date",    
        "To Time",    
        "Created Date",    
        "Created Time",    
        "Status",    
        "Showed Up",    
        "Role: Student, Faculty, Staff",  
        "Type of Assignment",    
        "Tech/Service",    
        "Number in Group",    
        "Class (IST 110 or n/a if none)",    
        "Booked by")


           
    logs = csv.writer(open(headerFile, 'wb'))
    logs.writerow(headerInfo)
    print "header written to output file"
    return()
# 

                 
# #Now output to row 1 in input csv. turn this into output function
def writeHeader(infile,logOutput):  #now write the header info to the output file
    reader = csv.DictReader(open(infile))
    headers = reader.fieldnames

    with open(logOutput, 'wb') as outcsv:
        writer1 = csv.writer(outcsv)
        writer1.writerow(headers)
    
    return

def openIntermediateLog(inputFile,logOutput):
    with open(inputFile, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|') 
# #     start parsing existing columns from each row for formatted output
#     print reader[0,1]
#         print "csv.list_dialects()",csv.list_dialects()
        
        for row in reader:
#check for old header
            a=row [14]
            z=str('Booking Form Answers')
#             print a[1:21],z           
            if a[1:21]==z:
                print "header is valid"
                print "rewriting input file to output"
                
            else:

# deal with commas
#                 role=str(row[14]+","+row[15]+","+row[16])
#                 print role
# append each row to header file copy
#                 print type(row)
                row_to_enter=(row[0], row[1],row[2], row[3], row[4],row[5],row[6],row[7], row[8], row[9], row[10],row[11],row[12],row[13],row[17],row[19],row[21],row[23],row[25],row[27],'\r') 
#                 row_to_enter.strip("\"")
                logs = csv.writer(open(logOutput, 'a'))  #quotes are still here. use this as of 121017 and remove quotes once spreadsheet is imported
#                 logs = csv.writer(open(logOutput, 'a'),escapechar='\"', quoting=csv.QUOTE_NONE)  #quotes are removed but all data is repeated in column 20 for some reason
                logs.writerow(row_to_enter)
        print "log entries appended to", logOutput
    return 




def main(headerFile,logOutput,logLibCal):
#     print "creating header"
    a=createTemplateCSV(headerFile)
#     print "writing header"
    c=writeHeader(headerFile,logOutput)
#     print 'reading source log'
    b=openIntermediateLog(logLibCal,logOutput)


    return a,c,b


main(headerFile,logOutput,logLibCal)      
print "great googly moogly the log processing is finished....to the batcave!"
 
         
            
            
            


