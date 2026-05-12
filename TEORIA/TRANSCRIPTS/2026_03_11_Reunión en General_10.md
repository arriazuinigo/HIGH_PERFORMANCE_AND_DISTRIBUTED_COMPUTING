Miquel Àngel Senar Rosell
0 minutes 4 seconds0:04
Miquel Àngel Senar Rosell 0 minutes 4 seconds
OK, now recording has started. I'm gonna close my.
Miquel Àngel Senar Rosell 0 minutes 10 seconds
My camera for a while and let's move to the presentation. So yesterday we ended up by taking a look at the parameters that are available in this room.
Miquel Àngel Senar Rosell 0 minutes 26 seconds
That can be used to control how many uh.
Miquel Àngel Senar Rosell 0 minutes 31 seconds
Resources we are requesting to the system and we were discussing a little bit about this idea of what kind of applications can be executed in a in a cluster of machines.
Miquel Àngel Senar Rosell 0 minutes 46 seconds
And what are the strictly the requirements that must be fulfilled to succeed in the execution of those applications? Basically, we ended up with this example. It was at the end of the session and.
Miquel Àngel Senar Rosell 1 minute 6 seconds
We didn't pay too much attention to that, but today let me go into some more details about this example, not because of the programming elements that are already here, but.
Miquel Àngel Senar Rosell 1 minute 22 seconds
Because this example illustrates what can be executed in a cluster and what are the main parameters that you have to fix when you want to to run something using.
Miquel Àngel Senar Rosell 1 minute 39 seconds
More than one basic core. OK, so this example is a hybrid program, which means it's a program prepared to run using multiple processes that will exchange messages to synchronize and to cooperate in the resolution of.
Miquel Àngel Senar Rosell 1 minute 59 seconds
A specific problem, but then each one of those processes can also be subdivided into threads. So in that sense, this application combines a shared memory model which is the model.
Miquel Àngel Senar Rosell 2 minutes 18 seconds
Where all the processes of the threads are running in the same machine using multiple cores of the same machine and using all the memory allocated, all the memory present on that machine. That's a shared memory model and that's what.

Johanna Ursula Albers
42 minutes 17 seconds42:17
Johanna Ursula Albers 42 minutes 17 seconds
Yeah, so put it in the background, right?

