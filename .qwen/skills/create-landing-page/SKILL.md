---
name: create-landing-page
description: Создание современной landing page для IT-платформ с использованием современных веб-технологий
source: auto-skill
extracted_at: '2026-06-05T07:42:29.246Z'
---

# Создание landing page для IT-платформы

Этот навык описывает процесс создания современной landing page для IT-платформы, такой как AI Crew, с использованием современных веб-технологий.

## Процесс реализации

### 1. Планирование и анализ требований

#### Определение целей
- Понять, для какой платформы создается landing page
- Определить целевую аудиторию
- Составить список ключевых функций и преимуществ

#### Сбор информации
- Прочитать README.md проекта для понимания контекста
- Определить основные ценности продукта
- Выбрать подходящий дизайн и функционал

### 2. Создание структуры файлов

#### Необходимые файлы
```
project-root/
├── index.html          # Основная HTML страница
├── styles.css          # Стили и дизайн
├── script.js           # Интерактивные функции
├── package.json        # Конфигурация проекта
└── netlify.toml        # Настройки развертывания (опционально)
```

#### Структура HTML
- Заголовок с навигацией
- Hero секция с основным предложением
- Секция с ключевыми возможностями
- Описание рисков и преимуществ
- CTA (Call to Action) секция
- Футер

### 3. Реализация дизайна

#### Цветовая схема
- Использовать современные градиенты
- Поддерживать консистентность цветов
- Учитывать брендбук проекта

#### Типографика
- Выбрать веб-безопасные шрифты
- Создать иерархию заголовков
- Определить основные размеры и отступы

#### Адаптивный дизайн
- Mobile-first подход
- Гибкие сетки (CSS Grid/Flexbox)
- Медиа-запросы для разных размеров экранов

### 4. Разработка функциональности

#### Основные интерактивные элементы
- Плавная прокрутка к секциям
- Hover-эффекты на кнопках и карточках
- Анимации при скролле
- Адаптивное меню

#### Оптимизация производительности
- Минимизация CSS и JavaScript
- Ленивая загрузка изображений
- Оптимизация шрифтов

### 5. Настройка развертывания

#### Локальная разработка
```bash
npm init -y
npm start  # Запускает локальный сервер на 8000 порту
```

#### GitHub Pages
1. Создать workflow для автоматического развертывания
2. Настроить права доступа
3. Активировать GitHub Pages в настройках репозитория

#### Альтернативные платформы
- Netlify: требует входа в аккаунт и CLI
- Vercel: требует входа в аккаунт и CLI
- GitHub Pages: бесплатный и простой вариант

### 6. Тестирование и оптимизация

#### Проверка кроссбраузерности
- Тестирование в Chrome, Firefox, Safari, Edge
- Проверка мобильных браузеров

#### SEO оптимизация
- Семантическая HTML5 разметка
- Meta теги для описания
- Оптимизированные заголовки и описания

#### Тестирование производительности
- Проверка скорости загрузки
- Оптимизация изображений
- Минимизация ресурсов

## Пример кода

### Базовая структура HTML
```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Название платформы</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <section class="hero">
        <div class="container">
            <h1>Название платформы</h1>
            <p>Краткое описание основных возможностей</p>
            <div class="cta-buttons">
                <a href="#demo" class="btn primary">Демонстрация</a>
                <a href="#features" class="btn secondary">Функции</a>
            </div>
        </div>
    </section>
    
    <section id="features" class="features">
        <div class="container">
            <h2>Ключевые возможности</h2>
            <div class="features-grid">
                <!-- Карточки функций -->
            </div>
        </div>
    </section>
    
    <script src="script.js"></script>
</body>
</html>
```

### Адаптивные стили
```css
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.btn {
    display: inline-block;
    padding: 12px 24px;
    margin: 10px;
    text-decoration: none;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn.primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

@media (max-width: 768px) {
    .cta-buttons {
        flex-direction: column;
        align-items: center;
    }
    
    .btn {
        width: 100%;
        max-width: 300px;
    }
}
```

### Интерактивность JavaScript
```javascript
// Плавная прокрутка
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Анимации при скролле
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, { threshold: 0.1 });

// Применение анимаций
document.querySelectorAll('.feature-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});
```

## Советы и лучшие практики

1. **Начинайте с контента**: Сначала напишите текстовое содержание, затем добавляйте стили
2. **Используйте CSS-переменные**: Для легкого управления цветами и размерами
3. **Тестируйте на реальных устройствах**: Не только в браузере разработчика
4. **Оптимизируйте изображения**: Используйте современные форматы (WebP)
5. **Добавляйте микро-взаимодействия**: Hover-эффекты улучшают пользовательский опыт
6. **Следите за производительностью**: Используйте инструменты вроде Lighthouse

## Типичные проблемы и решения

### Проблема: Неработающие ссылки развертывания
**Решение**: 
- Проверить статус входа в аккаунт платформы
- Убедиться, что все файлы добавлены в Git
- Проверить права доступа к репозиторию

### Проблема: Плохая производительность
**Решение**:
- Минимизировать CSS и JavaScript
- Использовать lazy loading для изображений
- Оптимизировать размеры медиафайлов

### Проблема: Неадаптивный дизайн
**Решение**:
- Проверить медиа-запросы
- Использовать относительные единицы измерения (rem, em, %)
- Тестировать на разных устройствах