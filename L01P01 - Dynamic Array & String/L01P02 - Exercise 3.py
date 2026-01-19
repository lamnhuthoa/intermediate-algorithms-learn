# Bear and Game
"""
Bear Limak likes watching sports on TV. He is going to watch a game today. The game lasts 90 minutes and there are no breaks.

Each minute can be either interesting or boring. If 15 consecutive minutes are boring then Limak immediately turns TV off.

You know that there will be n interesting minutes t1,t2,...,tn. Your task is to calculate for how many minutes Limak will watch the game.
"""

def get_number_limak_will_watch_the_game(interesting_minutes: list) -> int:
    boring_count = 0
    total_minutes_watched = 0
    for minute in range(1, 91):
        if minute in interesting_minutes:
            boring_count = 0
        else:
            boring_count += 1
        total_minutes_watched += 1
        if boring_count == 15:
            break
    return total_minutes_watched
    
n = int(input())
interesting_minutes = list(map(int, input().split()))
ans = get_number_limak_will_watch_the_game(interesting_minutes)
print(ans)