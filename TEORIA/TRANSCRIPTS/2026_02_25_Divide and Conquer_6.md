Sandra Adriana Méndez
0 minutes 3 seconds0:03
Sandra Adriana Méndez 0 minutes 3 seconds
Hey.
Sandra Adriana Méndez 0 minutes 4 seconds
We'll really see a new topic in that part that is the Bayon Conquer approach. This is another technique that we apply in programming. Yeah, so this is our topic in this part of the algorithm. So will we try to start understanding what is the Bayon Conquer, that is no complete concept and see some
Sandra Adriana Méndez 0 minutes 27 seconds
specific algorithm that implemented kind of proposal. Yeah. So here, what is the way in concrete is named that suggesting that the idea, no, the idea is to work in a big problem, dividing this in a small part, and solving this recursively.
Sandra Adriana Méndez 0 minutes 48 seconds
The idea is that, okay, we have a big problem, but we can divide this in a more stack where we can apply directly a solution. And after that, we combine this solution of the problem and obtain the solution for our original cases. Yeah, so this is the idea of divide and conquer.
Sandra Adriana Méndez 1 minute 9 seconds
the idea mainly is to reduce the space of our problem. Yeah, we apply this mainly in a large cases where we have a complex problem. And also, we have several algorithm in computer signs that use this approach and that we can apply in different domain. So this is the reason that
Sandra Adriana Méndez 1 minute 30 seconds
We need to understand what we do when we apply it by Jan Conquer. Possibly in your case, you only call the the algorithm and you don't understand, but it's 2 inferently, but several of the algorithm that is applying computer science, applying this kind of approach, so.
Sandra Adriana Méndez 1 minute 49 seconds
before to start, to see one algorithm that have the whole general view of this kind of approach, will we start reminding a little about the searching algorithm? I think that's after the two season that we have, session that we have in the last week,
Sandra Adriana Méndez 2 minutes 9 seconds
where we see the complexity of the recursion, and we see in both cases comment about the searching. Yeah, in that case, we will try to review again and to understand why we need some kind of algorithm to apply usually. Yeah, so
Sandra Adriana Méndez 2 minutes 28 seconds
In that case, you remember that we have the linear search in that in that case is a case that we're need to iterate over our list and to compare the element to search the to search the value that we want. Yeah, so we have different implementation.
Sandra Adriana Méndez 2 minutes 47 seconds
In that case, we can see here two iterative versions, both of them is doing the same, but one of them is returning is the element is fine or not. In any other case, we are returning the position of the element that we are searching in the case we find. This kind of algorithm is iterative and the complexity is linear.
Sandra Adriana Méndez 41 minutes 18 seconds
This is a binary set.
Sandra Adriana Méndez 41 minutes 21 seconds
Here we are doing a binary search, but we are doing with the camera list. Yeah, so the binary search needs a sorted element. So this binary search needs this in that order. So you can apply it directly to our camera list the sorted algorithm that we saw before.
Sandra Adriana Méndez 41 minutes 42 seconds
and then apply the search that we use with the program, and we can find, we can see how we find the element. So this is the advantage of this kind of algorithm. The Binary Search is useful for different domain and this and the merge sort.
Sandra Adriana Méndez 42 minutes 1 second
is useful because if you need searching and you need an algorithm that have a good complexity, then the most convenient is to apply an algorithm like Binary Search. But Binary Search need a list of sorted elements. So
Sandra Adriana Méndez 42 minutes 19 seconds
This is the reason that we need to apply the other, the last algorithm now. So the idea that this is important that the sorting part. It seems like it's not complex, but it seems that it's a concept that is not important, but it's important because there are several algorithms that need the data in
Sandra Adriana Méndez 42 minutes 42 seconds
Yeah, so you're gonna write this algorithm in your risk and you can obtain the the value. Yeah, so this is the advantage of this algorithm. Also, this is an algorithm that we have tested in several domain, we know the complexity and so.
Sandra Adriana Méndez 43 minutes 2 seconds
We don't need to invent nothing. We only need to use this. Yeah, so.
Sandra Adriana Méndez 43 minutes 12 seconds
Question about this party, I don't know, I don't put more, I think that.
Sandra Adriana Méndez 43 minutes 21 seconds
Question about the merge source, about the concept, really is not a complete concept. We only see here one algorithm. Yeah, so I think that the in the next session we will see, obviously, we always use the we review again some.
Sandra Adriana Méndez 43 minutes 40 seconds
previous algorithm, but because all of them is using the previous. Yeah, so it just up here, we the first concept that we saw was the vinar research, but really the vinar research have some requirement that then we need to see the algorithm that allows to
Sandra Adriana Méndez 44 minutes
have this sorted list that we need for the binary sales. Yeah, so you have some some question here.
Sandra Adriana Méndez 44 minutes 11 seconds
I don't know.
Sandra Adriana Méndez 44 minutes 13 seconds
I think that I was fast because we finish.
Sandra Adriana Méndez 44 minutes 17 seconds
There are some questions if you have some problem with something like there.
JA
Johanna Ursula Albers
44 minutes 27 seconds44:27
Johanna Ursula Albers 44 minutes 27 seconds
I think it's all clear, thank you.
SM
Sandra Adriana Méndez
44 minutes 30 seconds44:30
Sandra Adriana Méndez 44 minutes 30 seconds
Read that.
CK

