# Комрпессор изображений
## Используемые библиотеки/фреймворки:
- [Pillow](https://pillow.readthedocs.io/en/stable/)

## Описание

### Программа для уменьшения размеров изображений

## Способ запуска

- Создать виртуальное окружение (venv):
  > python -m venv **Your venv name**
  
- Установить requirements из requirements.txt с помощью команды:
  > pip install requirements.txt
  
- запустить скрипт *compress.py*
  > python compress.py **-i image_name** or **-d dir_path**

### Параметры запуска
> Флаг -i, --image - Конвертирует указанный файл
>
> Флаг -d, --dir - Конвертирует все jpeg файлы в укзанной директории
>
> Флаг -j, --to-jpg - Конвертирует в JPEG формат
>
> Флаг -q, --quality - Уровень качества от 0 до 95 (default=90)
> 
> Флаг -r, --resize-ratio - Степень сжатия от 0 до 1, (default=1.0)
> 
> Флаг -w, --width - Новая ширина файла, только с height параметром
> 
> Флаг -h, --height - Новая ширина файла, только с width параметром
 
