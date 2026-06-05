#!/usr/bin/env python3
"""
Скрипт для создания скриншотов интерфейса AI Crew
"""

import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройки Chrome для headless режима
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080')

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

def create_screenshots():
    """Создает скриншоты для всех разделов"""
    try:
        # Инициализация драйвера
        driver = webdriver.Chrome(options=chrome_options)
        
        # Создаем директорию для скриншотов если не существует
        screenshot_dir = "/Users/evgeny/aideveloper/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        
        for section_name, filename in sections.items():
            url = base_url + filename
            screenshot_path = os.path.join(screenshot_dir, f"{section_name}.png")
            
            print(f"Создание скриншота: {section_name}")
            
            try:
                # Загрузка страницы
                driver.get(url)
                
                # Ожидание загрузки контента
                time.sleep(2)
                
                # Сделать скриншот
                driver.save_screenshot(screenshot_path)
                print(f"✓ Скриншот сохранен: {screenshot_path}")
                
            except Exception as e:
                print(f"✗ Ошибка при создании скриншота {section_name}: {e}")
        
        driver.quit()
        print("✓ Все скриншоты успешно созданы!")
        
    except Exception as e:
        print(f"✗ Ошибка при инициализации Chrome: {e}")
        print("Попробуйте установить ChromeDriver: brew install chromedriver")

if __name__ == "__main__":
    create_screenshots()