Celica Krigul
44 minutes 30 seconds44:30
Celica Krigul 44 minutes 30 seconds
They have a question that might be silly, but for numeric values, why can't we just use the sort value that already exists in the source function that exists in Python and then use it inside of the binary search function?
SM
Sandra Adriana Méndez
44 minutes 32 seconds44:32
Sandra Adriana Méndez 44 minutes 32 seconds
Yeah.
Sandra Adriana Méndez 44 minutes 33 seconds
Yeah.
Sandra Adriana Méndez 44 minutes 47 seconds
Yeah, you sorry, you are saying me that we have, okay, you have the function implemented in in Python too. How did the the idea of all of this is to understand what is happened with the function that the Python provides us as library? Yeah, so.
Sandra Adriana Méndez 45 minutes 7 seconds
A buena idea in that part es.
Sandra Adriana Méndez 45 minutes 12 seconds
It's a way to show you that what happened really in in the background, what is really doing in Python. Yeah, as we say that all these algorithms are along that are validated and are implemented. So Python usually provide you some functions that do all the
Sandra Adriana Méndez 45 minutes 33 seconds
all this kind of implementation. Yeah, but the idea of our part is to show you how this is working, really. Possibly, you in your work, you only use some library that you can call the different source function, for example, that Python provide different
Sandra Adriana Méndez 45 minutes 55 seconds
that you can use the master sort and you can use the quick sort, the Google sort on different algorithm that we have in the sorting part.
Sandra Adriana Méndez 46 minutes 3 seconds
But our idea is to show you how it happened in the background. And mainly, if you decide that, for example, say, I don't need to implement this because I am no in computer science, so I don't need to program it. I can use directly.
Sandra Adriana Méndez 46 minutes 22 seconds
The library that provide a Python or some package of is used in by informatics, for example, or in in in in data science.
Sandra Adriana Méndez 46 minutes 32 seconds
But the important thing, I think, is to understand the complexity that is, if you are saying depending on the algorithm. As we comment, the smart source is following at the Bayam Conquer approach and have a complexity that is
Sandra Adriana Méndez 46 minutes 51 seconds
and log the end that is not compared to other algorithm. The complexity is not that, but is not the best.
Sandra Adriana Méndez 47 minutes
But then this allows you to select what is the sort algorithm that you can select offer the library that Python provides. So my idea is not that you learn to program in like a computer science engineer, for example, in that part. No, the idea is to understand.
Sandra Adriana Méndez 47 minutes 21 seconds
the way that's the different library implement the algorithm. Yeah, the complexity that we have there. So all of we can create our version and we can use the version that provide Python. Yeah, so that depends.
Sandra Adriana Méndez 47 minutes 40 seconds
depend off of each of the user. Sometimes we only use the function, but we don't see more about how this is implemented.
Sandra Adriana Méndez 47 minutes 49 seconds
I don't know if this is clear, but I am really pointing to you to your question.
CK

