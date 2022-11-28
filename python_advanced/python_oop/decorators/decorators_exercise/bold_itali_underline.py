from functools import wraps


def make_bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = [func(*args, **kwargs)]
        result.insert(0, '<b>')
        result.append('</b>')

        return ''.join(result)

    return wrapper


def make_italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = [func(*args, **kwargs)]

        result.insert(1, '<i>') if result[0] == '<b>' else result.insert(0, '<i>')
        result.insert(-2, '</u>') if result[0] == '<b>' else result.append('</i>')

        return ''.join(result)

    return wrapper

def make_underline(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = [func(*args, **kwargs)]

        result.insert(2, '<u>') if result[0] == '<b>' else result.insert(0, '<u>')
        result.insert(3, '</u>') if result[0] == '<b>' else result.append('</u>')


        return ''.join(result)


    return wrapper


import unittest


class BoldItalicUnderlineTests(unittest.TestCase):
    def test_make_bold(self):
        @make_bold
        def func():
            return "pesho"

        res = func()
        self.assertEqual(res, "<b>pesho</b>")

    def test_make_italic(self):
        @make_italic
        def func(name):
            return f"Hey, {name}"

        res = func("pesho")
        self.assertEqual(res, "<i>Hey, pesho</i>")

    def test_make_underline(self):
        @make_underline
        def func(first_name, last_name):
            return f"{first_name} {last_name}"

        res = func("pesho", "peshov")
        self.assertEqual(res, "<u>pesho peshov</u>")

    def test(self):
        @make_bold
        @make_underline
        @make_italic
        def func():
            return "pesho"

        res = func()
        self.assertEqual(res, "<b><u><i>pesho</i></u></b>")


if __name__ == "__main__":
    unittest.main()
