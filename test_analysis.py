import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    df = pd.read_csv("data_all.csv")

    # calculate profit versus the time took till now
    profit_list = []
    for index, row in df.iterrows():
        profit = row["current_price"] - row["initial_price"]
        profit_list.append(profit)
    
    df["profit"] = profit_list

    # profit percentage
    df["profit_percentage"] = df["profit"] / df["initial_price"]

    # time till now in days
    days_list = []
    for index, row in df.iterrows():
        days = (pd.to_datetime("2024-01-01")- pd.to_datetime(row["date"])).days
        days_list.append(days)
    
    df["days"] = days_list

    # write to csv
    df.to_csv('data_all_analysis.csv', index=False, encoding='utf-8')

    # plot graph of profit versus days for each place

    # first filter place with プライム
    plt.figure(figsize=(20,10))
    df_prime = df[df["place"].str.contains("プライム")]

    # filter place with スタンダード
    df_standard = df[df["place"].str.contains("スタンダード")]

    # fiter place with マザーズ　or グロース
    df_growth = df[df["place"].str.contains("マザーズ|グロース")]


    plt.plot(df_prime["days"], df_prime["profit"], 'o', color="red")
    plt.plot(df_standard["days"], df_standard["profit"], 'o', color="blue")
    plt.plot(df_growth["days"], df_growth["profit"], 'o', color="green")

    # y axis limit [-5000, 5000]
    plt.ylim(-5000, 5000)
    plt.title('profit versus days for each place')
    # save the graph
    plt.savefig("profit_vs_days.png")

    # plot histogram of profit on the left side of the graph
    # create new plt

    # for each 100 days plot the histogram

    profit_average_prime = []
    profit_average_standard = []
    profit_average_growth = []

    for i in range(13):
        #df_prime_100 = df_prime[df_prime["days"] < (i+1)*100 & df_prime["days"] > i*100]
        df_prime_100 = df_prime[df_prime["days"] < (i+1)*100]
        df_prime_100 = df_prime_100[df_prime_100["days"] > i*100]
        df_standard_100 = df_standard[df_standard["days"] < (i+1)*100]
        df_standard_100 = df_standard_100[df_standard_100["days"] > i*100]
        df_growth_100 = df_growth[df_growth["days"] < (i+1)*100]
        df_growth_100 = df_growth_100[df_growth_100["days"] > i*100]

        # calculate average profit for each place
        profit_average_prime.append(df_prime_100["profit"].mean())
        profit_average_standard.append(df_standard_100["profit"].mean())
        profit_average_growth.append(df_growth_100["profit"].mean())

        plt.figure(figsize=(20,10))
        plt.title(f'profit histgram for each place {i}')
        # plt x axis limit [-5000, 5000]
        plt.xlim(-5000, 5000)
        # plt y axis limit [0, 100]
        plt.ylim(0, 10)
        plt.hist(df_prime_100["profit"], bins=100, orientation='vertical', color="red", alpha=0.5)
        plt.hist(df_standard_100["profit"], bins=100, orientation='vertical', color="blue", alpha=0.5)
        plt.hist(df_growth_100["profit"], bins=100, orientation='vertical', color="green", alpha=0.5)
        plt.savefig(f"profit_hist_{i}.png")
    
    #plot average profit for each place
    plt.figure(figsize=(20,10))
    plt.title('average profit for each place')
    plt.plot(profit_average_prime, color="red")
    plt.plot(profit_average_standard, color="blue")
    plt.plot(profit_average_growth, color="green")
    plt.savefig(f"profit_average.png")


    for i in range(13):
        #df_prime_100 = df_prime[df_prime["days"] < (i+1)*100 & df_prime["days"] > i*100]
        df_prime_100 = df_prime[df_prime["days"] < (i+1)*100]
        df_prime_100 = df_prime_100[df_prime_100["days"] > i*100]
        df_standard_100 = df_standard[df_standard["days"] < (i+1)*100]
        df_standard_100 = df_standard_100[df_standard_100["days"] > i*100]
        df_growth_100 = df_growth[df_growth["days"] < (i+1)*100]
        df_growth_100 = df_growth_100[df_growth_100["days"] > i*100]

        # calculate average profit for each place
        profit_average_prime.append(df_prime_100["profit_percentage"].mean())
        profit_average_standard.append(df_standard_100["profit_percentage"].mean())
        profit_average_growth.append(df_growth_100["profit_percentage"].mean())

        plt.figure(figsize=(20,10))
        plt.title(f'profit percentage histgram for each place {i}')
        # plt x axis limit [-5000, 5000]
        plt.xlim(-3, 3)
        # plt y axis limit [0, 100]
        plt.ylim(0, 10)
        plt.hist(df_prime_100["profit_percentage"], bins=100, orientation='vertical', color="red", alpha=0.5)
        plt.hist(df_standard_100["profit_percentage"], bins=100, orientation='vertical', color="blue", alpha=0.5)
        plt.hist(df_growth_100["profit_percentage"], bins=100, orientation='vertical', color="green", alpha=0.5)
        plt.savefig(f"profit_percentage_hist_{i}.png")

    #plot average profit for each place
    plt.figure(figsize=(20,10))
    plt.title('average profit for each place')
    plt.plot(profit_average_prime, color="red")
    plt.plot(profit_average_standard, color="blue")
    plt.plot(profit_average_growth, color="green")
    plt.savefig(f"profit_percentage_average.png")