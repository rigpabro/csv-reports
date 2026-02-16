from csv_reports.cli import parse_args
from csv_reports.formatter import print_report
from csv_reports.reader import read_csv_files
from csv_reports.reports import registry


def main() -> None:
    args = parse_args()
    data = read_csv_files(args.files)
    report = registry.get_report(args.report)
    rows = report.generate(data)
    print_report(report.headers, rows)


if __name__ == "__main__":
    main()
