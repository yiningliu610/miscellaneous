This pr extracts the features from aurora blog posts, consolidates the blog traffic data from google analytics, and does some initial eda on the blog features.

blog_class.ipynb: 

	input: url of any blog in aurora blog
	
	function: turn the blog article into an object which would return the features in the file variables.txt such as author, word count, sentence length, reading_level ...
	
	output: features of the blog 
	
all_blogs.ipynb:
	
	input: data of each blog's traffic in google analytics saved as ga.csv 
	
	function: summarize the performance of each blog and normalize it to daily performance
	
	output: a giant data frame with each row to be a blog and each column to be the traffic from google analytics and features from blog class
	
eda_modeling.ipynb:

	input: the giant data frame from all_blogs.ipynb along with the categorical variables with manual input
	
	https://docs.google.com/spreadsheets/d/1DJbsjTALDd6annAwbyGrpiLg2iFFHQUN-XQ5Ap2A1RE/edit#gid=0

	function: eda 
	
	output: relationships between variables

	