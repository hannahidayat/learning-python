# Chapter 5 - Conditional Statements

* Reviewed how to create *if* statements and conditional tests to check for equality
* Learned how to check if a value is in a list 
* Checked strings with case insensitivity by using the lower() function 
* Learned how to check more than 1 condition by using *and* & *or* 
* Reviewed the *if-elif-else* chain 

## Summary 
I felt comfortable creating conditional tests and checking both strings and numerical values. However, I did have trouble with exercise 5-10 of checking usernames for uniqueness. 

Within the inner *for* loop I did not know how to print the message that a new username was available without the error of looping twice (so it ended up saying all the current usernames are available, then the new usernames were unavailable due to the same strings).

I decided to make a copy of the new username list and remove the usernames that were found to be already taken in current_users (by the *if* test). Then I could print a message for the remaining items to say that these usernames were available, which worked.