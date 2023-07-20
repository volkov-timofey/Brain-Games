### Hexlet tests and linter status:
[![Actions Status](https://github.com/volkov-timofey/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/volkov-timofey/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/volkov-timofey/python-project-49/maintainability)

This game that runs in the terminal. 100% Python.

### Installation
Make sure you are running at least Python 3.10.0

Clone the repository and install manually:

```bash
$ git clone https://github.com/volkov-timofey/python-project-49.git
$ cd python-project-49
$ make full # build, publish in pip, package-install
```

### Start Games
##### Game: "Check for even"
+ ##### Rules:

    To win, you need to correctly answer the proposed tasks 3 times.
    If you make a mistake, try starting over.

To start the game, run either:


```bash
$ brain-even
```

##### Game: "Calculator"
+ ##### Rules:

    To win, you need to correctly answer the proposed arithmetic tasks (only +, - or *) 3 times.
    If you make a mistake, try starting over.

To start the game, run either:


```bash
$ brain-calc
```

##### Game: "Greatest Common Divisor (GCD)"
+ ##### Rules:

    Two random numbers are displayed on the screen, for example, 25 50. It is necessary to calculate and enter the greatest common divisor of these numbers.
    To win, you need to correctly answer the proposed tasks 3 times.
    If you make a mistake, try starting over.

To start the game, run either:


```bash
$ brain-gcd
```

##### Game: "Arithmetic progression"
+ ##### Rules:

    It is necessary to determine the missing number in an arithmetic progression.
    To win, you need to correctly answer the proposed tasks 3 times.
    If you make a mistake, try starting over.

To start the game, run either:


```bash
$ brain-progression
```

##### Game: "Is it a prime number?"
+ ##### Rules:

    Need to answer if the number is prime.
    To win, you need to correctly answer the proposed tasks 3 times.
    If you make a mistake, try starting over.

To start the game, run either:


```bash
$ brain-prime
```

PS
: for Anton

Привет, Антон! Платформа, не позволяет написать свой фидбек на сайте или я его не нашел, поэтому напишу тут.

+ Спасибо за ревью в первую очередь! (отличные примеры, особенно ascii_racer)
Постарался не заниматься самодеятельностью и исправил то что было в замечаниях, получилась хорошая оптимизация. Пока пересобирал код пришла доработка, чтобы с одного запуска пользователю предлагались игры и окно не закрывалось пока сам пользователь этого не захочет.
+ Немного расскажу о себе, откуда могут вылезать какие нибудь нетипичные ошибки. Учился ранее на DS в Яндекс.Практикуме и был 2х месячный интенсив от ЦФТ (Золотая корона), по Deep Learning CV, после которого я понял, что многие вещи разработчика просто необходимы.
+ Из ранее сказанного вылез файл config, хотелось сделать более конфигурируемые игры. YAML использовать не получилось. Как часто используется в разработке стартовое конфигурирование типа YAML, или зачастую эти данные к нам приходят из сторонних источников. Какие из способов конфигурирования сейчас более широко распространены? (буду благодарн ссылкам)
+ Так же писали в проекте, что не нужно забегать вперед, весь код писал в NotePad++, не привычно, отсутствие "синтаксического сахара", поэтому вопрос) Можно ли переехать на PyCharm?

PPS: можно ли писать в личку на платформе Mattermost?
