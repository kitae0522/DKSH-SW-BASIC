if __name__ == '__main__':
    def main():
        player_name = input("이적하는 선수는 누구입니까? | ")
        old_league = input(f"{player_name}은 어디 리그였습니까? | ")
        old_team = input(f"{player_name}의 팀은 어디었습니까? | ")
        new_league = input(f"{player_name}은 어디 리그로 갑니까? | ")
        new_team = input(f"{player_name}의 새로운 팀은 어디입니까? | ")
        transfer_value = input("이적료는 얼마입니까? | ")

        print()

        print("=" * 20)
        print(f"""
        Breaking News!
        오늘 {old_league}에 명문 팀 {old_team}의 {player_name} 선수가 {new_league}의 {new_team}팀으로 이적한다고 합니다.
        이적료는 {transfer_value} 유로로, {player_name} 선수는 {new_team} 팀의 중요한 자원이 될 것입니다.
        {new_team}의 감독은 "{new_team}에 {player_name}이 합류하여 기쁘다. 팬들의 기대를 받아 이번 시즌 우승을 노려보겠다."라고 했습니다.
        """)
        print("=" * 20)


    main()
