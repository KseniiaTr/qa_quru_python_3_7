import allure

from selene import by, be
from selene.support.shared import browser
from allure_commons.types import Severity



def test_steps_all(size_browser):
    with allure.step('Открываем страницу GitHub'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий по названию'):
        browser.element('.header-search-input').send_keys(
            'eroshenkoam/allure-example').submit()

    with allure.step('Переходим в репозиторий'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем вкладку Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие текста 57 во всех Issues'):
        browser.element(by.partial_text('#57')).should(be.visible)


def test_razmetka_steps():
    allure.dynamic.tag('api')
    allure.dynamic.link('https://github.com', name='Main website')
    allure.dynamic.severity(Severity.MINOR)
    allure.dynamic.description('Проверка текста в репозитории')
    pass

