# Hadoop set up:

- Install homebrew
- Brew install hadoop
- Config hadoop environment

https://isaacchanghau.github.io/post/install_hadoop_mac/


# Hadoop Workflow

- Create input data, mapper and reducer 

- Test the mapper and reducer locally to make sure it works

	cat input | mapper | sort | reducer

- Upload files from local machine to hadoop system:

	hdfs dfs -put {filename} {from_local_file_path} {to_hadoop_file_path}

	eg. Hdfs dfs -put wc_input.txt /home/student/wc_input.txt /user/student

- Run mapper and reducer in hadoop

hadoop \
    jar /opt/hadoop/contrib/streaming/hadoop-streaming-1.0.3.jar \
    -mapper "python $PWD/mapper.py" \
    -reducer "python $PWD/reducer.py" \
    -input "wordcount/mobydick.txt" \
    -output "wordcount/output"
