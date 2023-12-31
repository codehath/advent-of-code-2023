> Original Problem - https://adventofcode.com/2023/day/9  
> Abstracted Problem - [Day 9 - Mirage Maintenance](/day-9/abstract_problem.md)  
> [Input Data](/day-9/input/input_day_09.txt) - [My Solution](/day-9/day_9.py)
> 
> __Computer Science Principles/Maths Used:__  
> `-` Functional Programming  
> `-` Recursive Function Calls  

---
#### Thinking Process
Created recursive function that 
calculates increment between each number of a sequence, 
calls itself recursively with these `increments` as the `sequence` parameter, 
calculates the next number in the sequence using the recursive call 
and returns it.

```python
def next_in_sequence(sequence):
    increments = []
    for index, num in enumerate(sequence):
        if index != len(sequence) -1:
            increments.append(sequence[index+1] - num)

    if set(increments) == {0}: return sequence[-1]
    return sequence[-1] + next_in_sequence(increments)
```

Then just call the function on each sequence in the input and sum the returned values.


__Part 2:__
Exactly the same as part one but this time the recursive function returns the number that would've come before the start of the sequence.

---
#### Issues
Very straightforward, no issues today

---
#### Things I thought about afterwards:
To reduce repetition, could combine `next_in_sequence()` and `previous_in_sequence()` functions into a one by taking in an additional boolean parameter - representing whether the next or previous value in sequence is required.

---
[< Back to all solutions](/README.md)