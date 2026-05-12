Miquel Àngel Senar Rosell
0 minutes 4 seconds0:04
Miquel Àngel Senar Rosell 0 minutes 4 seconds
OK, principle, everything seems to be working fine. So what we are going to talk about today basically.
Miquel Àngel Senar Rosell 0 minutes 15 seconds
We will have two main topics here in today's session. First of all, we will review a little bit about the theory or the the theoretical concepts behind the idea of modules in Python.
Miquel Àngel Senar Rosell 0 minutes 31 seconds
And then we will briefly go through some of the most useful, I would say, or some of the packages or modules that may be more useful for you.
Miquel Àngel Senar Rosell 0 minutes 46 seconds
In in the field of bioinformatics or in the with the idea of developing workflows that deal with biomedical data, because to some extent most of the these.
Miquel Àngel Senar Rosell 1 minute 5 seconds
Topics or subjects that we have been talking about in the last weeks have the the, the, the goal or the emphasis or the the idea of all the IES tools that we are seeing.
Miquel Àngel Senar Rosell 1 minute 23 seconds
Is basically with the underlying idea of developing workflows that can take by your any sort of biomedical data and then analyze it through different steps until you reach out an output that.
Miquel Àngel Senar Rosell 1 minute 40 seconds
Generate or provide some kind of information about that data in terms of.
Miquel Àngel Senar Rosell 1 minute 50 seconds
What's available there? What are the consequences or what are the characteristics of that data, and what are the consequences or what are the conclusions that can be explained obtained from that that data? And then the data has to go through several steps of filtering, curating, matching or comparing data, comparing data.
Miquel Àngel Senar Rosell 2 minutes 10 seconds
Or you have DNA or RNA data, comparing that data with available databases and that sort of stuff. So at the end, analyzing biomedical data is not something that is done by a single step, so you usually.
Miquel Àngel Senar Rosell 2 minutes 30 seconds
We go through several steps until you have some specific output and then going through those steps can be done by writing applications that will control these kind of workflows and then our emphasis.
Miquel Àngel Senar Rosell 1 hour 20 minutes 21 seconds
That can be used basically to perform some kind of file manipulation. And by file manipulation I mean everything that you want you can do with a file, copy, removing, moving.
Miquel Àngel Senar Rosell 1 hour 20 minutes 38 seconds
You can traverse a a folder, you can traverse all the folders and all the subfolders. Then you have make several methods and several mechanisms included in OS or in passive that can be used.
Miquel Àngel Senar Rosell 1 hour 20 minutes 54 seconds
In combination with the subprocessor one to build complex applications that can manipulate data located in different places in your in your system. OK, for instance, you can get the current working directory, you can change directories.
Miquel Àngel Senar Rosell 1 hour 21 minutes 11 seconds
Change directories. You can obviously get a list of all the files in a different folder. You can get the same either by a list or you can get an iterator. Then you have examples here that illustrate how to use these.
Miquel Àngel Senar Rosell 1 hour 21 minutes 28 seconds
These methods to get the list of all the files or how to to navigate through all the files and to get information from all the files and then from the files, especially when you're using these last two methods.
Miquel Àngel Senar Rosell 1 hour 21 minutes 45 seconds
You can get information not only about the name of the file, but also the size of the files. And here you have a list of all the attributes that you can manipulate the time of where the file was created, the information about the user who who has the owner of the file, the group owner of the file, and many, many.
Miquel Àngel Senar Rosell 1 hour 22 minutes 5 seconds
Any other information about the file can be get from this attribute list that can be used by these methods. And then eventually if you want to create folders, you have different methods for creating folders or you have even this is one of.
Miquel Àngel Senar Rosell 1 hour 22 minutes 24 seconds
One of the most interesting methods that are available is a work. The work method that can be used to move you around a specific tree in the system.
Miquel Àngel Senar Rosell 1 hour 22 minutes 40 seconds
So if you want to move up and down or you want to get all the files, all the folders and all the subfolders starting in a specific place in the system, this OS work method can be very handy. OK, here you have an example.
Miquel Àngel Senar Rosell 1 hour 22 minutes 56 seconds
That shows you how we can you can traverse and how you can get all the files that are located in a specific subtree of the system.
Miquel Àngel Senar Rosell 1 hour 23 minutes 10 seconds
OK, so I am leaving this just with examples just to to to check them. OK and to and to and to and to look at them quietly if you if you need.
Miquel Àngel Senar Rosell 1 hour 23 minutes 26 seconds
To develop an application that sometimes needs to to to move around the the specific folders or the specific files of the system, right? And then finally, just to conclude today, there are some utility functions.
Miquel Àngel Senar Rosell 1 hour 23 minutes 43 seconds
That can be used to copy files, to copy a whole tree, for a copy, to copy a whole folder or a complete folder. And then you can compress and move and rename files. OK, rename files or rename. You can rename folders and finally you can find.
Miquel Àngel Senar Rosell 1 hour 24 minutes 3 seconds
Specific files according to a pattern or you can finally you can have these miscellaneous modules that can be used to compress and to to to use temporary files. OK, you want to compress files in different formats or you can compress folders or that sort of stuff.
Miquel Àngel Senar Rosell 1 hour 24 minutes 22 seconds
OK so I am leaving this just as a as an information. You don't have all the the methods but you have you can refer to them and then you can go to the documentation if you need to to to manipulate files in some specific way but the the least.
Miquel Àngel Senar Rosell 1 hour 24 minutes 41 seconds
Of all the transparencies that we have seen are basically they contain the most relevant and I think that the most useful methods that can be used if you have to do some kind of.
Miquel Àngel Senar Rosell 1 hour 24 minutes 57 seconds
File manipulation or folder manipulation from a program we can in Python. OK, you have. We are not going to go into this bio Python part here maybe, but when we come back from from holidays in.
Miquel Àngel Senar Rosell 1 hour 25 minutes 15 seconds
In after Easter holidays we we we can cover this part. If we don't have time to to go through this Bio Python, I just want you to to to check them and to take a look at because Bio Python itself contains also it. It's an important.
Miquel Àngel Senar Rosell 1 hour 25 minutes 34 seconds
Package that contains many useful methods that can be used, especially if you want to manipulate sequences and that sort of information. So sequences coming from different in different formats or in different databases.
Miquel Àngel Senar Rosell 1 hour 25 minutes 51 seconds
DNA protein sequences, then Bio Python. The Bio Python package has a significant amount of elements that can simplify significantly the the manipulation of that kind of data. OK, even accessing remotely to to NCBI databases and so on.
Miquel Àngel Senar Rosell 1 hour 26 minutes 10 seconds
And you have several examples here for for the to illustrate how to do some some of these more more common operations. The Bio Python package has also several modules related to.
Miquel Àngel Senar Rosell 1 hour 26 minutes 27 seconds
Phylogenetics and proteomics and that's quite the specific. If you need or you have a a field of application that fits one of those fields, maybe it's worth to to to take a look at that what is available in in in there, OK.
Miquel Àngel Senar Rosell 1 hour 26 minutes 46 seconds
From my point of view, I just want to to conclude here. So the the the most important stuff were related with the modules and the some personal run and then this quick review.
Miquel Àngel Senar Rosell 1 hour 27 minutes 1 second
Of other modules or other methods available to to manipulate files. You have all the information available here and then you can simply navigate through these transparencies if you have some kind of a specific.
Miquel Àngel Senar Rosell 1 hour 27 minutes 17 seconds
Need to manipulate files in some specific way, and you have examples here illustrating the usage of such methods. There is no single package or no single module that solves everything, and you will see that there are different options for doing the same stuff in different ways.
Miquel Àngel Senar Rosell 1 hour 27 minutes 37 seconds
But in principle, most common operations can be solved by the methods that are listed in this set of transparencies. So OK, nothing else from my side. I don't know if you have any other.
Miquel Àngel Senar Rosell 1 hour 27 minutes 55 seconds
Any further question or any other, anything that you want to to add or to to ask right now?
Miquel Àngel Senar Rosell 1 hour 28 minutes 4 seconds
If not, we are going to do.
Miquel Àngel Senar Rosell 1 hour 28 minutes 9 seconds
To close the session now.
Miquel Àngel Senar Rosell 1 hour 28 minutes 13 seconds
So thank you for attending it. I will close the.
Miquel Àngel Senar Rosell 1 hour 28 minutes 18 seconds
Yeah.
Miquel Àngel Senar Rosell 1 hour 28 minutes 20 seconds
The recording.
Miquel Àngel Senar Rosell 1 hour 28 minutes 24 seconds
And.
Miquel Àngel Senar Rosell 1 hour 28 minutes 26 seconds
OK. So thank you for attending the session and eventually tomorrow Sandra will be back with you and probably, well, not today, but in the next days, probably before Easter holidays.
Miquel Àngel Senar Rosell 1 hour 28 minutes 44 seconds
I will publish one assignment that will include most of the middleware tools that we have already seen up to now, so stay tuned to that.
Miquel Àngel Senar Rosell 1 hour 28 minutes 57 seconds
And if nothing, if you don't have anything else to say, we I am going to close the session. So thank you for attending and see you see you soon.