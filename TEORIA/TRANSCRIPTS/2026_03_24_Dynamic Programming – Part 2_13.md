Sandra Adriana Méndez
0 minutes 8 seconds0:08
Sandra Adriana Méndez 0 minutes 8 seconds
Okay, okay, perfecto.
Sandra Adriana Méndez 0 minutes 11 seconds
Okay, so this is the last topic of algorithm technique. Today we'll finish with this unit, so the model will be start with other. I think that is less heavy than the next topic. So dynamic programming today, the idea is to finish with this. And if you remember, in the last class, we
Sandra Adriana Méndez 0 minutes 31 seconds
So the concept of a distance to compare to sequence. In our case, we saw the 11 stance algorithm. We implement our solution. That is how the idea is to compute how we can obtain a second stream from the first using.
Sandra Adriana Méndez 0 minutes 51 seconds
the basic operation that is sustitution insertion and emissions. So this is was the main idea. Then as we discussed, this is out an optimization problem. Yeah, well, the idea is to compute the minimum cost for a set of operations. This is the idea. In that case, we have
Sandra Adriana Méndez 1 minute 10 seconds
and an implicit cost that is one for each of the operations that we are doing here to obtain one string from the other. Yeah, so then we implement really in the in the last class we see the the root for implementation that we saw that the complexity is exponential.
Sandra Adriana Méndez 1 minute 31 seconds
So we propose a solution that using dynamic programming, where the idea of dynamic programming needs to reduce the complexity, then from an exponential complexity, we obtain a polynomial complexity. So also dynamic programming have two techniques, one is the memoization and the other is the tabulation, and we so only the memoization that we add a dictionary
Sandra Adriana Méndez 1 minute 56 seconds
where in that dictionary we save the different computation that we are doing when we compute it at distance.
Sandra Adriana Méndez 32 minutes 37 seconds
That, again, contrary that we have here.
Sandra Adriana Méndez 32 minutes 41 seconds
The j is geta than zero, and here we observe that is the position that we are analyzed is equal to the.
Sandra Adriana Méndez 32 minutes 52 seconds
In that case, it's the upper plus one. Yeah, that is this means that we we obtain the minimum from that part. Then this means that is an insertion, then we need to move for the upper for the upper part, then we.
Sandra Adriana Méndez 33 minutes 10 seconds
decrease the J in one. Yeah, so similarly for the deletions, what the deletion anyway we are working with the left part. Yeah, then in that case we need to add a D that is represented the deletion and E is also here and then we decrease
Sandra Adriana Méndez 33 minutes 30 seconds
the way in one, we are moving to the left. Yeah, when we start, when we finish with this, as we are following our table starting for the last position and move to the beginning,
Sandra Adriana Méndez 33 minutes 45 seconds
The SIGAR will be in the reverse or so, we need to apply a reverse to obtain the order from the beginning to the end. Then we'll return, in that case, we are returning the distance. This is the last position, the SIGAR and also our matrix. So in that way,
Sandra Adriana Méndez 34 minutes 5 seconds
you can obtain not only the distance, but also the operation that usually is, it's important to know the different operations that we applied, not only the the the cost of of change one other stream to another, yeah.
Sandra Adriana Méndez 34 minutes 22 seconds
But the way to use this is only to call our distance, and we have the different name that we return. So in that way, we have the similar, we resolve the similar problem that we have with memorization, but using tabulation.
Sandra Adriana Méndez 34 minutes 42 seconds
I think that the balls are similar in complexity could be that it's more difficult the backtracking part to obtain the the the cigar.
Sandra Adriana Méndez 34 minutes 55 seconds
nomenclature because it's more, in the case of the memorization, we only need to add in the same algorithm. Here, we need to add a specific path to obtain the backtracking. So this could be the part that is a little more complex, but the both algorithm.
Sandra Adriana Méndez 35 minutes 15 seconds
Are possible to apply in different cases, that is the important part, yeah? So, and both algorithms have the same complexity, that is a polynomial complexity, that depends on the length of the of the pattern and the text.
Sandra Adriana Méndez 35 minutes 30 seconds
Yeah, so in real cases, when you need to solve this kind of sequence alignment, it could be that the cost is not one like it would solve in that case. You observe in our case, we also add one for insertion, for division, or for match and sustitution.
Sandra Adriana Méndez 35 minutes 53 seconds
But there are cases like the networks to you can change this behavior and adding other kinds of.
Sandra Adriana Méndez 36 minutes 2 seconds
For example, here, instead, the complete with the minimum that we do, the we can complete with the maximum, and if you observe here, the weight of the operation is different. In that case, the insertion is has a negative operation.
Sandra Adriana Méndez 36 minutes 21 seconds
a penalty and the deletion have a negative penalty. So this means that you can't really only adapt this, this algorithm. Yeah, you only need to replace this value that we put here when we add one, we add one here and here, depending on your cases.
Sandra Adriana Méndez 36 minutes 41 seconds
Yeah, so here, for example, the insertion instead to add one, you need to decrease in minus four, and similar for the deletion. And here, for example, when you have a match on the institution, but that depend of unspecific
Sandra Adriana Méndez 37 minutes
the table that you can obtain for your real application, for real cases. Yeah. So the only change that you need to do to this algorithm is only change the last part. Yeah. And also, in that case, you are taking a minimum, if your rule say you need the max, so you only need to change.
Sandra Adriana Méndez 37 minutes 20 seconds
this. So the idea is that the older algorithm that is put here will be worth for your case. You only need to change the basic cases that is you want minimum or maximum. Then you change here the minimum or the maximum. And if your cause for the different operation is different, you only need to change this cause.
Sandra Adriana Méndez 37 minutes 44 seconds
But all the all the all the path is the same. Yeah. So this is the idea that you see this kind of problem that we can apply to different domain. Yeah. So the idea for the last part of this
Sandra Adriana Méndez 38 minutes 3 seconds
Three topics of the algorithm technique is to implement this kind of algorithm by changing the weight for the different operations. Yeah. So this is the assignment that will be the last assignment for this unit that I will put through I see tomorrow, so you can see and
Sandra Adriana Méndez 38 minutes 25 seconds
But the idea is to change only that part. Yeah, this means you need to implement something like this by using memorization or tabulation, but instead of using our rules, you need to use your your weight. Yeah, this is the idea.
Sandra Adriana Méndez 38 minutes 45 seconds
But, we put the assignment and then we explain what we want about this. Yeah. So, the important part of the dynamic programming, I think that is really the main programming is that in your area is more common than is appliance several.
Sandra Adriana Méndez 39 minutes 5 seconds
and several domains that you need. Yeah, so it's important to know the different with dynamic programming. And there are two things that it's important that remember that the memorization, when you when you decided to use this, you are working with recursion and when a catch that is the dictionary that we create.
Sandra Adriana Méndez 39 minutes 27 seconds
And the other solution is working with a tabulation that is a solution that is a bottom up solution. In that case, we are working with the iterative problem. Yeah, and we are working complete in a table, starting always with the smaller cases and complete all the problem. Remember also that.
Sandra Adriana Méndez 39 minutes 47 seconds
that we saw all the brute force solution that has a exponential complexity and the idea of dynamic programming that we can't reduce that complexity. Yeah, so.
Sandra Adriana Méndez 40 minutes
With this, I think that we have all the algorithm techniques done. So the last assignment where we apply the brute force and the dynamic programming for an specific case for the domain of sequence alignment. Yeah, so this will be the last assignment for this part.
Sandra Adriana Méndez 40 minutes 21 seconds
Son cuestión.
Sandra Adriana Méndez 40 minutes 30 seconds
Nice.
Sandra Adriana Méndez 40 minutes 32 seconds
Are you there?
LT
Ludovic Méan Touroyan
40 minutes 35 seconds40:35
Ludovic Méan Touroyan 40 minutes 35 seconds
Yes.
SM
Sandra Adriana Méndez
40 minutes 38 seconds40:38
Sandra Adriana Méndez 40 minutes 38 seconds
Okay, I think that some of you have some question about the different topics.
Sandra Adriana Méndez 40 minutes 49 seconds
Could be this part is a little more hard to follow, because we have several algorithms. But the main idea, guys, is that you understand when you need to apply your carcelon or when you need. I think the most important also is to know the complexity, to know that the complexity is very important when we are selecting a solution.
Sandra Adriana Méndez 41 minutes 11 seconds
Yeah, could be that you, if you are using Python, possibly you use the library to solve the problems. This means that you don't need to implement, but it's important to know what is the implementation that the Python is using to to to decide what is the solution that we need to select. Remember, the complexity is important, yeah.
Sandra Adriana Méndez 41 minutes 31 seconds
So it could be that you select the complexity depending on the kind of technique that we are using. The dynamic programming is better that use a combinator search, for example. So this is for me, for this part important for me is that you understand the concept of complexity, you understand the concept of recaution.
Sandra Adriana Méndez 41 minutes 50 seconds
understand that the exponential is not a good solution. We try to reduce the complexity of using technique like dynamic programming. Then when that idea for me, okay, I can say, okay, the guys study, understand and can apply the problem.
Sandra Adriana Méndez 42 minutes 10 seconds
Ya, so this is the idea, so.
Sandra Adriana Méndez 42 minutes 13 seconds
So you don't have questions, we can finish here. If you have some questions after that, tomorrow will we start with other units that is the management for workflow.
Sandra Adriana Méndez 42 minutes 27 seconds
So, for tomorrow, we will work with studies, no programming like this. It's more, it's more scripting, so it's not that, but I think that is not that difficult to understand. So, final part, more some questions, nothing.