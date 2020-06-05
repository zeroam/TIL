## Quiz In [regex101](https://regex101.com/)

### TASK 1. WORD BOUNDARIES

- description

```markdown
Check if a string contains the word `word` in it (case insensitive). If you have no idea, I guess you could try `/word/`.
```

- pattern

```javascript
/\bword\b/i
```



### TASK 2. CAPITALIZING I

- description

```markdown
Use substitution to replace every occurrence of the word `i` with the word `I` (uppercase, I as in me). E.g.: `i'm replacing it. am i not?` -> `I'm replacing it. am I not?`. A regex match is replaced with the text in the `Substitution` field when using substitution.
```

- pattern

```javascript
/\bi\b/g
```

- replace

```
I
```



### TASK 3. UPPERCASE CONSTANTS

- description

```markdown
With regex you can *count* the number of matches. Can you make it return the number of uppercase consonants (B,C,D,F,..,X,Y,Z) in a given string? E.g.: it should return `3` with the text `ABcDeFO!`. **Note:** Only ASCII. We consider `Y` to be a consonant! **Example:** the regex `/./g` will return **3** when run against the string `abc`.
```

- pattern

```javascript
/[^AEIOUa-z0-9\W_]/g
```



### TASK 4: RETRIEVE NUMBERS

- description

```markdown
Count the number of integers in a given string. Integers are, for example: `1, 2, 65, 2579`, etc.
```

- pattern

```javascript
/\d+/g
```



### TASK 5: WHITESPACE

- description

```markdown
Find all occurrences of **4 or more** whitespace characters in a row throughout the string.
```

- pattern

```javascript
/\s{4,}/g
```





### TASK 6: BROKEN KEYBOARD

- description

```markdown
Oh no! It seems my friends spilled beer all over my keyboard last night and my keys are super sticky now. Some of the time whennn I press a key, I get two duplicates. Can you ppplease help me fix thhhis?
```

- pattern

```javascript
/(.)\1\1/g
```

- replace

```
\1
```





### TASK 7: VALIDATE AN IP

- description

```markdown
Validate an IPv4 address. The addresses are four numbered separated by three dots, and can only have a maximum value of 255 in either octet. Start by trying to validate `172.16.254.1`.
```

- pattern

```javascript
/^(?:(?:25[0-5]|2[0-4][0-9]|1\d{2}|[1-9]\d|\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)$/
```





## Samples

### Password Check

```javascript
/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^\w\d\s:])([^\s]{8,})$/gm
```



### Strip

```javascript
/(?:(.*?)\n)/gm
```

