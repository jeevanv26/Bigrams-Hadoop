I implemented two mappers and reducers and tested them on a cluster.

Command used for first job:
mapred streaming -files mapper.py,reducer.py -mapper 'python mapper.py' -reducer 'python reducer.py' -input hw1 -output job_one


Command used for second job:
mapred streaming -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.num.map.output.key.fields=2 -D mapred.text.key.comparator.options=-k1,2 -D mapred.text.key.partitioner.options=-k1,1 -D mapred.reduce.tasks=12 -files second-mapper.py,second-reducer.py -mapper 'python second-mapper.py' -reducer 'python second-reducer.py' -input job_one -output final_output -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

Total unigrams seen and Total bigrams seen were read of the screen and manually inserted into second-reducer.py file from stderr.

