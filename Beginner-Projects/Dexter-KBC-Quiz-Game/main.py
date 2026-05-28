# Create a Program capable of displaying questions to the User like KBC
# Use List Data Type to store questions and there correct answers
# Display the Final Amount the person is taking Home after playing the game

# Questions
q1 = '''Dexter’s position at Miami Metro places him primarily in which department?

A) Major Crimes
B) Forensic Services
C) Homicide Division
D) Internal Affairs'''

q2 = '''When relocating in New Blood, Dexter chooses a profession that allows him to:

A) Access police intelligence
B) Stay armed without suspicion
C) Blend into rural community life
D) Track criminal records discreetly'''

q3 = '''Harry’s “Code” was primarily designed to:

A) Protect Miami from serial killers
B) Control Dexter’s urges while minimizing collateral damage
C) Help law enforcement solve cases
D) Channel Dexter toward federal investigations'''

q4 = '''Dexter’s trophy collection represents:

A) Evidence control
B) Psychological closure
C) Ritualistic symbolism
D) A reminder of dominance '''

q5 = '''Debra’s promotion to Lieutenant primarily alters:

A) Her romantic relationships
B) Her access to classified evidence
C) Her moral perspective on justice
D) Her professional dynamic with Dexter'''

q6 = '''The Bay Harbor Butcher investigation collapses mainly because:

A) Physical evidence is destroyed
B) Political pressure interferes
C) The primary suspect dies
D) Federal jurisdiction overrides it'''

q7 = '''Arthur Mitchell maintains his double life by anchoring himself in:

A) Community service and church leadership
B) Political activism
C) Financial consulting
D) Neighborhood watch involvement'''

q8 = '''In New Blood, suspicion toward Dexter resurfaces largely due to:

A) Ballistics inconsistencies
B) DNA re-evaluation
C) Injection mark similarities
D) Witness testimony'''

q9 = '''Miguel Prado’s alliance with Dexter ultimately fails because:

A) Miguel fears exposure
B) Miguel violates the Code
C) Dexter grows emotionally attached
D) Law enforcement intervenes'''

q10 = '''Harrison’s behavioral instability is most influenced by:

A) Abandonment trauma
B) Genetic predisposition
C) Peer rejection
D) Foster system abuse'''

q11 = '''The Ice Truck Killer’s motive toward Dexter was rooted in:

A) Revenge against Harry
B) Professional rivalry
C) Desire for fraternal reunion
D) Financial coercion'''

q12 = '''Debra’s psychological unraveling after Season 7 stems primarily from:

A) Romantic betrayal
B) PTSD from field work
C) Killing an innocent man
D) Killing to protect Dexter '''

q13 = '''Kurt Caldwell preserves his victims in a specific state because:

A) He views them as trophies
B) He recreates unresolved trauma
C) He fears decomposition evidence
D) He intends public display'''

q14 = '''In Original Sin, Harry’s mentorship reflects:

A) Calculated manipulation
B) Desperation masked as guidance
C) Professional obligation
D) Government directive '''

q15 = '''Dexter’s decision to fake his death originally was motivated most by:

A) Avoiding arrest
B) Protecting Hannah
C) Self-imposed exile to prevent harm
D) Financial escape'''

q16 = '''Sergeant Doakes’ suspicion of Dexter is driven mainly by:

A) Inconsistent alibis
B) Personal rivalry
C) Behavioral intuition
D) Forensic contradiction '''

q17 = '''Angela Bishop connects Dexter to Miami cases because of:

A) Batista’s confession
B) Archived FBI files
C) Independent investigative persistence
D) Federal task force alerts'''

q18 = '''The most significant moral fracture in Harry’s Code appears when:

A) Innocents become collateral damage
B) Emotional attachment clouds judgment
C) Dexter kills outside Miami
D) Law enforcement becomes targetable '''

q19 = '''Harrison’s final decision represents:

A) Acceptance of the Code
B) Rejection of Dexter’s philosophy
C) Continuation of vigilante justice
D) Strategic self-preservation '''

