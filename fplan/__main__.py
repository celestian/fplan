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

# https://www.financevpraxi.cz/finance-hypotecni-uver
# https://is.muni.cz/th/hlx9x/Plny_text_prace.pdf
# https://www2.karlin.mff.cuni.cz/~portal/fin_mat/?page=anuita


def main():

    args = docopt(__doc__, version='0.0.1')

    if args['basic']:

        vyska_uveru = float(args['<uver>'])
        uroky = float(args['<uroky>'])
        doba = float(args['<doba>'])

        splatka= vyska_uveru * (uroky / (1.0 - pow((1/(1+uroky )), doba)) )
        print(splatka/12.0)

if __name__ == '__main__':
    main()
