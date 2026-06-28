import keyboard, time, os, random, sys
mode = input("What game mode do you want?(speed/normal/unlimited/slow): ")
time.sleep(3)
if mode == "normal":
    width = 20
    apples = 0
    lives = 10
    player_pos = random.randint(0, width-1)
    speed = 0.05

    items = ["🍎", "🍌", "🍇", "💣", "🪙", "🍎", "🍌", "🍇", "💣"]
    caught_items = []

    while lives > 0:
        item = random.choice(items)
        n1 = random.randint(0, width-1)
        n3 = random.randint(15, 40)
        original_speed = speed

        while n3 > 0:
            sys.stdout.write("\033[H\033[J")
            attack = " " * n1 + item + " " * (width - n1 - 1)
            space = "\n" * n3
            player = " " * player_pos + "🧺" + " " * (width - player_pos - 1)

            print(f"Score: {apples} | Lives: {lives}")
            print(attack)
            print(space)
            print(player)

            if keyboard.is_pressed("left") or keyboard.is_pressed("a"):
                if player_pos > 0:
                    player_pos -= 1
            elif keyboard.is_pressed("right") or keyboard.is_pressed("d"):
                if player_pos < width-1:
                    player_pos += 1

            time.sleep(speed)
            n3 -= 1

        # ✅ catch/miss check with tolerance
        if abs(n1 - player_pos) <= 1:   # allow ±1 column tolerance
            if item == "🍎":
                apples += 1
                caught_items.append("Apple 🍎")
                print("\033[92mYou caught an apple! 🍎\033[0m")
            elif item == "🍌":
                apples += 2
                caught_items.append("Banana 🍌")
                print("\033[93mBanana bonus! 🍌\033[0m")
            elif item == "🍇":
                apples += 1
                caught_items.append("Grapes 🍇")
                speed = 0.2
                print("\033[95mGrapes power-up! 🍇\033[0m")
            elif item == "💣":
                apples -= 1
                lives -= 2
                caught_items.append("Bomb 💣")
                print("\033[97mBomb caught! 💣\033[0m")
            elif item == "🪙":
                apples += 1
                lives += 2
                caught_items.append("Gold Coin 🪙")
                print("\033[93mGold coin found! +Lives! 🪙\033[0m")
        else:
            if item != "💣":
                lives -= 1
                print("\033[91mMissed!\033[0m")

        speed = original_speed

        if apples % 5 == 0 and apples > 0:
            speed = max(0.05, speed - 0.01)

        if apples % 10 == 0 and apples > 0:
            lives += 1
            print("\033[96mBonus life awarded! 💖\033[0m")

        time.sleep(1)

    sys.stdout.write("\033[H\033[J")
    print(f"Game Over! Final Score: {apples}")

    if caught_items:
        print("You caught:")
        for item in caught_items:
            print(f"- {item}")
    else:
        print("You caught nothing!")
elif mode == "speed":
 

    width = 20
    apples = 0
    lives = 10
    player_pos = random.randint(0, width-1)
    speed = 0.02

    items = ["🍎", "🍌", "🍇", "💣", "🪙", "🍎", "🍌", "🍇", "💣"]
    caught_items = []

    while lives > 0:
        item = random.choice(items)
        n1 = random.randint(0, width-1)
        n3 = random.randint(15, 40)
        original_speed = speed

        while n3 > 0:
            sys.stdout.write("\033[H\033[J")
            attack = " " * n1 + item + " " * (width - n1 - 1)
            space = "\n" * n3
            player = " " * player_pos + "🧺" + " " * (width - player_pos - 1)

            print(f"Score: {apples} | Lives: {lives}")
            print(attack)
            print(space)
            print(player)

            if keyboard.is_pressed("left") or keyboard.is_pressed("a"):
                if player_pos > 0:
                    player_pos -= 1
            elif keyboard.is_pressed("right") or keyboard.is_pressed("d"):
                if player_pos < width-1:
                    player_pos += 1

            time.sleep(speed)
            n3 -= 1

        # ✅ catch/miss check with tolerance
        if abs(n1 - player_pos) <= 1:   # allow ±1 column tolerance
            if item == "🍎":
                apples += 1
                caught_items.append("Apple 🍎")
                print("\033[92mYou caught an apple! 🍎\033[0m")
            elif item == "🍌":
                apples += 2
                caught_items.append("Banana 🍌")
                print("\033[93mBanana bonus! 🍌\033[0m")
            elif item == "🍇":
                apples += 1
                caught_items.append("Grapes 🍇")
                print("\033[95mGrapes power-up! 🍇\033[0m")
            elif item == "💣":
                apples -= 1
                lives -= 2
                caught_items.append("Bomb 💣")
                print("\033[97mBomb caught! 💣\033[0m")
            elif item == "🪙":
                apples += 1
                lives += 2
                caught_items.append("Gold Coin 🪙")
                print("\033[93mGold coin found! +Lives! 🪙\033[0m")
        else:
            if item != "💣":
                lives -= 1
                print("\033[91mMissed!\033[0m")

        speed = original_speed

        if apples % 5 == 0 and apples > 0:
            speed = max(0.05, speed - 0.01)

        if apples % 10 == 0 and apples > 0:
            lives += 1
            print("\033[96mBonus life awarded! 💖\033[0m")

        time.sleep(1)

    sys.stdout.write("\033[H\033[J")
    print(f"Game Over! Final Score: {apples}")

    if caught_items:
        print("You caught:")
        for item in caught_items:
            print(f"- {item}")
    else:
        print("You caught nothing!")

