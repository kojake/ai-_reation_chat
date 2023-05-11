import json
#jsonからデータを読み込む
with open("Conversation_list.json", "r", encoding="utf-8") as file:
    Conversation_list = json.load(file)

print("アルゴリズム会話")
print("_______________")
print("会話を始めるなら：1")

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
            break
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