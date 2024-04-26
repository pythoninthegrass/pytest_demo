# How to write tests with pytest

![](static/meetup_pytest_20240427.png)

---

## `whoami`

Lance Stephens

* [DevOps Engineer](https://www.linkedin.com/in/lancestephens/)
* Pretty okay Pythonista 🐍

![](static/me.JPG)

---

## Agenda

* Zoom basic tells me I have 40 minutes
  * I'll try to keep it to 30 minutes for the remote folks
* 10 minutes for Q&A

---

## Agenda CTD

* What is pytest?
* Why pytest?
* Unit tests
* Integration tests
* Mocking
* Fixtures
* Demo
* Q&A
* Sources

## What is pytest? [^1]

> The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

---

### Features

> * Detailed info on failing assert statements (no need to remember self.assert* names)
> * Auto-discovery of test modules and functions
> * Modular fixtures for managing small or parametrized long-lived test resources
> * Can run unittest (including trial) test suites out of the box
> * Rich plugin architecture, with over 1300+ external plugins and thriving community

---

## Why pytest?

* It's _very_ easy to get started
  * Barrier to entry is low compared to vanilla `unittest`
  * Supports unit tests, integration tests, and end-to-end (E2E) tests
* There's a lot of community support (11K+ stars on GitHub)
* Official [Playwright plugin](https://playwright.dev/python/docs/intro) for integration and E2E testing

---

## Wildly detailed overview by somebody else [^2]

![](static/test-pyramid.jpg)

---

## Somewhat less detailed overview for humans

![](static/pyramid-progression.png)

https://semaphoreci.com/blog/testing-pyramid

---

## Unit tests

A unit is the smallest testable part of an application. In procedural programming, a unit could be an entire module, but it is more commonly an individual function or method.

[unittest](https://docs.python.org/3/library/unittest.html) is Python's built-in testing framework.

---

## Unit tests CTD

**Exhibit A** [^4]

### unittest example

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

---

### pytest example

```python
import pytest

def test_upper():
    assert 'foo'.upper() == 'FOO'

def test_isupper():
    assert 'FOO'.isupper()
    assert not 'Foo'.isupper()

def test_split():
    s = 'hello world'
    assert s.split() == ['hello', 'world']
    # check that s.split fails when the separator is not a string
    with pytest.raises(TypeError):
        s.split(2)
```

---

### Mocking

> In object-oriented programming, a mock object is an object that simulates the behavior of a production code object in limited ways.

---

#### unittest example

**Exhibit B** [^5]
```python
from unittest.mock import MagicMock

thing = ProductionClass()
thing.method = MagicMock(return_value=3)
thing.method(3, 4, 5, key='value')                      # 3
thing.method.assert_called_with(3, 4, 5, key='value')   # (5, 4, 3)     
```

---

#### pytest example

```python
import pytest

def test_method(monkeypatch):
    thing = ProductionClass()

    def mock_method(*args, **kwargs):
        assert (args, kwargs) == ((3, 4, 5), {'key': 'value'})
        return 3

    monkeypatch.setattr(thing, 'method', mock_method)

    assert thing.method(3, 4, 5, key='value') == 3
```

---

### Fixtures

> In testing, a fixture provides a defined, reliable and consistent context for the tests. This could include environment (for example a database configured with known parameters) or content (such as a dataset).

**Exhibit C** [^7]
```python
import pytest

class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

@pytest.fixture
def my_fruit():
    return Fruit("apple")

@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]

def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket
```

---

## Integration tests

> Integration testing takes as its input modules that have been unit tested ... It occurs after unit testing and before system testing. [^8]

---

## Integration tests CTD

**Exhibit D** [^9]
```python
import unittest

class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.app = App(database='fixtures/test_basic.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 100)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer.name, "Org XYZ")
        self.assertEqual(customer.address, "10 Red Road, Reading")

class TestComplexData(unittest.TestCase):
    def setUp(self):
        # load test data
        self.app = App(database='fixtures/test_complex.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 10000)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=9999)
        self.assertEqual(customer.name, u"バナナ")
        self.assertEqual(customer.address, "10 Red Road, Akihabara, Tokyo")

if __name__ == '__main__':
    unittest.main()
```

---

## Demo

<div align="center">

[Demo Repo](https://github.com/pythoninthegrass/pytest_demo)

![](static/qr.png)

**Source Material**

[Flask Blog](https://github.com/insomnux/flaskblog)
</div>

---

## Q&A

<div align="center">

Questions?

![](static/question_blocks.png)

</div>

---

## Thank you!

[Techlahoma](https://www.techlahoma.org/)

[The Verge OKC](https://www.vergeokc.com/)

---

## Sources

[^1]: https://docs.pytest.org/en/8.1.x/
[^2]: https://www.lambdatest.com/learning-hub/integration-testing
[^3]: https://docs.python.org/3/library/unittest.html
[^4]: https://en.wikipedia.org/wiki/Unit_testing
[^5]: https://en.wikipedia.org/wiki/Mock_object
[^6]: https://docs.python.org/3/library/unittest.mock.html
[^7]: https://docs.pytest.org/en/7.1.x/explanation/fixtures.html#about-fixtures
[^8]: https://en.wikipedia.org/wiki/Integration_testing
[^9]: https://realpython.com/python-testing/#testing-data-driven-applications

---

## Further Reading

* [Full pytest documentation](https://docs.pytest.org/en/8.1.x/contents.html)
* [Real Python: Python Testing](https://realpython.com/python-testing/)
* [The Testing Pyramid: How to Structure Your Test Suite - Semaphore](https://semaphoreci.com/blog/testing-pyramid)
* [Playwright Python](https://playwright.dev/python/docs/intro)
