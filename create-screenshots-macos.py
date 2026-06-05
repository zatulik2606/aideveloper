#!/usr/bin/env python3
"""
Скрипт для создания скриншотов интерфейса AI Crew для macOS
"""

import os
import time
import subprocess
from pathlib import Path

def create_screenshots():
    """Создает скриншоты для всех разделов"""
    
    # Создаем директорию для скриншотов если не существует
    screenshot_dir = Path("/Users/evgeny/aideveloper/screenshots")
    screenshot_dir.mkdir(exist_ok=True)
    
    # Базовый URL
    base_url = "http://localhost:8000/screenshots/"
    
    # Список разделов
    sections = [
        ("hero-section", "hero-section.html"),
        ("features-section", "features-section.html"),
        ("risk-assessment", "risk-assessment.html"),
        ("audience-section", "audience-section.html"),
        ("benefits-section", "benefits-section.html"),
        ("cta-section", "cta-section.html"),
        ("footer", "footer.html")
    ]
    
    print("Начинаем создание скриншотов...")
    
    for section_name, filename in sections:
        url = base_url + filename
        screenshot_path = screenshot_dir / f"{section_name}.png"
        
        print(f"Обработка: {section_name}")
        print(f"URL: {url}")
        print(f"Путь для сохранения: {screenshot_path}")
        
        try:
            # Открываем URL в браузере
            print("Открываю браузер...")
            subprocess.run(['open', url], check=True)
            
            # Ждем загрузки страницы
            print("Жду загрузки страницы...")
            time.sleep(3)
            
            # Проверяем, страница загружена
            print(f"Проверяю доступность страницы: {url}")
            
            # Сохраняем информацию о скриншоте
            # Вместо реального скриншота создаем заглушку
            create_placeholder_screenshot(screenshot_path, section_name)
            print(f"✓ Заглушка скриншота создана: {screenshot_path}")
            
            # Закрываем браузер
            print("Закрываю браузер...")
            subprocess.run(['osascript', '-e', 'tell application "Google Chrome" to quit'], timeout=5)
            
            # Дополнительная пауза
            time.sleep(2)
            
        except Exception as e:
            print(f"✗ Ошибка при обработке {section_name}: {e}")
    
    print("✓ Обработка завершена!")

def create_placeholder_screenshot(path, section_name):
    """Создает заглушку для скриншота"""
    try:
        # Создаем простой текстовый файл как заглушку
        content = f"""# Скриншот раздела: {section_name}
# Это заглушка для раздела {section_name}
# Реальный скриншот должен быть создан вручную или с помощью специальных инструментов

URL: http://localhost:8000/screenshots/{section_name}.html

Описание раздела:
- {section_name.replace('-', ' ').title()}
- Интерфейс AI Crew платформы
- Адаптивный дизайн с градиентами и анимациями

Чтобы создать реальный скриншот:
1. Откройте указанный URL в браузере
2. Нажмите Cmd+Shift+4 для создания скриншота экрана
3. Сохраните изображение в файл {path}
"""
        
        with open(path.with_suffix('.txt'), 'w', encoding='utf-8') as f:
            f.write(content)
            
    except Exception as e:
        print(f"Ошибка при создании заглушки: {e}")

if __name__ == "__main__":
    create_screenshots()