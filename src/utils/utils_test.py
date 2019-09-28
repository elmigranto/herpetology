from unittest import TestCase
from contextlib import redirect_stdout
from io import StringIO
from pprint import pformat
from . import heredoc, single_line, pp


class TestUtilsHeredocHeredoc(TestCase):
    def test_it_keeps_empty_strings_empty(self) -> None:
        self.assertEqual(heredoc(''), '')

    def test_it_trims_the_result(self) -> None:
        self.assertEqual(
            heredoc(' Hello, dear friends!\n'),
            'Hello, dear friends!'
        )

    def test_it_dedents_common_leading_whitespace(self) -> None:
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

    def test_it_ignores_empty_lines_on_both_ends(self):
        self.assertEqual(
            heredoc('''


                all above

                not middle ones

                all below


            '''),
            'all above\n\nnot middle ones\n\nall below'
        )


class TestUtilsHeredocSingleLine(TestCase):
    def test_it_keeps_empty_strings_empty(self) -> None:
        self.assertEqual(single_line(''), '')

    def test_it_trims_the_result(self) -> None:
        self.assertEqual(single_line(' How nice! \n'), 'How nice!')

    def test_it_multiline_becomes_single_line(self):
        self.assertEqual(
            single_line('''
                Hello, dear friend!
                How are you doing?
                Hope all is well.
            '''),
            'Hello, dear friend! How are you doing? Hope all is well.'
        )

    def test_it_replace_multiple_newlines_with_one_space(self) -> None:
        self.assertEqual(
            single_line('''
                Inline\t\tmultispace:  <-- is kept.


                But multiple empty lines like above
                  and this indent to the left
                   are collapsed
                    into one!
            '''),

            ' '.join([
                'Inline\t\tmultispace:  <-- is kept.',
                'But multiple empty lines like above',
                'and this indent to the left',
                'are collapsed into one!'
            ]),
        )


class PpTest(TestCase):
    def test_it_prints_pformat_of_the_value(self):
        with StringIO() as stream, redirect_stdout(stream):
            pp(self)
            self.assertEqual(stream.getvalue(), f'{pformat(self)}\n')

    def test_it_returns_a_value(self):
        with open('/dev/null', 'w') as stream, redirect_stdout(stream):
            self.assertEqual(pp(stream), stream)
