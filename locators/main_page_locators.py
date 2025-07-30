from selenium.webdriver.common.by import By


class MainPageLocator:
    MAKE_ORDER_TOP_BUTTON = [By.XPATH, "//button[contains(text(), 'Статус заказа')]/preceding-sibling::button"]
    MAKE_ORDER_BOTTOM_BUTTON = [By.XPATH, ".//button[contains(@class, 'Button_Middle')]"]
    COOKIE_BUTTON = [By.XPATH, '//*[@id="rcc-confirm-button"]']
    SCOOTER_ICON = [By.XPATH, '//img[@src="/assets/scooter.svg" and @alt="Scooter"]']
    IMG_MAIN_PAGE = [By.XPATH, '//img[@src="/assets/scooter.png"]']
    YANDEX_ICON = [By.XPATH, '//img[@src="/assets/ya.svg"]']
    YANDEX_SEARCHING_FIELD = [By.XPATH, '//*[contains(text(), "Поиск Яндекса")]']
   

    faq_section = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')
    faq_questions_items = {
        1: [By.XPATH, '//div[@id="accordion__heading-0"]/parent::div'],
        2: [By.XPATH, '//div[@id="accordion__heading-1"]/parent::div'],
        3: [By.XPATH, '//div[@id="accordion__heading-2"]/parent::div'],
        4: [By.XPATH, '//div[@id="accordion__heading-3"]/parent::div'],
        5: [By.XPATH, '//div[@id="accordion__heading-4"]/parent::div'],
        6: [By.XPATH, '//div[@id="accordion__heading-5"]/parent::div'],
        7: [By.XPATH, '//div[@id="accordion__heading-6"]/parent::div'],
        8: [By.XPATH, '//div[@id="accordion__heading-7"]/parent::div']
    }

    faq_answers_items = {
        1: (By.XPATH, '//div[@id="accordion__panel-0"]'),
        2: (By.XPATH, '//div[@id="accordion__panel-1"]'),
        3: (By.XPATH, '//div[@id="accordion__panel-2"]'),
        4: (By.XPATH, '//div[@id="accordion__panel-3"]'),
        5: (By.XPATH, '//div[@id="accordion__panel-4"]'),
        6: (By.XPATH, '//div[@id="accordion__panel-5"]'),
        7: (By.XPATH, '//div[@id="accordion__panel-6"]'),
        8: (By.XPATH, '//div[@id="accordion__panel-7"]')
    }

