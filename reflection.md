# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looked like a normal game until I started guessing then I noticed that the game had so much logic errors. For example if the secret was 30 and I guess 35 it would say "GO HIGHER" instead of "GO LOWER". Also I was not able to play another game so it was like playing a game with an attempt limit.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  
  1) The hints were backwards. For example if the secret is 60 and if I guess 75 it would output "Too High", "📈 Go HIGHER!". Instead it should output "Too High",  "📉 Go LOWER!". The error was on lines 38, 40 and 46,47

  2) It wouldn't allow you to start a new game no matter if you won the previous game or lost.

  3) It says guess a number between 1-100 for all difficulties.

  4) The secret is the same across all difficulties.

  5) The attempts remaining counter is wrong causing the secret to be revealed with 1 attempt remaing and ends after 1 more attempt.

  6) I noticed that you could score negative points which doesn't make sense and if you guess the secret correct on your first attempt you would get 80 instead of 100.

  

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior         | Actual Behavior           | Console Output / Error |
|-------|---------------------------|---------------------------|------------------------|
   75     "Too High",  "📉 Go LOWER!" "Too High", "📈 Go HIGHER!" no error
   -1     "Not in Range"              "Too low," "📉 Go LOWER!"   no error
   35     "Too Low, "📈 Go HIGHER!"    "Too low," "📉 Go LOWER!"  no error

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used ChatGPT and Claude.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I wanted the AI to provide logic for the comparisons of the hint and secret and the AI changed the comparison from a String to an int. This allows the proper outcome and proper return statement to be displayed. I verified it by reruning it and looking to see if I found any new errors caused by the code change.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). 

I wanted the agent to provide logic for the hint text for each difficulty. The AI didnt initalize the string before the if/else if / else block which caused a NameError. Therefore I initalized the string before the if/else if/else block and then ran the code and I saw no NameError and no new errors.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I would rerun the app and I would check to see if I noticed the same error and I would check to see if there is no other bug caused by the code change. I also created pytests designed around that issue. Then I would run it and make sure it said all my tests passed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I ran the test for number of attempts left and when I ran it manually I noticed it wsn't keeping track of my attempts left correctly. The game would end with 1 attempt left when it was supposed to end when there is 0 attempts left or if the user enters the secret.

- Did AI help you design or understand any tests? How?

AI helped me desgin the range for each difficulty because when I first opened the app the rnage was the same for each difficulty which is not how it was intended to be. For easy difficulty the user is supposed to have 6 attempts, in normal the user would have 8 attempts and in hard the user is supposed to have 5 attempts. The attempts are based off the range and the difficulty so that is why easy has less attempt than normal mode. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the entire file from top to bottom whenever a user interacts with a button or the app. Session state is a way of keeping a variable or value across reruns like secret in this apps case. In conclusion rerun is like the refresh button and session state is just a save which stores data tht you want to keep throughout the refreshes or the reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  
I would like to reuse asking AI to explain code that I don't know so I could understand what each function is doing and how to fix it without AI. This will help me improve my proficency in Python as it is not my main coding language. Then I will be able to fix the bugs quicker than I did during this project.



- What is one thing you would do differently next time you work with AI on a coding task?

I think next time I would like to ask my AI assistant where the logic for a certain task is. Therefore, I can try to find th error because my coding language is Java not python. This would allow me to get more familiar and understand it more and maybe even rely on AI less. 

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project made me realize that ene though the AI gives you the right code it doesn't mean that it wouldn't generate new errors in the file. 