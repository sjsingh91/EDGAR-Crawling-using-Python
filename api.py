import wget
fp = open('file path where you saved form.gz', 'r')
#removing the header, so taking data from line number 11.
data=fp.readlines()[11:]
fp.close()

#Code for getting the file path aligned with the database and writing in the directory

for lines in data:
    temp=lines.split('\n')[0]
    temp=temp.split()
    if((temp[0]=='10-K') & (int(temp[-2][5:7])==1)):
        response = wget.download('http://www.sec.gov/Archives/'+temp[-1],'secData/')