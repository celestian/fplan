"""fplan

Usage:
  fplan basic <uver> <uroky> <doba>
  fplan (-h | --help)
  fplan --version

Options:
  -h --help         Show this screen.
  --version         Show version.
"""

from docopt import docopt

from core.mortgage import Mortgage

# https://www.financevpraxi.cz/finance-hypotecni-uver
# https://is.muni.cz/th/hlx9x/Plny_text_prace.pdf
# https://www2.karlin.mff.cuni.cz/~portal/fin_mat/?page=anuita


def main():

    args = docopt(__doc__, version='0.0.1')

    if args['basic']:

        mortgage = Mortgage(int(args['<uver>']), float(args['<uroky>']), int(args['<doba>']))
        print('Splatka: {:.2f}'.format(mortgage.anuita()))


if __name__ == '__main__':
    main()
