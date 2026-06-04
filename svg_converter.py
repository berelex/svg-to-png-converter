#!/usr/bin/env python3
import os
import json
import argparse
import cairosvg

def load_config(config_path):
    """Загрузка конфигурации из JSON файла."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Файл конфигурации не найден: {config_path}")
    
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def convert_svg_to_package(svg_path, output_dir, config_path, preset_name):
    """Конвертация SVG в пакет PNG по заданному пресету."""
    # Проверки исходного файла
    if not os.path.exists(svg_path):
        print(f"Ошибка: Исходный файл {svg_path} не существует.")
        return

    # Загрузка конфига и выбор пресета
    try:
        config = load_config(config_path)
        packages = config.get("output_packages", {})
        if preset_name not in packages:
            print(f"Ошибка: Пресет '{preset_name}' не найден в {config_path}")
            print(f"Доступные пресеты: {', '.join(packages.keys())}")
            return
        sizes_to_render = packages[preset_name]
    except Exception as e:
        print(f"Ошибка при чтении конфигурации: {e}")
        return

    # Создаем выходную папку, если её нет
    os.makedirs(output_dir, exist_ok=True)

    print(f"Начало конвертации файла: {svg_path}")
    print(f"Используется пресет: {preset_name} ({len(sizes_to_render)} файлов)")
    print("-" * 50)

    # Процесс конвертации
    for item in sizes_to_render:
        filename = item.get("name")
        width = item.get("width")
        height = item.get("height")

        if not filename or not width or not height:
            print(f"Пропуск некорректной записи в конфиге: {item}")
            continue

        output_path = os.path.join(output_dir, filename)
        
        try:
            # CairoSVG автоматически масштабирует вектор под нужные output_width/output_height
            cairosvg.svg2png(
                url=svg_path,
                write_to=output_path,
                output_width=width,
                output_height=height
            )
            print(f"✓ Создан: {filename} ({width}x{height}px)")
        except Exception as e:
            print(f"✕ Ошибка при создании {filename}: {e}")

    print("-" * 50)
    print(f"Готово! Все файлы сохранены в папку: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI утилита для пакетной конвертации SVG в PNG заданных размеров.")
    
    # Обязательный аргумент
    parser.add_argument("svg_path", help="Путь к исходному SVG файлу")
    
    # Необязательные аргументы с дефолтными значениями
    parser.add_argument("-c", "--config", default="config.json", help="Путь к файлу конфигурации JSON (по умолчанию: config.json)")
    parser.add_argument("-o", "--output", default="output", help="Путь к папке для сохранения PNG (по умолчанию: ./output)")
    parser.add_argument("-p", "--preset", default="default", help="Имя пресета настроек из конфига (по умолчанию: default)")

    args = parser.parse_args()

    convert_svg_to_package(
        svg_path=args.svg_path,
        output_dir=args.output,
        config_path=args.config,
        preset_name=args.preset
    )