Celica Krigul
47 minutes 57 seconds47:57
Celica Krigul 47 minutes 57 seconds
Yes, thank you.
SM
Sandra Adriana Méndez
48 minutes 1 second48:01
Sandra Adriana Méndez 48 minutes 1 second
Ok, so.
Sandra Adriana Méndez 48 minutes 3 seconds
I understand that more of you could be that I'm not from Computer Science area.
Sandra Adriana Méndez 48 minutes 11 seconds
But my idea mainly is to show you that this different functions. So if you have some problem with this or do you think that we have some functions that are in Python, you can always ask, yeah. So, you say Sandra, we you decided to see the solvent, but always the idea always is to.
Sandra Adriana Méndez 48 minutes 33 seconds
trying to focus in the strategy that we have here now. So what is the importance of this part? We have a way to resolve problems that is the approach that we have with the by and conquer. This is the general idea.
Sandra Adriana Méndez 48 minutes 51 seconds
you can apply this by a conquer in that way, or you can use a function that sort element by using different library. But the important thing is that when you apply this, try to understand what is happened in the background.
Sandra Adriana Méndez 49 minutes 10 seconds
in the real implementation. Yeah, because Python is friendly and provides several functions, but the complexity has the impact in the time. Yeah, sometimes we decided to select one function that provide Python that solve the problem.
Sandra Adriana Méndez 49 minutes 29 seconds
But could be that when we increase the the the size of the problem, we can see that the time of resolution is long. Yeah, but this is because we are not using the best algorithm. So this is the the idea of our part is that give you give you an idea.
Sandra Adriana Méndez 49 minutes 49 seconds
How are the complexity of the different algorithm of the different technique that we have right here, then you can know the technique and you can decide how is the best argument that you can select. This is the idea. It will be that you don't need to implement when you work. You only not select. Yeah, but.
Sandra Adriana Méndez 50 minutes 8 seconds
This is a buena idea, so more cuestión.
Sandra Adriana Méndez 50 minutes 22 seconds
If we don't have more questions.
Sandra Adriana Méndez 50 minutes 26 seconds
Do you see that we put I put two release? Yeah.
Sandra Adriana Méndez 50 minutes 32 seconds
If you have some problem with the complexity or the recursion part, remember, you can send an email or you can, if you need some extra explanation, we can put some meeting to solve the problem. So,
Sandra Adriana Méndez 50 minutes 50 seconds
For this part, I think that will combine the this part with the other with the net topics, yeah? And I will put a release for that part because you have now to release two assignments, so I think it will be a little
Sandra Adriana Méndez 51 minutes 10 seconds
Y.
Sandra Adriana Méndez 51 minutes 12 seconds
It's more worth that. I prefer you finish well the complexity and the recursion part. And after that, I will combine the guide for this part and the next topic. Yeah.
Sandra Adriana Méndez 51 minutes 28 seconds
So if we don't have more question, we can finish here. So we ask again, you have more question about this.
Sandra Adriana Méndez 51 minutes 46 seconds
I think no. Okay. If we don't have my question, then we need, we will have the session the next week. Yeah. And the next week, we need to release all the two guides that we provide. Yeah. So for
Sandra Adriana Méndez 52 minutes 7 seconds
Please don't forget to finish all of that. Yeah, that is important for for your day. Okay, then we can finish now and see you the next week. 