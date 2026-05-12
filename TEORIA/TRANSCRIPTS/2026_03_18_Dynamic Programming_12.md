Sandra Adriana Méndez
0 minutes 3 seconds0:03
Sandra Adriana Méndez 0 minutes 3 seconds
So if you I will try to read the chat, if you just have some question. Okay, today will we start with the dynamic programming. This is a new topic in the algorithm techniques. And this is the last topic. Yeah.
Sandra Adriana Méndez 0 minutes 18 seconds
But this is the last topic, but I divide this into part.
Sandra Adriana Méndez 0 minutes 23 seconds
Yeah, one is for an introduction to understand what is dynamic programming and the next in the next session, we will see the final part of dynamic programming. And after that, we propose a final work with the three-pass topic related with this.
Sandra Adriana Méndez 0 minutes 44 seconds
Part of the.
Sandra Adriana Méndez 0 minutes 47 seconds
of the subject. Yeah. So before we start with dynamic programming as a concept, we remind the concept of the recursion, but for an specific example that was Fibonacci, we saw this even when we see the recursion concept.
Sandra Adriana Méndez 1 minute 5 seconds
But the idea is to understand why we use dynamic programming, and then we use this as example. As you remember that if you want to sequences, we have two field element in our sequence that is zero and one. And after that, each element in the sequence is computed as the sum of the two previous value.
Sandra Adriana Méndez 1 minute 24 seconds
Then we have a sequence of elements that follow the fibonety sequence. Yeah, so the seconds look like this. So when we solve this problem by using recaution.
Sandra Adriana Méndez 1 minute 38 seconds
This was a solution that we proposed when we have the base case and the recursive case, where we put the value and we have in zero or one. And after that, we use a recursion part that we call to part, one is for the previous one and the other for the previous.
Sandra Adriana Méndez 1 minute 57 seconds
to. Yeah, so that was our solution that we proposed when we see the recursion part. We need to remember how this work. This is a call of, it's a tree of calls that we do to solve the problem. Yeah, when we
Sandra Adriana Méndez 2 minutes 16 seconds
when we call the FIBO for the number five, this called for one part for four and this start a three of calls. Yeah. So this called is for three and the three called two and two called for one. Yeah. One is one, this means that we have the finalization of the recursion for that.
Sandra Adriana Méndez 29 minutes 39 seconds
The the value, yeah, so we have to part one one part what we need to see is we have this call with what's done is what's solved, then we don't need to do all the regular algorithm. Yeah, in other case, we'll need to do the regular algorithm and store the results.
Sandra Adriana Méndez 30 minutes
Yeah.
Sandra Adriana Méndez 30 minutes 2 seconds
So we are using here similar to we use for the few cases, but in that case, this is a little more complex cases, no? But the solution is similar. Yeah, so how we can solve this?
Sandra Adriana Méndez 30 minutes 19 seconds
It's also here. Here we have the path where we see this is our data structure. This is the data structure that is saving the solution of my recursive calls. Yeah, here the key is to define the key of
Sandra Adriana Méndez 30 minutes 38 seconds
Our data structure, yeah, so in that way it's more easy to find.
Sandra Adriana Méndez 30 minutes 46 seconds
the combination and to return the value. Yeah, so this is the idea. So here, if you observe, we use a key for our dictionary, the pattern, and the text. That with the combination, too. This is
Sandra Adriana Méndez 31 minutes 5 seconds
We are creating a composer key there. Yeah, because if you see in the recursive part, we are sending the pattern and the text, but we are sending like a substring. Yeah, then we are moving in the pattern or we are moving in the text.
Sandra Adriana Méndez 31 minutes 25 seconds
Then we are we are sending in my recursive function a combination of this pattern and text. Yeah, so in how we can detect that that code was stored. This is a way to detect if we if we have.
Sandra Adriana Méndez 31 minutes 44 seconds
the value of the minimum cost for a combination, a string and the other string, this means we compute that part. So we don't need to call again this combination of pattern and text. So this is the reason we define key.
Sandra Adriana Méndez 32 minutes 3 seconds
as this combination. So if this key is in my data structure, then I don't need to call the regular algorithm. I only need to return the call in that key. So then I can use the minimum close. So
Sandra Adriana Méndez 32 minutes 22 seconds
It's a way that we review the value is there or not. So here the key is to define this part. And the other part is like a regular algorithm. It's our regular algorithm. Similarly that we follow the part of the fibonacci.
Sandra Adriana Méndez 32 minutes 42 seconds
So we run all the normal path and then we need to store the value. Remember that this is the way that we are saving the data in my data structure. Then the next time we need to recompute this, we only do depart that if the value is there or not. So here.
Sandra Adriana Méndez 33 minutes 2 seconds
We call normally our function, and here we put in the key that minimum cost.
Sandra Adriana Méndez 33 minutes 10 seconds
Yeah, so this means that the next time when we have this combination of value, as we say this value here, then we take this minimum value, so we don't need to call again all that function. Yeah, and then we return the minimum value. So just here, we have two main parts.
Sandra Adriana Méndez 33 minutes 30 seconds
That is one is related with the control.
Sandra Adriana Méndez 33 minutes 34 seconds
That if my result is there or not, and the other that is very important is to save the result. So we can use this after when we have the same combination of pattern and text.
Sandra Adriana Méndez 33 minutes 50 seconds
So, this is...
Sandra Adriana Méndez 33 minutes 52 seconds
The part that we have here, remember, always to store at the end, yeah, and always to check at the beginning. Yeah, so this is the idea of we are with our bright memorization and we have our solution that is a reconsive version.
Sandra Adriana Méndez 34 minutes 11 seconds
then we can do this without problems. So if we request, for example, for the final assignment, applied memorization, but instead to do it for an according where the cost
Sandra Adriana Méndez 34 minutes 30 seconds
of each operation is different. This means that it's not one is have different ways. For example, the match the cost is one and the insertion the cost is four and the deletion the cost is six. You only need to see this algorithm and need to change some.
Sandra Adriana Méndez 34 minutes 51 seconds
sync in your edit distance product and propose a solution. The only difference is that you change the code both observe. All this is similar. Yeah. So the way that we use our distance is we need to have our code.
Sandra Adriana Méndez 35 minutes 11 seconds
It's our data structure and we only call the with the with the pattern and the text and the data structure and we obtain.
Sandra Adriana Méndez 35 minutes 22 seconds
our distance by using memorization. Yeah, so each observe is not a complex solution, and with this, we reduce the complexity. So with this solution, we obtain this complexity. Yeah, that is a polynomial complexity.
Sandra Adriana Méndez 35 minutes 42 seconds
that depend of the length of the of the pattern and the length of the text. So this is the idea to apply dynamic programming. Yeah, so.
Sandra Adriana Méndez 35 minutes 54 seconds
Some questions here.
Sandra Adriana Méndez 35 minutes 56 seconds
I do is in that.
Sandra Adriana Méndez 35 minutes 58 seconds
It was fuss.
Sandra Adriana Méndez 36 minutes 4 seconds
It's clear if we don't have more questions. I think I was fast.
Sandra Adriana Méndez 36 minutes 13 seconds
Yeah, because then the idea to use dynamic programming in the next in the next part is to move. This is only memorization that is not difficult, but for this case is a little more complicated to apply the part of tabulation.
Sandra Adriana Méndez 36 minutes 31 seconds
Yeah, so I prefer to leave the tabulation for the next session because we have several things to see there. I prefer that more focus in this as that is single that we have the technique that is no difficult. So question to this.
Sandra Adriana Méndez 36 minutes 55 seconds
Do you have son cuestion.
Sandra Adriana Méndez 36 minutes 58 seconds
Because if we don't have more questions, we can finish here. But the idea is you have clear what is the idea. Remember that the assignment will be related with this part. Yeah, so the assignment is we will request a similar algorithm, but changing some criteria. So I need.
Sandra Adriana Méndez 37 minutes 16 seconds
You understand this, yeah?
Sandra Adriana Méndez 37 minutes 22 seconds
Será eso en cuestión.

