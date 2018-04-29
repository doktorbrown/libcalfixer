'''
Created on Dec 9, 2017
new header info formatting  042918

@author: teb15
'''


import csv

logLibCal = 'input.csv'
logOutput = 'formatted_output.csv'
headerFile = 'headerFile.csv'

# as of 042718
headerInfo = ("Space ID",
"Space Name",    
"Location",
"Category",    
"First Name",    
"Last Name",    
"Email",
"From Date",    
"From Time",    
"To Date",    
"To Time",  
"Status",    
"Showed Up",
"Booked by",  
"Class (IST 110 or n/a if none)",
"Number in Group", 
"Role: Student, Faculty, Staff", 
"Tech/Service",
"Type of Assignment" )  
    

def createTemplateCSV(headerFile,headerInfo):  #yeah we could have just read in a source file but this gives an output reference file too

           
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
        print "csv.list_dialects()",csv.list_dialects()
        
        for row in reader:
#check for old header
            a=row [17]
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
                row_to_enter=(row[0], row[1], row[2], row[3],row[4],row[5],row[6], row[9], row[10], row[11],row[12],row[15],row[16],row[18],row[20],row[22],row[26],row[28],row[30],'\r') 
#                 row_to_enter.strip("\"")
                logs = csv.writer(open(logOutput, 'a'))  #quotes are still here. use this as of 121017 and remove quotes once spreadsheet is imported
#                 logs = csv.writer(open(logOutput, 'a'),escapechar='\"', quoting=csv.QUOTE_NONE)  #quotes are removed but all data is repeated in column 20 for some reason
                logs.writerow(row_to_enter)
        print "log entries appended to", logOutput
    return




def main(headerFile,headerInfo,logOutput,logLibCal):
#     print "creating header"
    a=createTemplateCSV(headerFile,headerInfo)
#     print "writing header"
    c=writeHeader(headerFile,logOutput)
#     print 'reading source log'
    b=openIntermediateLog(logLibCal,logOutput)


    return a,c,b


main(headerFile,headerInfo,logOutput,logLibCal)      
print "great googly moogly the log processing is finished....to the batcave!"
 
         
            
            
            


