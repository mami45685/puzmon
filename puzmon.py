#インポート

#グローバル宣言

#関数宣言

def main():
    player_name=input("名前を入力してください>>")
    print("*** Puzzle & Monsters ***")
    kills = go_dungeon(player_name)
    print("*** GAME CLEAR!! ***")
    print(f"倒したモンスター数={kills}体")


def go_dungeon(player_name):
    print(f"{player_name}はダンジョンに到着した")
    print(f"{player_name}はダンジョンに制覇した")
    return 5



#main関数の呼び出し
main()

