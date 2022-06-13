# a Simple ATM
**The following flow has been implemented**

```
Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
```

For simplification, there is only 1 dollar bill in this project, no cents.

Thus account balance can be represented in integers.

</br>

# Demo
![ATM_demo](https://user-images.githubusercontent.com/77220012/173383597-8fdfcd32-7f67-4e75-a0e5-9ecd754f39f9.gif)


</br>

# Running

```python
python ATM_project.py
```

</br>

# Unit Testing

```python
python -m unittest discover [option] . ATM_test.py
```

**option :** 

- **` v , -verbose `**
    
    Verbose output
    
- **` s, -start-directory directory`**
    
    Directory to start discovery (`.` default)
    
- **` p, -pattern pattern`**
    
    Pattern to match test files (`test*.py` default)
    
- **` t, -top-level-directory directory`**
    
    Top level directory of project (defaults to start directory)
    
- **` f, -failfast`**
    
    Stop the test run on the first error or failure.


**example :** </br>
![ATM_test](https://user-images.githubusercontent.com/77220012/173383727-5c51c271-eca2-4cb9-9f2c-f0892105d560.png)

