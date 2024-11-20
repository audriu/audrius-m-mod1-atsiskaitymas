if __name__ == '__main__':
    from audrius_m_mod1_atsiskaitymas.crawler import crawl

    print(crawl(time_limit=60, source='https://httpbin.org/delay/5', return_format='html'))
