# Refactor an Implementation of Student Directory

In `student_directory.py` you'll find the code for a program manages a list of students. Do `python3 student_directory.py` to play with it a little.

As you'll see, the program is composed entirely of 'top level' functions. It works, but it's a bit of a mess. Your job is to tidy things up by breaking the code up into some classes.

## Making a plan

### 1. Identify behaviours

Start by taking a look at the codebase and making a note of all the different things that it does. From now on, we'll call those 'behaviours'. One example would be the behaviour of writing to a file. Another would be the behaviour of reading from a file.

As you read through the code for this exercise, your approach should be to get the gist of what's going on rather than to figure out in detail exactly _how_ it is being done. Save some brainpower for later.

### 2. Identify state

Once you have a list of behaviours, look for bits of state in the program. The name of a student, would be one good example. Make a list of these too.

### 3. Plan some classes

Now you're ready to think about how the various behaviours and bits of state could group into coherent chunks - these chunks will be your classes.

- Decide which bits of state and which behaviours belong together
- Give your classes sensible, descriptive names

### 4. Iterate towards your plan

This is the hardest part. Your goal here is not to delete everything and start again - this would not normally be a feasible approach in any serious project, though it does (sort of) happen sometimes. Instead, you are to iterate toward your solution by taking several, or many, small steps. Crucially, after each step the program should still work.

Good luck!

### 5. Share your solution and look at other people's

No explanation needed :)