elif mode == "unlimited":


    width = 20
    apples = 0
    player_pos = random.randint(0, width-1)
    speed = 0.05

    items = ["🍎", "🍌", "🍇", "💣", "🪙", "🍎", "🍌", "🍇", "💣"]
    caught_items = []

    while True:
        item = random.choice(items)
        n1 = random.randint(0, width-1)
        n3 = random.randint(15, 40)
        original_speed = speed

        while n3 > 0:
            sys.stdout.write("\033[H\033[J")
            attack = " " * n1 + item + " " * (width - n1 - 1)
            space = "\n" * n3
            player = " " * player_pos + "🧺" + " " * (width - player_pos - 1)

            print(f"Score: {apples} ")
            print(attack)
            print(space)
            print(player)

            if keyboard.is_pressed("left") or keyboard.is_pressed("a"):
                if player_pos > 0:
                    player_pos -= 1
            elif keyboard.is_pressed("right") or keyboard.is_pressed("d"):
                if player_pos < width-1:
                    player_pos += 1

            time.sleep(speed)
            n3 -= 1

        # ✅ catch/miss check with tolerance
        if abs(n1 - player_pos) <= 1:   # allow ±1 column tolerance
            if item == "🍎":
                apples += 1
                caught_items.append("Apple 🍎")
                print("\033[92mYou caught an apple! 🍎\033[0m")
            elif item == "🍌":
                apples += 2
                caught_items.append("Banana 🍌")
                print("\033[93mBanana bonus! 🍌\033[0m")
            elif item == "🍇":
                apples += 1
                caught_items.append("Grapes 🍇")
                speed = 0.2
                print("\033[95mGrapes power-up! 🍇\033[0m")
            elif item == "💣":
                apples -= 1
           
                caught_items.append("Bomb 💣")
                print("\033[97mBomb caught! 💣\033[0m")
            elif item == "🪙":
                apples += 1
            
                caught_items.append("Gold Coin 🪙")
                print("\033[93mGold coin found! +Lives! 🪙\033[0m")
        else:
            if item != "💣":
          
                print("\033[91mMissed!\033[0m")

        speed = original_speed

        if apples % 5 == 0 and apples > 0:
            speed = max(0.05, speed - 0.01)

        if apples % 10 == 0 and apples > 0:

            print("\033[96mBonus life awarded! 💖\033[0m")

        time.sleep(1)

        sys.stdout.write("\033[H\033[J")
        print(f"Game Over! Final Score: {apples}")

        if caught_items:
            print("You caught:")
            for item in caught_items:
                print(f"- {item}")
        else:
            print("You caught nothing!")
elif mode == "slow":
    import keyboard, time, os, random, sys

width = 20
apples = 0
lives = 10
player_pos = random.randint(0, width-1)
speed = 0.2

items = ["🍎", "🍌", "🍇", "💣", "🪙", "🍎", "🍌", "🍇", "💣"]
caught_items = []

while lives > 0:
    item = random.choice(items)
    n1 = random.randint(0, width-1)
    n3 = random.randint(15, 40)
    original_speed = speed

    while n3 > 0:
        sys.stdout.write("\033[H\033[J")
        attack = " " * n1 + item + " " * (width - n1 - 1)
        space = "\n" * n3
        player = " " * player_pos + "🧺" + " " * (width - player_pos - 1)

        print(f"Score: {apples} | Lives: {lives}")
        print(attack)
        print(space)
        print(player)

        if keyboard.is_pressed("left") or keyboard.is_pressed("a"):
            if player_pos > 0:
                player_pos -= 1
        elif keyboard.is_pressed("right") or keyboard.is_pressed("d"):
            if player_pos < width-1:
                player_pos += 1

        time.sleep(speed)
        n3 -= 1

    # ✅ catch/miss check with tolerance
    if abs(n1 - player_pos) <= 1:   # allow ±1 column tolerance
        if item == "🍎":
            apples += 1
            caught_items.append("Apple 🍎")
            print("\033[92mYou caught an apple! 🍎\033[0m")
        elif item == "🍌":
            apples += 2
            caught_items.append("Banana 🍌")
            print("\033[93mBanana bonus! 🍌\033[0m")
        elif item == "🍇":
            apples += 1
            caught_items.append("Grapes 🍇")
            speed = 0.2
            print("\033[95mGrapes power-up! 🍇\033[0m")
        elif item == "💣":
            apples -= 1
            lives -= 2
            caught_items.append("Bomb 💣")
            print("\033[97mBomb caught! 💣\033[0m")
        elif item == "🪙":
            apples += 1
            lives += 2
            caught_items.append("Gold Coin 🪙")
            print("\033[93mGold coin found! +Lives! 🪙\033[0m")
    else:
        if item != "💣":
            lives -= 1
            print("\033[91mMissed!\033[0m")

    speed = original_speed

    if apples % 5 == 0 and apples > 0:
        speed = max(0.05, speed - 0.01)

    if apples % 10 == 0 and apples > 0:
        lives += 1
        print("\033[96mBonus life awarded! 💖\033[0m")

    time.sleep(1)

sys.stdout.write("\033[H\033[J")
print(f"Game Over! Final Score: {apples}")

if caught_items:
    print("You caught:")
    for item in caught_items:
        print(f"- {item}")
else:
    print("You caught nothing!")
