import time
import pymongo

# Open the log file in read mode
with open('demofile.log', 'r') as log_file:
  # Open the text file that keeps track of the total number of lines read from the log file
  with open('count.txt', 'r') as line_count_file:
    # Read the total number of lines read from the log file from the text file
    line_count = int(line_count_file.read())
    # Seek to the line after the last line that was read from the log file
    log_file.seek(line_count)

  # Read the log file line by line
  while True:
    # Read a line from the log file
    line = log_file.readline()
    if line:
      # Print the line
      print(line)
      # Increment the total number of lines read from the log file
      line_count += 1
      # Write the new total number of lines read from the log file to the text file
      with open('count.txt', 'w') as line_count_file:
        line_count_file.write(str(line_count))
    else:
      # Sleep for 5 minutes if there are no new lines in the log file
      print ('i have read all the data, now i will sleep for 5 minutes and lets hope there will be new data when i wake up')
      time.sleep(300)
      
