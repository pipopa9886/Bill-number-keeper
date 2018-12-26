print("1000円番号保存所へようこそ")
print("これを使えば今まで出会った1000円の番号が保存可能です")
print("いずれ見直したときに同じ番号にめぐりあえてびっくりするかもしれません")

print("どちらのモード？")
print("0:追加、1:閲覧,2:検索")
which=int(input())

if which==0:
    print("番号を入力")
    print("例:GX563636M 等")
    number=input()
    with open("1000_yen.txt","a",encoding="utf-8") as write:
        write.write("\n{}".format(number))
    print("入力完了")

elif which==1:
    print("ファイルの中身を表示します")
    print("直接 1000_yen.txt を開いても確認できます")
    print("よろしいですか")
    print("はい:y,いいえ:n")
    choose=input()
    if choose=="y" or "ｙ" or "Y":
        with open("1000_yen.txt","r",encoding="utf-8") as read:
            for i in read:
                print(i,end="")

else:
    print("未実装だよ")
