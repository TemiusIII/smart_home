# smart_home
Это умный дом на Ардуино и все что к нему есть!

В файле "config.json" у нас храняться команды, что-бы просто программа сравнивала то, что человек говорит с ними.

В файле "main.py" у нас код на Python для распознования речи и ответа пользователю, так же он отправляет Arduino зашифрованные команды.

В файле "arduino_code.ino" у нас код для Arduino, в нем мы указываем, что мы делаем при разных командах, которые он разшифровывает от "main.py".

Файл "config_undecoded.json" мы тестируем значения в "ASCII", что-бы потом их преобразовать в закодированные байты, для сравнивания с голосом!

Файл ".gitignore" позволял нам удаленно одновременно работать над проектом!

Спасибо за внимание!!!