q20 = '''Across the franchise, Dexter’s core internal conflict can best be summarized as:

A) Justice vs legality
B) Nature vs nurture
C) Isolation vs connection
D) Power vs control '''

q21 = '''Across every iteration of the series, which event most definitively disproves Harry’s belief that the Code could permanently prevent innocent casualties?

A) Rita’s death
B) LaGuerta’s death
C) Logan’s death
D) Debra’s death '''

# Answers

a1 = 'B'
a2 = 'C'
a3 = 'B'
a4 = 'B'
a5 = 'D'
a6 = 'C'
a7 = 'A'
a8 = 'C'
a9 = 'B'
a10 = 'A'
a11 = 'C'
a12 = 'D'
a13 = 'B'
a14 = 'B'
a15 = 'C'
a16 = 'C'
a17 = 'C'
a18 = 'A'
a19 = 'B'
a20 = 'C'
a21 = 'C'

# Lists of Questions and Answers 
question = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21]
answer = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21]

# Stages of questions :
# Stage 1 : [0 - 4]
# Stage 2 : [5 - 9]
# Stage 3 : [10 - 14]
# Stage 4 : [15 - 19]
# Golden Stage : [20]

# Prize Money
# Stage 1 = 100$
# Stage 2 = 500$
# Stage 3 = 1000$
# Stage 4 = 5000$
# Golden Stage = 10000$

prize = 0
count = 0 # No. of correct answers

# Intro

Title = "Welcome to the Game of DWYM : Dexter Wins You Money"
print(Title.center(100))

intro = '''It's Really Simple !!!
Answer the following questions correctly and You'll win Money
This game has 5 different stages :
Stage 1 :- 5 Questions and each wins you 100$
Stage 2 :- 5 Questions and each wins you 500$
Stage 3 :- 5 Questions and each wins you 1000$
Stage 4 :- 5 Questions and each wins you 5000$
Stage 5 :- The Golden Stage has 1 Final Question and it wins you a huge 10000$
Isn't that just great?

To proceed to the next stage you must answer all the questions of the previous stage correctly...
Alright then let's get Started'''
print(intro.center(100))

# Main-Loop
print("Stage 1".center(100))
for i in range(21) :
    print(f"Question {i+1} :- " + question[i])
    ans = input("Enter the Correct Option : ").strip().upper()
    if ans == answer[i] :   # Checking Answer
        print("CORRECT!!!".center(100))
        count += 1
        if i <= 4 :
            prize += 100
            
        elif i <= 9 :
            prize += 500
            
        elif i <= 14 :
            prize += 1000

        elif i <= 19 :
            prize += 5000

        else :
            prize += 10000
            
    else :
        print("Wrong!".center(100))
    
    if i == 4 :
        if count != 5 :
            print("Game Over!!!".center(100))
            break
        else :
            print("Congratulations!!! Stage 2 :".center(100))
    elif i == 9 :
        if count != 10 :
            print("Game Over!!!".center(100))
            break
        else :
            print("Congratulations!!! Stage 3 :".center(100))
    elif i == 14 :
        if count != 15 :
            print("Game Over!!!".center(100))
            break
        else :
            print("Congratulations!!! Stage 4 :".center(100))
    elif i == 19 :
        if count != 20 :
            print("Game Over!!!".center(100))
            break
        else :
            print("WOO HOO!!! LAST GOLDEN STAGE!!!".center(100))
    elif i == 20 :
        continue
    else :
        print("Next Question :".center(100))

# Final Part Of The Game

if count == 21 :
    print("You are a True Dexter Fan... RESPECT!!!".center(100))
elif count >= 10 :
    print("Not Bad!!! Well Done...".center(100))
else :
    print("Well... Next Time Don't Go Skipping Scenes".center(100))

print(f"Congratulations! You have won {prize}$".center(100))
print("Thank You for playing".center(100))