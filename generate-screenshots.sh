#!/bin/bash

# Скрипт для генерации скриншотов интерфейса AI Crew

SCREENSHOT_DIR="/Users/evgeny/aideveloper/screenshots"
BASE_URL="http://localhost:8000/screenshots/"

# Создаем директорию для скриншотов
mkdir -p "$SCREENSHOT_DIR"

echo "Начинаем создание скриншотов..."
echo "Для каждого раздела откроется браузер, нажмите Cmd+Shift+4, чтобы сделать скриншот экрана"
echo "После этого нажмите любую клавишу для продолжения..."

# Список разделов
SECTIONS=(
    "hero-section:hero-section.html"
    "features-section:features-section.html"
    "risk-assessment:risk-assessment.html"
    "audience-section:audience-section.html"
    "benefits-section:benefits-section.html"
    "cta-section:cta-section.html"
    "footer:footer.html"
)

for section in "${SECTIONS[@]}"; do
    IFS=':' read -r name filename <<< "$section"
    
    echo ""
    echo "=== $name ==="
    echo "Открываю: $BASE_URL$filename"
    echo "Нажмите любую клавишу, чтобы открыть браузер..."
    read -n 1
    
    # Открываем URL в браузере
    open "$BASE_URL$filename"
    
    echo "Браузер открыт. Сделайте скриншот экрана (Cmd+Shift+4), затем нажмите любую клавишу..."
    read -n 1
    
    # Закрываем браузер
    osascript -e 'tell application "Google Chrome" to quit'
    
    echo "Браузер закрыт."
    echo "Ожидание перед следующим разделом..."
    sleep 2
done

echo ""
echo "Готово! Все скриншоты должны быть созданы в директории: $SCREENSHOT_DIR"