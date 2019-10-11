#### Polya's Problem solving techniques
- be able to break down larger and more complex problems

### Steps
1. `Understand the problem fully`
2. Devise a plan ex. what's your approach?  What technologies are you using? What's your timeline?
3. Start implementing with code
4. Reflect on how you can make that solution better


Example.  Plan a Wedding

1. Understand the problem
    - Ask questions
        Where will it be?
        What is the budget?
        When will it happen?

2. Devise a plan
    - Break up the problem
        Prep hair/wardrobe
        Ceremony
        Reception
        after-party

3. Implement
    - Follow the plan
        - order hairdressers and clothes
        - book venues

4. Reflect
    - make changes to make original plan more efficient
        Find cheaper venues
        better food, etc.




#### Example Python Project

When creating more complex projects: 
    1. outline what you're trying to do 
    2. break larger tasks down into manageable tasks
    3. try not to get overwhelmed by the scope of the entire project, one thing at a time


### Making Rock Paper Scissors
    - 2 players
    - 3 possible choices
    - compare choices, results are win, lose, or tie

Thinking about this sequentially 

Start: 
    - display a welcome message, instructions, etc
    - in this case, we're going to load a historical data
    - prompt user to choose: rock, paper, scissors, or quit game
    - this => if they don't quit the game, compare their choice with computer choice
    - or this => if user input is invalid, try again
    - result of either of these leads them back to playing again

Code: 

wins = 0
ties = 0
losses = 0
print("welcome to Rock, Paper, Scissors!")
print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")

#gameplay loop
while not user == 9
#user