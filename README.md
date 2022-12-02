# Лабораторная работа 2 по дисциплине "Технологии программирования"

**Изучение фреймворка MVC**

Выполнил: Ст.гр. САПР-1.4 Шебаршов Артем

## Цели

1. Познакомиться c моделью MVC, ее сущностью и основными фреймворками на ее основе.
2. Разобраться с сущностями «модель», «контроллер», «представление», их функциональным назначением.
3. Получить навыки разработки веб-приложений с использованием MVC-фреймворков, написания модульных тестов к ним и интеграции приложений в конвейер CI / CD;
4. Получить навыки управления автоматизированным тестированием и разворачиванием программного обеспечения, расположенного в системе Git, с помощью инструмента Travis CI.

## Задачи

1. Выберите для Вашего проекта тип лицензии и добавьте файл с лицензией в проект.
2. Доработайте проект магазина, добавив в него новую функциональность и информацию в базу данных в соответствии с типом магазина (согласно индивидуальному варианту, см. таблицу). Составьте модульные тесты к проекту, постарайтесь покрыть тестами максимально возможный объем кода. Для работы с этим заданием создайте новую ветку кода на основе главной и фиксируйте в нее весь программный код в процессе разработки. Добейтесь выполнения всех тестов проекта, после чего объедините текущую ветку кода с главной.
3. Обеспечьте автоматическое тестирование и разворачивание приложения на любом доступном хостинге. Для выполнения этих операций можно использовать любые инструменты CI / CD.
4. Проанализируйте полученные результаты и сделайте выводы.

## Постановка задачи

Дан проект сайта интернет-магазина. В соответствии с индивидуальным вариантом:

- сформировать ассортимент магазина товаров для сада
- реализовать:
  - наличие ограниченного числа товара в продаже
  - уменьшение числа товара при его покупке
  - повышение цены товара при уменьшении количества товара более чем в два раза

## Индивидуальный вариант

| Вариант | Тип магазина             | Функциональность приложения                                                                                                                                                                       |
|---------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 11      | Магазин товаров для сада | В магазине имеется определенное количество товара каждого вида. После покупки количество товара уменьшается. Если количество товара уменьшилось более чем в два раза, его цена возрастает на 20%. |

## Используемые язык и библиотеки

Используется язык `Python 3.10` с фреймворком `Django`

## Краткое описание проекта

Проект представляет собой интернет магазин. По индивидуальному варианту в магазине продаются товары для сада. Количестов товара ограничено и уменьшается при покупке. Если остаётся менее половины товара, его цена увеличивается на 20%.

## Выводы

Выполнив лабораторную работу я реализовал приложение в модели MVC с использованием фреймворка Django.
