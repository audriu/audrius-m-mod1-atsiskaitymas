if __name__ == '__main__':
    from audrius_m_mod1_atsiskaitymas.crawler import crawl

    print(crawl(time_limit=1, source='https://www.manoip.lt/', return_format='text'))
