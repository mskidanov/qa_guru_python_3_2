from selene.support.shared import browser
from selene import be, have

def test_positive_google(browser_open):
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_negative_google(browser_open):
    browser.element('[name=q]').should(be.blank).type('dfkdfldlkfjdlk;gjdl;kg').press_enter()
    browser.element('[id=search]').should(have.text('По запросу dfkdfldlkfjdlk;gjdl;kg ничего не найдено.'))