Miquel Àngel Senar Rosell
42 minutes 19 seconds42:19
Miquel Àngel Senar Rosell 42 minutes 19 seconds
So the process was started in the background but the the script.
Miquel Àngel Senar Rosell 42 minutes 25 seconds
Complete it immediately. So the script simply put the the process in the background and finished immediately and that that that's the the the mistake, right? So we have to wait until all the processes in the script are completed before we leave the the whole script.
Miquel Àngel Senar Rosell 42 minutes 44 seconds
Now I think that well the application should be completed and now it's number three. So basically what we have here is a single execution. You see here we have executed from one to 700, that's the total number of primes and the script took about
Miquel Àngel Senar Rosell 43 minutes 4 seconds
3 seconds. So basically we have executed one single instance of the application. OK, now if we want to run multiple instances of a given application, we have to do something like this.
Miquel Àngel Senar Rosell 43 minutes 22 seconds
By doing something like this, we will eventually be executing two instances of the of the application. We put one instance in the background and then we start the second instance, and then eventually we we have to add a wait statement.
Miquel Àngel Senar Rosell 43 minutes 42 seconds
at the end. So basically the idea would be, I can do something like this and then eventually I can, obviously doing the same is not that interesting, but I can do something like, okay, I can I can compute from
Miquel Àngel Senar Rosell 43 minutes 57 seconds
This come from one 880,000 sorry and then I have to use this add this weight statement at the end so that I guarantee that both processes are completed before I leave the script.
Miquel Àngel Senar Rosell 44 minutes 14 seconds
The ampersand here is eventually useless if you if you the 2nd ampersand. If you don't want to use it, that's fine. But in this way we have a mechanism to run 2 instances. In principle should be two different instances or two complete different instances of the application.
Miquel Àngel Senar Rosell 44 minutes 32 seconds
And both instances will take advantage of the two cores that are available. OK, so in the.
Miquel Àngel Senar Rosell 44 minutes 43 seconds
Going the same, we are going to run using these two instances. OK, now they will take approximately something similar to 30 seconds, which is which is the time it takes for the second case to be completed.
Miquel Àngel Senar Rosell 44 minutes 59 seconds
And while this is, uh, running OK, click for a while.
Miquel Àngel Senar Rosell 45 minutes 7 seconds
Now let's see another option would be I can do an S run. OK, by using S run the output or the consequence that we will have is now we are going to run 2 instances, so S run.
Miquel Àngel Senar Rosell 45 minutes 22 seconds
will generate 2 instances because we have allocated, we have specified that we we need to to task or we have allocated 2 cores. So everyone takes this value into account and will run as many instances of this command as
Miquel Àngel Senar Rosell 45 minutes 41 seconds
Calls allocated in the in the Loom request. Let me check if the previous has been completed and now let's see the.
Miquel Àngel Senar Rosell 45 minutes 56 seconds
The output of this example.
Miquel Àngel Senar Rosell 46 minutes
So you see here we have been able to run two different instances by using this ampersand mechanism. We have requested two cores. We are running two instances. OK if we do.
Miquel Àngel Senar Rosell 46 minutes 15 seconds
Now we change Greece and we replace this by this as run. As we have already said, we will be running. Well, in that case the the weight is not strictly needed, but we will leave it.
Miquel Àngel Senar Rosell 46 minutes 35 seconds
Here, let me move quickly to this example. I show me this and now.
Miquel Àngel Senar Rosell 46 minutes 44 seconds
What we are having here is we are running. What we will see now at the end is that we will be running 2 instances of the same application. So this means that by using S run I can start applications in all the.
Miquel Àngel Senar Rosell 47 minutes 4 seconds
all the resources that I have been requesting or all the resources that have been allocated to my to my job. And obviously uh doing something like this is not very useful or not very interesting because nobody has too much interest in running the same stuff twice.
Miquel Àngel Senar Rosell 47 minutes 24 seconds
or several times, but what we can do if uh we want is we can allocate many resources and then we can generate a specific S1 commands for each one of the resources allocated so that our application or our submission file might look
Miquel Àngel Senar Rosell 47 minutes 44 seconds
Look like something similar to this one. So I am allocating in this example 2 nodes and I am allocating also two tasks or I am requesting 2 tasks. I say that I will use one core per task. So this means that.
Miquel Àngel Senar Rosell 48 minutes 1 second
Each task will be allocated in principle in each one of the of the nodes, and then we can do something like this. We can run one specific instance of this problem into one specific node in one of the cores of the node and the other specific.
Miquel Àngel Senar Rosell 48 minutes 20 seconds
Instance can be executed in a different node. Obviously here you can, depending on the allocations that you are requesting or the resources that you are requesting, the distribution of these instances can be adapted to your specific case, but the main idea here that I want to highlight.
Miquel Àngel Senar Rosell 48 minutes 39 seconds
Is by using a run we can submit a single job and we can split and we can run independent instances of the same application or different applications in all the resources that are being allocated at once.
Miquel Àngel Senar Rosell 48 minutes 58 seconds
By using the initial options here, we allocate as many resources as we want. In principle, resources can be allocated in different machines or in the same machine, and then by using a run, we can distribute
Miquel Àngel Senar Rosell 49 minutes 16 seconds
All our applications in all the instances that we have been requested.
Miquel Àngel Senar Rosell 49 minutes 24 seconds
Answering one, let me go back to to to to the initial question. The first question when someone of you said that you should put a two here regard that if you put a 2 here.
Miquel Àngel Senar Rosell 49 minutes 40 seconds
This instance will not be executed in, so Loom will not distribute the application in each one of the nodes. OK, so in this if we have this scenario 2 in the number of nodes and one in the number of tasks, only a single instance.
Miquel Àngel Senar Rosell 50 minutes
Will be executed in one of the nodes and the other node will remain idle. And again in the case of S run if we are saying I am requesting 2 nodes but I am.
Miquel Àngel Senar Rosell 50 minutes 15 seconds
Only requesting one task or I am only saying that I will run one task. The F run will only run one instance of the application, so independently of how many nodes we have allocated.
Miquel Àngel Senar Rosell 50 minutes 32 seconds
What is important for from the point of view of the number of instances that will be executed is the number of tasks that we specify in the second in the second common. OK, if we want to use a lot of machines or we want to and we want to distribute the applications in in different ways within the cluster.
Miquel Àngel Senar Rosell 50 minutes 52 seconds
Then it makes sense to request more than one node, and then eventually to distribute the work among nodes in a in an expression similar to this one that you see that you see here. OK.
Miquel Àngel Senar Rosell 51 minutes 4 seconds
OK.
Miquel Àngel Senar Rosell 51 minutes 6 seconds
And now let's check finally the example that we have been running before. So if we take this 75, what you see here is uh in this example what we have been using is dsrun, okay we have
Miquel Àngel Senar Rosell 51 minutes 25 seconds
We have requested two tasks, so what we have obtained it is 2 executions of the same application by means of the SRAN command. So that basically illustrates that SRAN can create as many instances as.
Miquel Àngel Senar Rosell 51 minutes 45 seconds
we want. Obviously creating instances, as we said, of the same stuff is not that useful, but uh so so this is something that is not very uh very useful in practice because you are running the same stuff and you will get exactly the same stuff.
Miquel Àngel Senar Rosell 52 minutes 5 seconds
unless this application is a kind of a random simulator that generates random values and you want to run several times to to get kind of statistics about something. Uh If that's not the case, the the normal way of using as run to control and to
Miquel Àngel Senar Rosell 52 minutes 24 seconds
that multiple instances of different applications or the same application with different parameters would be something similar to the expression that you have here. OK.
Miquel Àngel Senar Rosell 52 minutes 38 seconds
OK, questions because we have already done. We are we have finished now the the topic we have finished, we have conclude with the Saloon and if you don't have any any questions we are going to close the session today.
Miquel Àngel Senar Rosell 52 minutes 56 seconds
Right here. Any question?
Miquel Àngel Senar Rosell 53 minutes 1 second
Regarding.
Miquel Àngel Senar Rosell 53 minutes 4 seconds
The the thing that we have seen about the slurm today.
Miquel Àngel Senar Rosell 53 minutes 17 seconds
No questions.
Miquel Àngel Senar Rosell 53 minutes 27 seconds
OK. I assume that you have no questions and everything is clear. So thank you for attending the session in the in the well next week probably Sandra will be doing the both sessions on.
Miquel Àngel Senar Rosell 53 minutes 45 seconds
Tuesday and Wednesday if we and then probably we will see each other back in two weeks from now. So in any case we will continue with the next topic related to to to this part of executing using middleware.