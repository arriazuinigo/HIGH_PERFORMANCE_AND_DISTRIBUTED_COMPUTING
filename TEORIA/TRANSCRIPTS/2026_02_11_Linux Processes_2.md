Miquel Àngel Senar Rosell
0 minutes 3 seconds0:03
Miquel Àngel Senar Rosell 0 minutes 3 seconds
Linux processes OK and.
Miquel Àngel Senar Rosell 0 minutes 12 seconds
Continuing somehow that the the some ideas that we presented yesterday because as we said yesterday, modern computers have are built.
Miquel Àngel Senar Rosell 0 minutes 28 seconds
On top of processors that have multi core that are multi core processors or they are multi core devices, which means that each processor has the capacity of running multiple applications at the same time.
Miquel Àngel Senar Rosell 0 minutes 46 seconds
And that brings us the opportunity to run things in parallel. And then that's the idea. Or if we take this feature as uh as an idea, we can think about the computer as a machine that can run
Miquel Àngel Senar Rosell 1 minute 5 seconds
Parallel applications.
Miquel Àngel Senar Rosell 1 minute 10 seconds
For solving our problem. So and and that is what we will refer probably as parallel computing. So this idea of running multiple things at the same time. OK, and then there are many examples of things that are.
Miquel Àngel Senar Rosell 1 minute 28 seconds
problems that can fit very nicely in this idea of parallel computation because there are problems that can be divided or subdivided nicely in PCs and each one of these pieces can be computed independently of
Miquel Àngel Senar Rosell 1 minute 47 seconds
The other and then we can take advantage of our computing resources through increase to reduce the total execution time of our computations. OK, and that's the idea behind this concept of parallel computing.
Miquel Àngel Senar Rosell 2 minutes 3 seconds
Obviously we can write a specific program that is broken internally into different parts, and that would be probably more close to computing science degrees.
Miquel Àngel Senar Rosell 2 minutes 19 seconds
That's something that computer scientists, engineers can can do, or they learn how to do it. In our case, we are not going to uh to follow that approach in general. We will mostly
Miquel Àngel Senar Rosell 49 minutes 55 seconds
processes are appearing there. They have an ID. This number is an ID that identifies in a unique way each one of these programs in execution. And here we get some kind of information about what's the time that has been expended by the processes uh right up to
Miquel Àngel Senar Rosell 50 minutes 15 seconds
to this moment. So six seconds in one case, three seconds in the other case. And this is exactly the command that we have issued to the system. Now, once we have this scenario regarded by using this ampersand mechanism and by using this mechanism to put a process in the background, what
Miquel Àngel Senar Rosell 50 minutes 34 seconds
We have is that one process eventually running in one core, another process running in the second core, and that's a way of achieving parallelism. So we don't have to wait until the completion of the first application to start the second one by using this ampersand mechanism that
Miquel Àngel Senar Rosell 50 minutes 54 seconds
put a process in execution without direct connection to the terminal, we can have multiple processes running before, uh I mean, in the background. Actually, I don't have any other word to to say that. So you put the process in execution
Miquel Àngel Senar Rosell 51 minutes 14 seconds
but you have the terminal free for you to type new commands, but the operating system will take care and knows about the execution of the processes that you have started before and you have sent it to this background scenario. And then obviously because you don't have the control of
Miquel Àngel Senar Rosell 51 minutes 33 seconds
Of the terminal, but however you can have you can have a mechanism if you want to kill those processes. For instance with the kill command you can say kill stop or you can kill continue and you can control whether a process from those.
Miquel Àngel Senar Rosell 51 minutes 50 seconds
Those two that we have seen before, I can stop it. That means I can put in in pause that process for a while and then I can continue say OK, you can you can go on again and that's a mechanism that provides the operating system to stop to pass to do.
Miquel Àngel Senar Rosell 52 minutes 10 seconds
a partial stop or to pause a process for a while or to continue, or I can really kill. If I put a kill -9, then I will kill it and I will stop completely the execution. But that mechanism, this uh mechanism of the ampersand is one
Miquel Àngel Senar Rosell 52 minutes 30 seconds
That can be very easily used to exploit the.
Miquel Àngel Senar Rosell 52 minutes 39 seconds
the potential resources, the potential course that I have in a in a system. You see here the example of kill minus kill that will remove completely, that will abort the execution of the application at the time or at the point where that application has reached. And then when you type again PS, you see that that process
Miquel Àngel Senar Rosell 52 minutes 59 seconds
2229 has disappeared from the the list of running processes in the system, while the previous one has accumulated 9 minutes and 50 and 50 seconds. OK then. Uh
Miquel Àngel Senar Rosell 53 minutes 15 seconds
And that's the idea that you have been mentioning. OK, we can put processes in the foreground that are running in a synchronous way. Synchronous in the terms of I have the process synchronized with my terminal, so I can type things or the output of the process will appear in my terminal or I can run applications or processes in a.
Miquel Àngel Senar Rosell 53 minutes 35 seconds
In an asynchronous way by putting them in the background. OK, and that's the the idea of foreground, background connected to the terminal or without connection with a direct connection to the terminal and then.
Miquel Àngel Senar Rosell 53 minutes 50 seconds
Um.
Miquel Àngel Senar Rosell 53 minutes 52 seconds
We have eventually what this is an example of where we can use the sleep for doing this background, background processes, background, foreground mechanism. We have one way that again.
Miquel Àngel Senar Rosell 54 minutes 7 seconds
Follow the same example as before, counting primes for for several and putting them in the background and then you see that all of them are running and they are using each one of them is using nearly a whole core in the system. So we are exploiting 3 cores from the system simultaneously.
Miquel Àngel Senar Rosell 54 minutes 27 seconds
And then if you want to control how job, what jobs are in the foreground, in the background, you have the jobs command and eventually you have this foreground background command that can move processes from the background to the foreground and back to the background and so on.
Miquel Àngel Senar Rosell 54 minutes 47 seconds
So forth, frankly speaking, this.
Miquel Àngel Senar Rosell 54 minutes 52 seconds
Game of moving processes from the background to the foreground and back again to the foreground and to the to the background. Sorry is not really very useful, or at least in my experience you usually put a process in the background.
Miquel Àngel Senar Rosell 55 minutes 7 seconds
And you leave it there to run until it completes. While you have control, you keep the control with the terminal and then you can start new things or you can run additional things. But in any case, if you want to play around with this background, foreground and also with the jobs to see what are the processes in the background and.
Miquel Àngel Senar Rosell 55 minutes 27 seconds
How can you control them to to bring in them to the foreground or to the background? Just I leave you here this information so you can play around with them. OK and.

