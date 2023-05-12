import json
import requests
from bs4 import BeautifulSoup

def open_View():
    # JSONからデータを読み込む
    with open("Conversation_list.json", "r", encoding="utf-8") as file:
        Conversation_list = json.load(file)

    print("アルゴリズム会話")
    print("_______________")
    print("会話を始めるなら：1")
    print("アルゴリズムを削除する：2")
    print("終わりたい場合は：3")

    waiting_for_choices = input("番号を入力して下さい ==>")

    if waiting_for_choices == "1":
        print("😃：こんにちは！")
        print("😃：会話を始めましょう")
        print("__________________")
        print("「天気は何」と返信今日の天気を言ってくれる")
        print("会話を終わらせたいなら：2")
        print("------------------")
        while True:
            Waiting_for_conversation_reply = input("返信 ==>")
            #会話を終わらせるかを確認する
            if Waiting_for_conversation_reply == "2":
                print("😃：また話そうね")
                open_View()
                break
            if Waiting_for_conversation_reply == "天気は何":

                weather = 0

                # スクレイピング対象のURL
                url_base = "https://tenki.jp/forecast/weathe/"

                # 県名を入力する
                prefecture = input("県名を入力してください: ")

                if url_base == "札幌":
                    weather = 1
                elif url_base == "仙台":
                    weather = 2
                elif url_base == "東京":
                    weather = 3
                elif url_base == "新潟" or url_base == "金沢":
                    weather = 4
                elif url_base == "名古屋":
                    weather = 5
                elif url_base == "大阪":
                    weather = 6
                elif url_base == "広島":
                    weather = 7
                elif url_base == "高知":
                    url_base = 8
                elif url_base == "福岡" or url_base == "鹿児島":
                    url_base = 9
                elif url_base == "那覇":
                    url_base = 10

                # URLにリクエストを送信してHTMLを取得する
                url = url_base.format(prefecture)
                res = requests.get(url)
                html = res.content

                # BeautifulSoupを使ってHTMLを解析する
                soup = BeautifulSoup(html, "html.parser")

                # 天気情報を取得する
                weather = soup.find(class_="weather-telop").get_text()
                print(prefecture + "の天気はです。".format(prefecture, weather))
                
            #アルゴリズムに回答する情報が入っているかを確認する
            if Conversation_list:
                for item in Conversation_list.items():
                    if item[0] == Waiting_for_conversation_reply:
                        print("😃：" + item[1])
                        break
                else:
                    print("アルゴリズムはこの言葉を理解していません")
                    print("学習させましょう")
                    Content_you_want_to_reply_to = input("なんて返信させたいですか？ ==>")
                    Conversation_list[Waiting_for_conversation_reply] = Content_you_want_to_reply_to
                    #jsonファイルに追加し保存する
                    with open("Conversation_list.json", "w", encoding="utf-8") as file:
                        json.dump(Conversation_list, file)
            else:
                print("アルゴリズムはこの言葉を理解していません")
                print("学習させましょう")
                Content_you_want_to_reply_to = input("なんて返信させたいですか？ ==>")
                Conversation_list[Waiting_for_conversation_reply] = Content_you_want_to_reply_to
    elif waiting_for_choices == "2":
        print("________________!dangerzone!________________")
        print("アルゴリズムを削除してしまいますと元に戻せません")
        print("終わる場合は「exit」と入力して下さい")
        print("____________________________________________")
        print("あなたが学習させたアルゴリズムリストです")
        for item in Conversation_list.items():
            print("返信" + item[0] + "回答" + item[1])
            Waiting_for_delete_selection = input("このアルゴリズムは削除しますか y/n ==>")

            if Waiting_for_delete_selection == "y":
                print("_______________________________")
                print("選択されたアルゴリズム")
                print("返信" + item[0] + "回答" + item[1])
                print("-------------------------------")
                Final_confirmation_of_deletion = input("本当に削除しますか?この操作は取り消せません y/n ==>")
                if Final_confirmation_of_deletion == "y":
                    with open("Conversation_list.json", "r", encoding="utf-8") as file:
                        Conversation_list = json.load(file)
                    del Conversation_list[item[0]]
                    with open("Conversation_list.json", "w", encoding="utf-8") as file:
                        json.dump(Conversation_list, file)

                    #無事に削除できたことを伝える
                    print("削除しました")
            else:
                continue
        print("アルゴリズムはここで終わっています")
        print("最初の画面に戻る場合は1")
        print("画面を閉じる場合は2")
        end_or_continue = input("選択して下さい ==>")

        if end_or_continue == "1":
            open_View()
        elif end_or_continue == "2":
            exit()
        else:
            print("予期せぬ答えが帰ってきましたので強制終了しました")
            exit()
    elif waiting_for_choices == "3":
        exit()
    else:
        print("予期せぬ答えが帰ってきましたので強制終了しました")

open_View()