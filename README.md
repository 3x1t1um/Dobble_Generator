## Dobble Generator
This tool is a dobble generator. Many mathematical properties are used.
To use it, simply put your images in the "images" folder, launch the main.py and enter the amount of images.
Please read "Mathematics" to understand how the generator works and how to use it.

## Table of contents
* [Mathematics](#Mathematics)
* [Exemples](#Examples)
* [Requirements](#requirements)

## Mathematics
The main mathematical property of the generator is :

```
(n * n+1) / 2 = number of total symbols on all the cards
# which corresponds to :
(number of symbols per card * number of cards) / 2 = number of total symbols on all the cards
```

In this formula (which is not that of the official dobble) the number of cards is always greater than the number of symbols per card of "+1".
For example if the total number of symbols is 15 then (it's the same formula but backwards) :

```
15 * 2 = 30 and 5 * 6 = 30
5 is the number of symbols per card and 6 is the number of cards
```

Or if the number of cards is 4, the number of symbols per card is "number of cards" - 1 therefore 3, then:

```
(3 * 4) / 2 = 6 ; there are 6 symbols in total on all the cards
```
In view of this formula, some numbers cannot be entered. For example the number 11.
If we follow the logical sequence of (n * n + 1) / 2 then:

```
(1 * 2) / 2 = 1
(2 * 3) / 2 = 3
(3 * 4) / 2 = 6
(4 * 5) / 2 = 10
(5 * 6) / 2 = 15
```

The number 11 is not in the list. This is why if you enter 11 as input, the operations will be done on the number 10. The selected number will always be below the entered number if it is not in the list.

## Examples

```
py main.py
```

If I put 15 in input :

![alt text](https://image.noelshack.com/fichiers/2020/18/5/1588337747-capture.png)

And in the generate folder:

![alt text](https://image.noelshack.com/fichiers/2020/18/5/1588337191-capture.png)

## Requirements
- Pillow
- platform
- datetime

```
pip install -r requirements.txt
```
