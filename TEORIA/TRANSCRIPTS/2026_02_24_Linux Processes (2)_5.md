Miquel Àngel Senar Rosell
0 minutes 5 seconds0:05
Miquel Àngel Senar Rosell 0 minutes 5 seconds
Okay.
Miquel Àngel Senar Rosell 0 minutes 6 seconds
So, we are ready to go.
Miquel Àngel Senar Rosell 0 minutes 13 seconds
Welcome back to these sessions. We are going to resume and review very briefly the things that we saw last two weeks ago when we were talking about processes in Linux and how to run
Miquel Àngel Senar Rosell 0 minutes 32 seconds
multiple processes in the background and the idea of processes in the background and processes in the foreground. If you remember very briefly when we run something on the common line of Linux, that process is what we call a foreground process.
Miquel Àngel Senar Rosell 0 minutes 54 seconds
we don't get back the the control of the cursor until the process that we have started has been finished. And this is something that you you can see here.
Miquel Àngel Senar Rosell 1 minute 8 seconds
So that this is an example of a foreground process or what we call also a synchronous process in the sense that we can interact with the system again when the process is finished. So that's why we are synchronized with the process. If we add these ampersand
Miquel Àngel Senar Rosell 1 minute 27 seconds
symbol at the end of the process, that process will run asynchronously so we can continue typing commands on the on the terminal while the process is running on the background. So we don't see the process and the process is not controlling the
Miquel Àngel Senar Rosell 1 minute 46 seconds
The terminal about the process is running and is managed by the operating system before.
Miquel Àngel Senar Rosell 1 minute 53 seconds
under the scene, let's say. And that's a one way, one simple way of running applications without needing, without the need of opening multiple terminals. So with a single terminal, we can start
Miquel Àngel Senar Rosell 2 minutes 12 seconds
multiple processes and we can use as many cores as possible while we are still typing other comments in the terminal, right? And if we want to control how many processes are in the background or you want to see how many of them are there, you can use the jobs.
Miquel Àngel Senar Rosell 1 hour 15 minutes 35 seconds
into arguments to create the instances of a slip in this case. Okay, the minus T is simply showing explicitly what is going on in the system. If I do something like, let me do something like this, let me put a thing here.
Miquel Àngel Senar Rosell 1 hour 15 minutes 54 seconds
And.
Miquel Àngel Senar Rosell 1 hour 15 minutes 58 seconds
Can hear?
Miquel Àngel Senar Rosell 1 hour 16 minutes 1 second
Remember, regard that we have started two of them.
Miquel Àngel Senar Rosell 1 hour 16 minutes 6 seconds
The first one to complete is going to be the first one. Once this is completed, we will start sleep five. And now we have two cores, five seconds remaining. We have to start the last one when each one of the previous ones is completed. Okay.
Miquel Àngel Senar Rosell 1 hour 16 minutes 25 seconds
So that's the idea of exacts. So it's a common that in our case, it can manage the execution of multiple parallel applications automatically. So the main difference, or one of the main differences compared to the background processes and that sort of stuff, is that
Miquel Àngel Senar Rosell 1 hour 16 minutes 49 seconds
Exacts will create a list of tasks to be done according to the input that we have here, and it will manage and it will be monitoring the application automatically for us, and we'll start as many instances of the process that we specify here automatically for us. So we don't have to.
Miquel Àngel Senar Rosell 1 hour 17 minutes 8 seconds
to where, to worry about how, when we have to start the next instance. So exact will take care of that automatically for us, okay? And then that's basically it. We have, this is another example, and we'll go very fast.
Miquel Àngel Senar Rosell 1 hour 17 minutes 29 seconds
for that and basically the main idea here is that you have this syntax here using this minus i as a mechanism to control where to take these arguments or these elements that are coming from the standard input, where to put these values
Miquel Àngel Senar Rosell 1 hour 17 minutes 49 seconds
in the command that we have to run. So in this particular case, we have to run process and we have files, JPJ files, and the name of the file has to be used according to the values provided here. So this one, two, three, four, five will.
Miquel Àngel Senar Rosell 1 hour 18 minutes 9 seconds
be added here in this position. So the process will have one GPJ, two GPJ, three alto one to four. OK?
Miquel Àngel Senar Rosell 1 hour 18 minutes 19 seconds
And that's exact. Okay.
Miquel Àngel Senar Rosell 1 hour 18 minutes 23 seconds
Now we have an asynchronous version.
Miquel Àngel Senar Rosell 1 hour 18 minutes 26 seconds
It's a kind of an asynchronous version compared to this. We know how to do it using the background processes. Now we can do the same, exactly the same by using exacts. With the advantage, that's something added here, is that we don't have to type it and to control
Miquel Àngel Senar Rosell 1 hour 18 minutes 45 seconds
when one application has finished before we start the next one. Okay. That's basically the main advantage provided by XARCs. And now the last command is exactly, oh, it's something very similar. It's the genuine parallel command. It is more powerful in terms of syntax complexity.
Miquel Àngel Senar Rosell 1 hour 19 minutes 6 seconds
And you can do more nice things if we wanted to run parallel applications following the same idea. It follows a very similar idea compared to the case of Xarcs. Instead of Xarcs, we are using parallel. You take
Miquel Àngel Senar Rosell 1 hour 19 minutes 25 seconds
arguments that are coming from the standard output of a process on those arguments or those that standard output elements are going to be used as arguments for the process that you want to run here.
Miquel Àngel Senar Rosell 1 hour 19 minutes 41 seconds
and you can control how many instances you run in parallel simultaneously. In this example, you have up to three instances of the same process running simultaneously. And then because it has more, it's a more modern common, it has more features in terms of
Miquel Àngel Senar Rosell 1 hour 20 minutes 1 second
You can do more nice examples where you can combine things in a more sophisticated way. The input arguments can be supplied via the command line, so you can do something like this parallel, you want to run this and the arguments instead of coming from the
Miquel Àngel Senar Rosell 1 hour 20 minutes 20 seconds
from a pipe, you can put them here, one, two, three, 456. That will create six instances, and each one will be run using one argument at a time. Arguments can be supplied in a file, so input txt.
Miquel Àngel Senar Rosell 1 hour 20 minutes 40 seconds
can contain these values and the values will be read from the file and will be passed to the process that you want to run. That's exactly another convenient way of doing the same. And then you can do combinations. If you want to combine one, one, two, two,
Miquel Àngel Senar Rosell 1 hour 20 minutes 58 seconds
For instance, if you have something that is regular, you can put the arguments in this way, and the parallel command will generate all the combinations of these parallel sets of arguments. You can do this, or you can do something that more limited, in this case, it's with the
Miquel Àngel Senar Rosell 1 hour 21 minutes 18 seconds
link you are doing only one one two two three three that's another limitation or you can do other ways of you can control where to put the the argument again by using this the syntax where you have you specify where to to do the trans the
Miquel Àngel Senar Rosell 1 hour 21 minutes 37 seconds
A.
Miquel Àngel Senar Rosell 1 hour 21 minutes 39 seconds
the substitution. So one to three will be located or will be put at this particular point. Okay. So basically the idea is the same as before. So if you have understood the idea of Xarcs when I have run it here, parallel provides more or less the same
Miquel Àngel Senar Rosell 1 hour 21 minutes 59 seconds
functionality in the sense that it can control how many applications, how many instances of one specific application we can run simultaneously. We have mechanisms to get arguments and to put the arguments to pass arguments to the application that we want to run.
Miquel Àngel Senar Rosell 1 hour 22 minutes 19 seconds
In the case of exact, everything has to be coming from the standard input. In the case of parallel, things come from the standard input, they can be put at the end of the command, they can come from a file. So you have more flexibility in the case of parallel.
Miquel Àngel Senar Rosell 1 hour 22 minutes 38 seconds
But the rational of those of both comments is more or less the same in terms of I can take elements, I can pass those elements as arguments to a specific application, and I can run multiple instances of that application in parallel.
Miquel Àngel Senar Rosell 1 hour 23 minutes 1 second
according to one parameter that controls how many instances simultaneously I am going to be executing in the system. And then Xarcs or parallel, both of them are going to do, will do the same work at the end, they will control when to start a new application
Miquel Àngel Senar Rosell 1 hour 23 minutes 20 seconds
as long as the previous one has been finished and you have scores available for running them.
Miquel Àngel Senar Rosell 1 hour 23 minutes 31 seconds
O K.
Miquel Àngel Senar Rosell 1 hour 23 minutes 33 seconds
So, and here you have well several examples that are showing you different combinations and how to generate different combinations of common that are more sophisticated. Okay.
Miquel Àngel Senar Rosell 1 hour 23 minutes 47 seconds
No, sure.
Miquel Àngel Senar Rosell 1 hour 23 minutes 50 seconds
Any any questions so far regarding exact row or parallel?
Miquel Àngel Senar Rosell 1 hour 24 minutes
Is it more less clear what this last couple of comments can be?
Miquel Àngel Senar Rosell 1 hour 24 minutes 8 seconds
can can do for when we when you want to run a parallel application or multiple instances of an application.

