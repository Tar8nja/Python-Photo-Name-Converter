# # # # # # # # # # # # # # # # # # #                    
#                                   #
#       Code made by Tar8nja        #
#       under the MIT License       #
#                                   #
# # # # # # # # # # # # # # # # # # #

# Currently changes the name in the following format:
#
#               yyyymmdd-hhmmss-i
# 
# Where i is a value that changes to more than 0 if there are more than
# one image shot at the same second  
#
# I know the code is bad, but it works.


import os
import time
HOUR_DATE_SEPARATOR = '-'
SEPARATOR = ''
FILE_NAME = '_date_renamer.py'
MONTH = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06',\
         'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12' }


path = os.path.abspath(__file__).replace(FILE_NAME,'')
file_name_list = os.listdir(path)
print('Number of files: ', len(file_name_list)-1)
input('Press anything to continue, close the script to exit.')
print('The script is exectuing...')

previous_text = """Number of files: %i
Press anything to continue, close the script to exit.
The script is exectuing...""" %(int(len(file_name_list)-1))

j = 1
i = 0

date_text = ''
year_text = ''
month_text = ''
day_text = ''
hour_text = ''
try:
    for file in file_name_list:

        if(j%10 == 0 or j==len(file_name_list)):
            os.system('cls')
            print(previous_text)
            print("%.1f%% Complete..." % ( j/(len(file_name_list))*100) )
        j += 1


        
        if file == FILE_NAME:  
            continue # Skip this file

        file_extension = os.path.splitext(file)[1] # Get the extension

        if file_extension not in ['.jpg', '.jpeg', '.png', '.raw', '.arw', '.mp4', '.mts'
                                '.JPG', '.JPEG', '.PNG', '.RAW', '.ARW', '.MP4', '.MTS']:
            previous_text += 'File with the name ' + file + ' unable to modify.\n'
            continue # Only change names of images & videos

        if file_extension == '.mts':
            file_extension = '.mp4'
        elif file_extension == '.MTS':
            file_extension = '.MP4'



        elapsed_float = os.path.getmtime(path+file)
        time_stamp = time.ctime(elapsed_float)
        date_text = str(time_stamp)

        # Get the year in value (in text)
        year_text = date_text[-4:]

        # Get rid of day of the week for the name
        date_text = date_text   \
        .replace('Mon', '')     \
        .replace('Tue', '')     \
        .replace('Wed', '')     \
        .replace('Thu', '')     \
        .replace('Fri', '')     \
        .replace('Sat', '')     \
        .replace('Sun', '')

        # Get rid of space in front
        date_text = date_text[1:]

        # Get the month in value (in text)
        month_text = MONTH[date_text[:3]]

        # Get rid of space in front
        date_text = date_text[4:]

        # Convert 1 -> 01, 4 -> 04, etc.
        if(date_text[0] == ' '): date_text = date_text.replace(' ','0',1)

        # Get the day in value (in text)
        day_text = date_text[:2]

        # Get the hour, minute, second of the shot (in text)
        hour_text = date_text[3:11].replace(':', SEPARATOR)

        # Define the date
        date_text = year_text+SEPARATOR+month_text+SEPARATOR+day_text

        # Define the final name
        final_name = date_text+HOUR_DATE_SEPARATOR+hour_text



        K = True
        new_text_date = final_name + HOUR_DATE_SEPARATOR + str(i) + file_extension
        while(K):
            try:
                os.rename(os.path.join(path,file),os.path.join(path,(new_text_date)))
                K = False
            except:
                new_text_date = final_name + HOUR_DATE_SEPARATOR + str(i) + file_extension
                i += 1

except:
    print('Something went wrong.')

input('The script has finalized.\nPress anything to exit.')