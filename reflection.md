# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  
  1) The hints were backwards. For example if the secret is 60 and if I guess 75 it would output "Too High", "📈 Go HIGHER!". Instead it should output "Too High",  "📉 Go LOWER!". The error was on lines 38, 40 and 46,47

  2) It wouldn't allow you to start a new game no matter if you won the previous game or lost.

  It says guess a number between 1-100 for all difficulties.

  The secret is the same across all difficulties which is wrong due to 

  The attempts remaining counter is wrong causing the secret to be revealed with 1 attempt remaing and ends after 1 more attempt.

  

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
ChatGPT and Claude.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). 

I wanted the agent to provide logic for the hint text for each difficulty and the AI didnt initalize the string before the if/else if / else block which caused a NameError. Therefore I initalized the string before the if/else if/else block and then ran the code and I saw no NameError and no new errors

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I would rerun the app and I would check to see if I noticed the same error and I would check to see if there is no other bug caused by the code change.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  
I would like to reuse asking AI to explain code that I don't know so I could understand what each function is doing ad how to fix it without AI.



- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