Iris Mestres Pascual
1 hour 24 minutes 20 seconds1:24:20
Iris Mestres Pascual 1 hour 24 minutes 20 seconds
Yeah, everything is there.
M
Miquel Àngel Senar Rosell
1 hour 24 minutes 21 seconds1:24:21
Miquel Àngel Senar Rosell 1 hour 24 minutes 21 seconds
Okay, so we are going to close the session now. You have a kind of exercise here, and I will try to give it to you on the campus virtual in a more organized way.
Miquel Àngel Senar Rosell 1 hour 24 minutes 40 seconds
I will add some kind of additional information to this exercise for you to practice it. Okay, but basically that's it. So we are going to leave it here today. We have seen all the set of all the comments that can be used to run multiple applications in a single machine.
Miquel Àngel Senar Rosell 1 hour 25 minutes 2 seconds
and the control of the user or and the control of a of a command that takes care of the of the starting and the finishing of the of all the instances.
Miquel Àngel Senar Rosell 1 hour 25 minutes 15 seconds
And then next week, we will start to see how we can run now, not in a single machine, but using multiple machines available in a given infrastructure. So for now, I am going to close now. So let me go back to the
Miquel Àngel Senar Rosell 1 hour 25 minutes 36 seconds
To the present to the to the Teams session, so if you if you don't have any other question, I am going to close the the.
Miquel Àngel Senar Rosell 1 hour 25 minutes 47 seconds
