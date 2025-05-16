
import argparse
from build import handle_build
from buy import handle_buy
from sell import handle_sell
from listings import handle_list

def main():
    parser = argparse.ArgumentParser(prog="licensechain", description="LicenseChain CLI")
    subparsers = parser.add_subparsers(dest="command")

    # build
    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("--repo", required=True)
    build_parser.add_argument("--spec", required=True)

    # buy
    buy_parser = subparsers.add_parser("buy")
    buy_parser.add_argument("res_id")
    buy_parser.add_argument("--max-price", type=int, required=True)

    # sell
    sell_parser = subparsers.add_parser("sell")
    sell_parser.add_argument("res_id")
    sell_parser.add_argument("--min-price", type=int, required=True)

    # list
    subparsers.add_parser("list")

    args = parser.parse_args()
    if args.command == "build":
        handle_build(args.repo, args.spec)
    elif args.command == "buy":
        handle_buy(args.res_id, args.max_price)
    elif args.command == "sell":
        handle_sell(args.res_id, args.min_price)
    elif args.command == "list":
        handle_list()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
