import argparse, pickle, pathlib
from .autocomplete import AutoComplete

dev_string       = 'Questions? Contact: bobbyocean@gmail.com.'
default_filepath = pathlib.Path.cwd().joinpath('autocomplete_database.pkl').resolve()


def train():

    # Argument Parsing
    parser = argparse.ArgumentParser(
        description=
        '''
        Creates an autocomplete database. If the dest database already exists, the database is appended to instead.  
        ''',
        epilog=dev_string,
    )
    parser.add_argument('-t','--text',
        help='text to train on',required=True)
    parser.add_argument('-d','--dest',
        help='the database to use (defaults to ./autocomplete_database.pkl)')
    args = parser.parse_args()

    # Main
    dest   = pathlib.Path(args.dest).resolve() if args.dest else default_filepath
    print(f'{["Creating","Appending to"][dest.exists()]} autocomplete database at {dest}...',end='')
    autodb = pickle.load(open(dest,'rb')) if dest.exists() else AutoComplete()
    autodb.train(args.text)
    pickle.dump(autodb,open(dest,'wb'))
    print(f'Done.')


def complete():

    # Argument Parsing
    parser = argparse.ArgumentParser(
        description=
        '''
        Auto completes a given string based on a trained autocomplete database. 
        ''',
        epilog=dev_string,
    )
    parser.add_argument('-t','--text',required=True,
        help='the text you wish to autocomplete')
    parser.add_argument('-d','--database',default=default_filepath,
        help='the location of the autocomplete_database to use (defaults to ./autocomplete_database.pkl)')
    parser.add_argument('-l','--limit-results',type=int,
        help='limit the number of results')
    parser.add_argument('-c','--confidence',action='store_false',
        help='include the confidence values when printing results')
    args = parser.parse_args()

    # Main
    if not args.database:
        print('This binary doesn\'t work without a trained autocomplete database to reference.')
    else:
        autodb = pickle.load(open(args.database,'rb'))
        words  = autodb.autocomplete_dict(args.text).most_common(args.limit_results)
        if args.confidence:
            print(', '.join(w for w,c in words))
        else:
            print(', '.join(f'{w} ({c})' for w,c in words))
