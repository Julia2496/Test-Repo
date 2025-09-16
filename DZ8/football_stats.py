football_stats = {
    "Команд сыграло": 48,
    "Завершился": True,
    "Страна проведения": "Катар"
}

teams_count = football_stats.get("Команд сыграло")  # 1-й способ
print(teams_count)  # 48

teams_count = football_stats["Команд сыграло"]  # 2-й способ
print(teams_count)  # 48

football_stats = {
    "Команд сыграло": 48,
    "Завершился": True,
    "Страна проведения": "Катар"
}
football_stats["Команд сыграло"] = 50  # Перезаписали существующее значение
football_stats["Победитель"] = "Аргентина"  # Добавили новое значение

teams_count = football_stats["Команд сыграло"]
print(teams_count)  # 50

winner = football_stats["Победитель"]
print(winner)  # Аргентина

football_stats = {
    "Участники": ["Австралия", "Англия", "Аргентина", "Бельгия",
                  "еще 42 страны", "Эквадор", "Япония"],
    "Награды": {"Золотой мяч": "Лионель Месси",
                "Больше всего голов": {"Игрок": "Килиан Мбаппе - капитан команды",
                                       "Количество мячей": 8
                                       },
                }
}

england = football_stats["Участники"][1]
print(england)  # Англия

goals_leader = football_stats["Награды"]["Больше всего голов"]["Игрок"]
max_goals = football_stats["Награды"]["Больше всего голов"]["Количество мячей"]
print(goals_leader)  # Килиан Мбаппе - капитан команды
print(max_goals)  # 8

football_stats = {
    "Команд сыграло": 48,
    "Завершился": True,
    "Страна проведения": "Катар"
}

length = len(football_stats)
print(length)  # 3
