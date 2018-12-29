import time
import re
print("1000円番号保存所へようこそ")
print("これを使えば今まで出会った1000円の番号が保存可能です")
print("いずれ見直したときに同じ番号にめぐりあえてびっくりするかもしれません")

print("どちらのモード？")
print("0:追加、1:閲覧,2:検索")
which=int(input())

if which==0:
    while True:
        print("番号を入力")
        print("例:GX563636M 等")
        print("入力をやめたいときは何も入力せず ENTER を押してください")
        pattern=r"[A-Z]{2}[0-9]{6}[A-Z]{1}"
        number=input()
        if number=="":
            break

        else:
            with open("1000_yen.txt","r",encoding="utf-8") as se:
                line=[s.strip() for s in se.readlines()]
            if re.fullmatch(pattern,number):

                c_0=number in line
                if c_0==True:
                    print("既に番号は存在します！")

                else:
                    if re.fullmatch(pattern,number):
                        with open("1000_yen.txt","a",encoding="utf-8") as write:
                            write.write("{}\n".format(number))
                        print("入力完了\n")

            else:
                print("正しい番号かな？\n")


elif which==1:
    print("ファイルの中身を表示します")
    print("よろしいですか")
    print("はい:0,いいえ:1")
    choose=int(input())
    if choose==0:
        with open("1000_yen.txt","r",encoding="utf-8") as view:
            line=[s.strip() for s in view.readlines()]
        line.sort()
        print(line)

    else:
        pass
else:
    d=0
    while d==0:
        print("検索したい番号を入力してください。")
        b=input()
        with open("1000_yen.txt","r",encoding="utf-8") as search:
            line=[s.strip() for s in search.readlines()]

        c=b in line
        if c==True:
            print("{} は存在します！".format(b))
            time.sleep(1)
        else:
            print("その番号は存在しません")

        print("続けて検索しますか？")
        print("はい:0,いいえ:1")
        d=int(input())
