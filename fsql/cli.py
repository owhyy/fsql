import argparse

from .main import SQLFaker


def cli():
    usage_str = """
    fsql Person name 10 -o insert.sql en_EN
    fsql Person first_name last_name age:[10:60] 3 -c
    fsql Teacher foo:first_name married:bool 15 -n
    fsql City city 'climate:[cold, mild, hot]' 10 -i city_id
    """

    parser = argparse.ArgumentParser(
        description="Generate a SQL insert statement", usage=usage_str
    )

    parser.add_argument(
        "Name",
        nargs=1,
        metavar="table name",
        type=str,
        help="the name of the table",
    )
    parser.add_argument(
        "Values", nargs="+", metavar="values", type=str, help="the values to generate"
    )
    parser.add_argument(
        "Count",
        metavar="count",
        type=int,
        help="how many rows to generate",
        nargs=1,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="save output to file",
        metavar="FILENAME",
        nargs=1,
        type=str,
        required=False,
    )
    parser.add_argument(
        "-c",
        "--copy",
        help="save output to clipboard",
        action="store_true",
        required=False,
    )
    parser.add_argument(
        "-n",
        "--noid",
        help="don't generate ids for the inserts",
        action="store_false",
        required=False,
    )
    parser.add_argument(
        "-i",
        "--idname",
        help="specify the name of the field to be used as id",
        metavar="NAME",
        nargs=1,
        type=str,
        required=False,
    )
    parser.add_argument(
        "-l",
        "--locale",
        help="specify the locale (ro_RO) is default",
        metavar="LOCALE",
        nargs=1,
        type=str,
        required=False,
    )

    args = parser.parse_args()

    id_field_name = None
    if args.noid and args.idname:
        id_field_name = args.idname[0]

    fakesql = SQLFaker(
        args.Name[0],
        args.Values,
        args.Count[0],
        generate_ids=args.noid,
        id_field_name=id_field_name,
        locale=args.locale[0] if args.locale else None,
    )

    if args.copy:
        fakesql.copy()
    elif args.output:
        fakesql.write(args.output[0])
    else:
        fakesql.print()
