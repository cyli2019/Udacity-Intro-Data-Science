__author__ = 'unifireseeker'
import csv

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:
    
    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''
    for name in filenames:
        # your code here
        f_in = open(name, 'r')
        new_name = 'updated_'+name
        f_out = open(new_name, 'w')
        
        read_in = csv.reader(f_in, delimiter=',')
        
        for row in read_in:
            head3 = row[0] +','+ row[1]+','+ row[2]
            rep_times = int((len(row)-3)/5)
            
            for i in range(rep_times):
                new_row = head3 +','+row[3+i*5]+','+row[4+i*5]+','+row[5+i*5]+','+row[6+i*5]+','+row[7+i*5]
                f_out.write(new_row)
                f_out.write('\n')
    
    f_in.close()
    f_out.close()
           
            
            
