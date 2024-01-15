"""
We have a collection of servers globally distributed.  Each server streams log messages to a central 
server that dumps these logs to disk.  Given their physical distribution and variation of network 
delays, the records may not be received by the central server, and therefore not written to disk, in 
strict time order.  The central server produces a new file daily and these files are used for analytics. 
For my analytical processing I want the log messages to be in strict time order.  

Please write me a program, that for a given file on disk which contains records, 
will create a new file with the same records but in time order.
"""


# same time stamp - order not should 


def read_file(file_name):
  from collections import heapq
  # time stamp, line number
  
  # 10 gb file

  file_ts_heap = []
  heapq.heapify(file_ts_heap)
  max_line = 1000
  
  fileName = "Data"
  creation_index = 0
  file = open(fileName)
  currCount = 0
  currDataMap = {}
  fileMaps = {}
  file_size = defaultdict(int)
  for line in file.readline(): # timestamp: ddata"
    currCount+=1
    timeStamp,data = file.split(":")
    currDataMap[timeStamp]=data
    currDatMap[]
    if currCount = maxLine:
      currCount=0
      fileToWrite = fileName+str(creation_index)
      loweset_time, start_line,fileName,max_records = push_intermediate_file(fileToWrite,currDataMap)
      # time stamp, file to read, 
      heap.heappush(file_ts_heap,(loweset_timestamp,fileName,line_to_read)) # 0,file 3,0 , 100,file2,0 
      creation_index+=1
      currDataMap = {}
    	file_size[fileName]=max_records
    # how_many_files = creation_index
    
    
    
    
    while file_ts_heap:
      loweset_timestamp,file.line_to_read = heapq.heappop(file_ts_heap)
      # method to read a data from the file and also topmost record after reading the first record
      data,line_read,timestamp = read_first_line(file,line_to_read)
      write_to_output(data)
      # remove_first_line(file)
      #_,timestamp = read_first_line(file) 
      # check end of the file before pushing on the heap
      file_size[file]-=1
      if file_size[file]:
      	heapq.heappush(file_ts_heap,(timestamp,file)) # size of heap will be O(files lenght)
      
    
  # reduce the records
  
  	
  	
      
  def push_intermediate_file(fileName,currDataMap)->(dateimte,int,fileName,max_records): 
    data_tuple = currDataMap.items()
    data_tuple = list(data_tuple)
    data_duple.sort(key=lambda item:item[0]) # nlogn
    f = open(fileName)
    # use the with clause to make this safe operation
    line_number=0
    for t,d in data_duple:
      f.write(line_number,t,d)
      line_number+=1
    f.close()
    
    return lowest_timestamp,fileName,line_number
  
  
  