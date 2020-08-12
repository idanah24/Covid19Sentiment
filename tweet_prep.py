import pandas as pd
import numpy as np
import twint
from datetime import date, timedelta
# V1
# def sample_influencers_tweets(accounts, keywords, dates, output):
#     for user in accounts:
#         config = twint.Config()
#         print("[INFO] Reading tweets from " + user)
#         config.Username = user
#         config.Limit = 100
#         config.Lang = "en"
#         config.Store_csv = True
#         config.Output = output
#
#         for d in dates:
#             print("[INFO] Sampling for day: {0}".format(d))
#             day = d + ' 08:00:00'
#             next_day = d.split('-')
#             next_day = date(int(next_day[0]), int(next_day[1]), int(next_day[2])) + timedelta(days=1)
#             next_day = str(next_day) + ' 00:00:00'
#             config.Since = day
#             config.Until = next_day
#             for key in keywords:
#                 print("[INFO] Searching for keyword: " + key)
#                 config.Search = key
#                 twint.run.Search(config)
#
#         print("[INFO] Done sampling " + user)




def sample_influencers_tweets(accounts, keywords, dates, output):
    config = twint.Config()


    # for d in dates:
    #     print("[INFO] Sampling for day: {0}".format(d))
    #     day = d + ' 08:00:00'
    #     next_day = d.split('-')
    #     next_day = date(int(next_day[0]), int(next_day[1]), int(next_day[2])) + timedelta(days=1)
    #     next_day = str(next_day) + ' 00:00:00'
    #     config.Since = day
    #     config.Until = next_day
    for user in accounts:
        print("[INFO] Reading tweets from " + user)
        config.Username = user
        config.Limit = 100
        config.Lang = "en"
        config.Store_csv = True
        config.Output = output

        for key in keywords:
            print("[INFO] Searching for keyword: " + key)
            config.Search = key
            twint.run.Search(config)

        print("[INFO] Done sampling " + user)


def sample_pop_tweets(keywords, dates):
    config = twint.Config()
    config.Limit = 100
    config.Lang = "en"
    config.Store_csv = True
    config.Output = "uk_pop_tweets.csv"
    config.Near = "United Kingdom"

    for d in dates:
        print("[INFO] Sampling for day: {0}".format(d))
        day = d + ' 08:00:00'
        next_day = d.split('-')
        next_day = date(int(next_day[0]), int(next_day[1]), int(next_day[2])) + timedelta(days=1)
        next_day = str(next_day) + ' 00:00:00'
        config.Since = day
        config.Until = next_day
        for key in keywords:
            print("[INFO] Searching for keyword: " + key)
            config.Search = key
            twint.run.Search(config)

        print("[INFO] Done sampling for day: {0}".format(d))




usa_accounts = ["@BarackObama", "@katyperry", "@taylorswift13", "@ladygaga", "@realDonaldTrump",
            "@TheEllenShow", "@ArianaGrande", "	@KimKardashian", "@jtimberlake", "@selenagomez"]

canada_accounts = ["@Drake", "@elonmusk", "@ShawnMendes", "@AvrilLavigne", "@theweeknd",
                   "@carlyraejepsen", "@Sethrogen", "@ninadobrev", "@laurDIY", "@JustinTrudeau"]


australia_accounts = ["@RealHughJackman", "@5SOS", "@Luke5SOS", "@Michael5SOS", "@troyesivan",
                      "@Calum5SOS", "@CodySimpson", "@chrishemsworth", "@Ashton5SOS", "@MirandaKerr",
                      "@ScottMorrisonMP"]


uk_accounts = ["@BBCBreaking", "@Harry_Styles", "@Louis_Tomlinson", "@LiamPayne", "@onedirection", "@EmmaWatson",
               "@zaynmalik", "@BBCWorld", "@Adele", "@coldplay"]


corona_keywords = ["coronavirus", "covid19", "covid-19", "Covid-19",
            "Covid19", "Coronavirus", "COVID19", "COVID_19", "COVID2019"] #, "corona"




dates = pd.read_csv('owid-covid-data.csv')
usa_dates = list(dates[dates['location'] == 'United States']['date'].unique())
uk_dates = list(dates[dates['location'] == 'United Kingdom']['date'].unique())
australia_dates = list(dates[dates['location'] == 'Australia']['date'].unique())
canada_dates = list(dates[dates['location'] == 'Canada']['date'].unique())


sample_influencers_tweets(accounts=usa_accounts, keywords=corona_keywords, dates=usa_dates, output='usa_inf_tweets1.csv')
sample_influencers_tweets(accounts=uk_accounts, keywords=corona_keywords, dates=uk_dates, output='uk_inf_tweets1.csv')
sample_influencers_tweets(accounts=australia_accounts, keywords=corona_keywords, dates=australia_dates, output='australia_inf_tweets1.csv')
sample_influencers_tweets(accounts=canada_accounts, keywords=corona_keywords, dates=canada_dates, output='canada_inf_tweets1.csv')

# sample_pop_tweets(corona_keywords, dates)













