# a Simple ATM

# Demo

**The following flow has been implemented**

```
Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
```

For simplification, there is only 1 dollar bill in this project, no cents.

Thus account balance can be represented in integers.


# Running

```python
python ATM_project.py
```

# Unit Testing

```python
python -m unittest discover [option] . ATM_test.py
```

**option :** 

- **`v**, **-verbose**`
    
    Verbose output
    
- **`s**, **-start-directory** directory`
    
    Directory to start discovery (`.` default)
    
- **`p**, **-pattern** pattern`
    
    Pattern to match test files (`test*.py` default)
    
- **`t**, **-top-level-directory** directory`
    
    Top level directory of project (defaults to start directory)
    
- **`f**, **-failfast**`
    
    Stop the test run on the first error or failure.
