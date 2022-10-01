!pip install requests-html
from requests_html import HTMLSession
session = HTMLSession()
year = [2020, 2021, 2022]
for i in range(0, len(year)):
        url = f"https://www.dsebd.org/old_news.php?startDate={year[i]}-01-01&endDate={year[i]}-12-30&criteria=4&archive=news"
        r = session.get(url)
        dse_news = r.html.find(".table-news")[0].text
        dse_news_list = dse_news.split('\n')
        trading_code = dse_news_list[1::8]
        news_title = dse_news_list[3::8]
        news = dse_news_list[5::8]
        post_date = dse_news_list[7::8]
        trading_code, news_title, news, post_date = trading_code[:-4], news_title[:-4], news[:-4], post_date[:-3]
        with open(f"{year[i]}.txt", "w", encoding="utf-8") as f:
            f.write("News no, Trading Code, News Title, News, Post Date\n")
            for i, t_c, n_t, n, p_o in zip(range(1, len(trading_code)+1), trading_code, news_title, news, post_date):
                f.write(f"{i} : {t_c}, {n_t}, {n}, {p_o}\n")
           