Michael George Nabih Lotfy Eskander
55 minutes 39 seconds55:39
Michael George Nabih Lotfy Eskander 55 minutes 39 seconds
When the process in the background, how to see the results or how do you know when it's finished?
M
Miquel Àngel Senar Rosell
55 minutes 44 seconds55:44
Miquel Àngel Senar Rosell 55 minutes 44 seconds
Well, the results will appear on the screen from time to time if the program is running some kind of input output operation. But you will see messages appearing on the screen at a time where the message is generated by the program, but without any order.
Miquel Àngel Senar Rosell 56 minutes 4 seconds
Maybe.
Miquel Àngel Senar Rosell 56 minutes 4 seconds
You are typing a comment and in the middle of typing something appears on the screen and your typing is broken into two lines because the output of the process has appeared on the screen. So there is no control on that output. Basically it will appear on the terminal as soon as it is produced, but without.
Miquel Àngel Senar Rosell 56 minutes 24 seconds
No control or no no specific order or any specific formatting at the at the screen.

Michael George Nabih Lotfy Eskander
56 minutes 34 seconds56:34
Michael George Nabih Lotfy Eskander 56 minutes 34 seconds
OK. Thank you.
M
Miquel Àngel Senar Rosell
56 minutes 36 seconds56:36
Miquel Àngel Senar Rosell 56 minutes 36 seconds
OK, I'm afraid that I have to close today the session now because I have a problem with another lecture at the same time. So what I want you to to do and I will.
Miquel Àngel Senar Rosell 56 minutes 53 seconds
I am going to publish uh this count count program that you see here. This count primes, I will later on, I will publish this count primes program on the on the Moodle website.
Miquel Àngel Senar Rosell 57 minutes 11 seconds
I just leave you a small exercise, which is, first of all, I think that most of you have already been successful in connecting to the to the cluster. So I I will like you to try out these count primes and see using a small value. These count primes is a program that counts how many
Miquel Àngel Senar Rosell 57 minutes 31 seconds
Primes are in a given interval of numbers and I want you to try this program out using this ampersand mechanism and using this foreground, background and practicing also these these commands that can be used to kill or to control processes.
Miquel Àngel Senar Rosell 57 minutes 51 seconds
running on the on the system. Because this is our first approach for how we can take advantage, how we can use the resources available in a system, how we can use, how we can run parallel applications on a specific system. Uh
Miquel Àngel Senar Rosell 58 minutes 11 seconds
Later on I will publish a very small exercise to guide your your test and I will publish also these count primes. So let's say as a informal homework for you to do during the next weeks or during the next days.
Miquel Àngel Senar Rosell 58 minutes 30 seconds
I will just give you or leave you this exercise to start practicing this uh Linux commands and Linux execution of of parallel applications. Okay?
Miquel Àngel Senar Rosell 58 minutes 48 seconds
So if you have no other questions related to what you have seen up to now, it's about these processes, foreground, background processes. I will close the the session now.

Michael George Nabih Lotfy Eskander
58 minutes 49 seconds58:49
Michael George Nabih Lotfy Eskander 58 minutes 49 seconds
OK.
M
Miquel Àngel Senar Rosell
59 minutes 4 seconds59:04
Miquel Àngel Senar Rosell 59 minutes 4 seconds
And as I told you, I am going to publish this small exercise for you to practice in the next days. And please check that you can enter into the system, that you can run this Python program, for instance, in the system without any problem, and also please try to move the files.
Miquel Àngel Senar Rosell 59 minutes 23 seconds
to copy files back and forth from your home machine to this, to our cluster, so that you can also learn how to move files from the inside to the outside and vice versa. Okay?