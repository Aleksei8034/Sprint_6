# Sprint_6  

Автотесты для сервиса «Яндекс.Самокат»

tests - каталог с тестами

tests/ test_main_page: содержит тесты для главной страницы проверяет переход по клику.

tests/ test_order_page: содержит тесты заказа самоката по клику кнопки с разных расположений.

tests/ test_questions_main_page: содержит тесты на проверку вопросов о важном.

allure_results - каталог с отчетом о тестировании

locators - каталог с файлами локаторов страниц

pages - каталог с файлами страниц

сonftest.py - файл с фикстурами

data - вспомагательный файл с данными

для установки внешних зависимостей: pip install -r requirements.txt

Запустить все тесты из директории tests: pytest tests --alluredir=allure_results

Для отчета введите команду: allure serve allure_results