Miriam Cegarra Cuquerella
37 minutes 26 seconds37:26
Miriam Cegarra Cuquerella 37 minutes 26 seconds
Everything clear.
SM
Sandra Adriana Méndez
37 minutes 27 seconds37:27
Sandra Adriana Méndez 37 minutes 27 seconds
Is so clear or you don't understand nothing?

Miriam Cegarra Cuquerella
37 minutes 35 seconds37:35
Miriam Cegarra Cuquerella 37 minutes 35 seconds
For me is clear.
SM
Sandra Adriana Méndez
37 minutes 36 seconds37:36
Sandra Adriana Méndez 37 minutes 36 seconds
I don't know if you put some questions in the chat.
Sandra Adriana Méndez 37 minutes 46 seconds
There is no more question.
Sandra Adriana Méndez 37 minutes 53 seconds
OK, here I think that's on chat here.
Sandra Adriana Méndez 38 minutes 3 seconds
No, I can hear you. I don't know why, but I can hear you, yeah.
Sandra Adriana Méndez 38 minutes 12 seconds
Okay, so there are some of you that write me by chat, Johanna, and say me that is clear that what is the idea of this? I suggest to test all this algorithm because
Sandra Adriana Méndez 38 minutes 31 seconds
We usually have problems when we request the assignment, because I usually request only a change in this kind of algorithm, but if you don't understand, it's more difficult to change. Yeah, so this is the idea that you can ask. But anyway, the idea is that review this.
Sandra Adriana Méndez 38 minutes 52 seconds
and try to understand this and test the different algorithm. I will try to upload the Jupiter Notebook so you can play a little with the different algorithm that will put here and mainly try to test the timing of the different solution, the solution by using.
Sandra Adriana Méndez 39 minutes 11 seconds
Combinatoral selt that is.
Sandra Adriana Méndez 39 minutes 15 seconds
This case, yeah, remember, this is the combinatorial search solution. So, and we provide in the Jupiter Novel, so you can test for different pattern and take and measure the timings, so compared with the solution by using memorization. Yeah.
Sandra Adriana Méndez 39 minutes 34 seconds
So the idea is to review this. So the net week, when we start with the tabulation part that is a little more complicated usually, we also request that in the segment.
Sandra Adriana Méndez 39 minutes 46 seconds
So you can have clear the idea and then we can start with this. Yeah. So if you don't have more questions, we can stop here.
Sandra Adriana Méndez 39 minutes 57 seconds
Please try to play with this a little, run the example, run this program, and evaluate the timing. Yeah. So I don't see more question in the chat. So if you don't have more questions, I will stop.