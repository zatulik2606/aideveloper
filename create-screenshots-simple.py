#!/usr/bin/env python3
"""
Простой скрипт для создания скриншотов интерфейса AI Crew
Использует системные команды для создания скриншотов
"""

import os
import time
import subprocess
import sys
from PIL import Image, ImageGrab
import pyautogui

def create_screenshots():
    """Создает скриншоты для всех разделов"""
    
    # Создаем директорию для скриншотов если не существует
    screenshot_dir = "/Users/evgeny/aideveloper/screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    
    # URL сервера
    base_url = "http://localhost:8000/screenshots/"
    
    # Словарь разделов для скриншотов
    sections = {
        'hero-section': 'hero-section.html',
        'features-section': 'features-section.html',
        'risk-assessment': 'risk-assessment.html',
        'audience-section': 'audience-section.html',
        'benefits-section': 'benefits-section.html',
        'cta-section': 'cta-section.html',
        'footer': 'footer.html'
    }
    
    print("Начинаем создание скриншотов...")
    
    # Открываем браузер для каждого раздела
    for section_name, filename in sections.items():
        url = base_url + filename
        screenshot_path = os.path.join(screenshot_dir, f"{section_name}.png")
        
        print(f"Создание скриншота: {section_name}")
        
        try:
            # Открываем URL в браузере (используем open для macOS)
            subprocess.run(['open', url], check=True)
            
            # Ждем загрузки страницы
            time.sleep(3)
            
            # Делаем скриншот всей области экрана
            screenshot = pyautogui.screenshot()
            
            # Сохраняем скриншот
            screenshot.save(screenshot_path)
            print(f"✓ Скриншот сохранен: {screenshot_path}")
            
            # Закрываем вкладку (экспериментальный подход)
            # Это может не сработать во всех браузерах
            try:
                # Команда для закрытия текущей вкладки в Chrome
                subprocess.run(['osascript', '-e', 'tell application "Google Chrome" to close active tab'], timeout=2)
            except:
                pass
            
            # Дополнительная пауза перед следующим скриншотом
            time.sleep(1)
            
        except Exception as e:
            print(f"✗ Ошибка при создании скриншота {section_name}: {e}")
    
    print("✓ Все скриншоты успешно созданы!")

if __name__ == "__main__":
    create_screenshots()