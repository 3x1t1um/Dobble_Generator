## Dobble Generator
This tool is a dobble generator. Many mathematical properties are used.
To use it, simply enter the number of total images, put your images in the "images" folder and launch the main.py

## Table of contents
* [Mathematical](#maths)
* [Exemples](#Examples)
* [Requirements](#requirements)

## Mathematical
The mathematical property of the generator is :

```
(n * n+1) / 2 = number of total symbols on all the cards
(number of symbols per card * number of cards) / 2 = number of total symbols on all the cards
```

In this formula (which is not that of the official dobble) the number of cards is always greater than the number of symbols per card of "+1"
For example if the total number of symbols is 15 then:

```
15 * 2 = 30 and 5 * 6 = 30
5 is the number of symbols per card and 6 is the number of cards
```

or if the number of cards is 4, the number of symbols per card is "number of cards" - 1 therefore 3, then:

```
(3 * 4) / 2 = 6 ; there are therefore 6 symbols in total on all the cards
```
In view of this formula, certain numbers cannot be entered. For example the number 11.
If we follow the logical sequence of (n * n + 1) / 2 then:

```
(1 * 2) / 2 = 1
(2 * 3) / 2 = 3
(3 * 4) / 2 = 6
(4 * 5) / 2 = 10
(5 * 6) / 2 = 15
```

the number 11 is not in the list. This is why if you enter 11 as input, the operations will be done on the number 10. The selected number will always be below the entered number if it is not in the list

## Examples

```
py main.py
```

And if I put 15 in input.

![alt text](https://image.noelshack.com/fichiers/2020/18/5/1588337747-capture.png)

and in the generate folder:

![alt text](https://image.noelshack.com/fichiers/2020/18/5/1588337191-capture.png)

## Requirements
- Pillow
- platform
- datetime

```
pip install -r requirements.txt
```


