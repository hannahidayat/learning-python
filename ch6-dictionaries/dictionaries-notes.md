# Chapter 6 - Dictionaries
Why are dictionaries so cool???

## Key concepts
* Learned how to store information in dictionaries
* Gained knowledge of key-value pairs
* How to use *for* loops to read dictionaries 
* Nesting lists in a dictionary
* Nesting dictionaries in a list
* Nesting dictionaries in a dictionary 

## Potholes to avoid and prevent tire damage  
### Defining a dictionary **VS** defining a key-value pair: <br>
When defining the dictionary, I have to make sure to use the **=**  *equal* sign. For key-value pair, I have to use **:** *colon* sign. Easy to mess up when coding fast.

Each key-value pair must have a **,** *comma* to separate them. 

### Looping
When I want to loop through the information in a dictionary, I *must* use the <dictionary_name>**.items()** function in the *for* statement. I keep forgetting the items() and causing error. 

In order to avoid printing the list in its original format, I have to remember to use a *for* loop to print it without any brackets. <br>
If I wanted to be specific on which to print, I write <dictionary_name>.**keys()** or <dictionary_name>.**values()**.

### Dictionaries in a list
Adding dictionaries to empty lists is easy. Just create an empty list and the dictionary, then add dictionary to list by **append()** function.

### Lists in dictionary
While defining a dictionary's key, the values could be a list by using **[]** brackets. Inside the brackets should still have quotations and be separated by commas. 

### Dictionaries in dictionary 
Fascinating and I think easy to get to hang of with practice. I just need to make sure each dictionary has its information defined with **{}** curly brackets and are still separated by a comma after its closing. The rules for key-value pairs are the same. It could get confusing with many/lengthy pairs for each dictionary, but I think that is where consistency and neat coding is important.
