from unittest import TestCase
from utils.heredoc import heredoc, single_line


class TestUtilsHeredocHeredoc(TestCase):
    def test_empty_string_stays_the_same(self) -> None:
        self.assertEqual(heredoc(''), '')

    def test_single_line_is_trimmed(self) -> None:
        self.assertEqual(
            heredoc(' Hello, dear friends!\n'),
            'Hello, dear friends!'
        )

    def test_multiline_trims_least_number_of_leading_spaces(self) -> None:
        self.assertEqual(
            heredoc('''
                Oh wow!
                  banana

                 It's nice!
                    So…
            '''),

            '\n'.join((
                'Oh wow!',
                '  banana',
                '',
                " It's nice!",
                '    So…',
            ))
        )


class TestUtilsHeredocSingleLine(TestCase):
    def test_empty_string_stays_the_same(self) -> None:
        self.assertEqual(single_line(''), '')

    def test_single_line_is_trimmed(self) -> None:
        self.assertEqual(single_line(' How nice! \n'), 'How nice!')

    def test_multiline_is_converted_to_single_line(self) -> None:
        self.assertEqual(
            single_line('''
                Oh wow!
                  banana

                 It's nice!
                    So…
            '''),

            "Oh wow! banana It's nice! So…"
        )
