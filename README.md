### Thanking

It is really impressing and cool as project. I have just documented myself and it is bluffing. So I would like to thank you for this challenge, this constructive and heavy problem that I loved working. I have seen your mail around 11pm UK Time, and with this constintancy, I have worked all the night and, certainly, I would improve the render. I mean that this is just a primary solution resolved in few hours. But, I would improve it and generate a web render example in the next two days.  

### Warning
I am using Ubuntu. It seems that installing word2vec on windows or Mac is not stable. It is mentioned in their official website.

### Testing 

Kindly note, that I was not able to test theproject with my computer. Testing only negative comments required about 1 hour to find out a little bug after that. So I tested my work on a little sample of text. As training data were small, results were not convincing. I would deploy it in a free server and test it.

With this huge amount of data, I generated only Negative reviews training. It would be the same thing for positive reviews by changing the name of the file of simply to add a new list.

### Tutorial
The principle is simple. By downloading the folder, you may install some librairie and run the script, it would take the unsupervised comments text file in the folder and test it depending on positive and negative sets in the two other files.
As a first solution, this would generate a csv file in the same folder with sentiment of each comment. But, I would set up a web application for a sophisticated view in the next two days if you agree.

Librairies used in the project : 
1- os : This lib is used only to link the script to the different text files in the folder
2- re : Regular expression lib for splitting words.
3- numpy : As word2vec required 2D vectors as set, I used numpy to define these vectors fast and in a simple way
4- gensim : You asked for that, it is a lib where I imported word2vec
5- scikitlearn : For classification, I turned to scikitlearn library.
6- pandas : to generate the final csv file, I used, temporarily, pandas library. But if I turned to a web application, I would remove this lib.


### Steps

1- Place your training data in the folder where the script
2- Using text files with huge amount of data, instead of opening files usually, I treated files as objects and browsed them line by line. In this case, and only in this one, this is a great approach because every comment is mentionned in a line. So, browsing files with this method would allows us to split different comments and in the same time gain time processing.
3- To prepare the data to use it in the model of word2vec, two lists, clean_train_comment and clean_test_comment, were initiated and after that appended with corresponding sentences.
4- By generating the model, with defining differents features:
- Nbr of Threats that would be executed for the project.
- The word vector dimentianlity
- The minimum nuber of word counts.
- The sample

The script is well commented, I would write another, as web tutorial, detailing how setup these librairies and how to run the script with its different functionalities.

### Opinion
This is the kind of challenges that I want to work on. I only figured out your mail at 11pm UK Time and I worked until now 04 UK Time on this first and primary solution. Sincerly, I hope to be selected.