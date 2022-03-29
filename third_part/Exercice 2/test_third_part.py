from src import Exo2


def main():
    pathname = 'data/data.json.gz'
    exo2 = Exo2(pathname)
    contentFile = exo2.parse_json()
    data, columns = exo2.get_products(contentFile)
    exo2.generate_csv_file(data, columns)


if __name__ == '__main__':
    main()
