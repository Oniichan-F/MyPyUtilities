import os
from icrawler.builtin import GoogleImageCrawler


def main():
    options = get_options()

    input("Enter to start")
    check_dir(options['storage'])
    google_crawler = GoogleImageCrawler(storage={'root_dir': options['storage']})
    google_crawler.crawl(keyword=options['keyword'], max_num=options['max_num'])


def get_options():
    options = {}
    options['keyword'] = input("Input keyword: ")
    options['max_num'] = int(input("Input max number: "))
    options['storage'] = "outputs/" + input("Input save directory: ")
    input("Enter to start")
    
    return options


def check_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


if __name__ == "__main__":
    main()
    print("\n--- end ---")
