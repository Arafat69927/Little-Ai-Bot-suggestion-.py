import random
DATA = {
    "movie": [
        ("Inception", ["thrill", "mind", "excited"]),
        ("The Pursuit of Happyness", ["sad", "motivated", "emotional"]),
        ("3 Idiots", ["happy", "funny", "motivated"]),
        ("Interstellar", ["mind", "emotional", "excited"]),
        ("The Mask", ["funny", "happy", "bored"]),
        ("Shutter Island", ["thrill", "mind", "bored"]),
    ],
    "food": [
        ("Biryani", ["happy", "excited", "hungry"]),
        ("Khichuri + Egg", ["sad", "tired", "rainy"]),
        ("Burger", ["bored", "hungry", "excited"]),
        ("Fuchka", ["happy", "bored", "funny"]),
        ("Tea + Singara", ["tired", "rainy", "sad"]),
        ("Pasta", ["happy", "hungry", "motivated"]),
    ],
    "book": [
        ("Atomic Habits", ["motivated", "bored", "tired"]),
        ("Sherlock Holmes", ["thrill", "mind", "bored"]),
        ("Himu Somogro", ["funny", "happy", "sad"]),
        ("The Alchemist", ["emotional", "motivated", "sad"]),
        ("Deep Work", ["motivated", "mind", "tired"]),
    ],
    "game": [
        ("Chess", ["mind", "bored", "thrill"]),
        ("Football (FC/eFootball)", ["excited", "happy", "funny"]),
        ("Minecraft", ["bored", "tired", "happy"]),
        ("Sudoku", ["mind", "tired", "motivated"]),
        ("Racing game", ["excited", "thrill", "bored"]),
    ],
}

MOODS = ["happy", "sad", "bored", "tired", "excited", "motivated",
         "funny", "thrill", "mind", "emotional", "hungry", "rainy"]

# Bot er "memory":
scores = {}
for category in DATA:
    for name, tags in DATA[category]:
        scores[name] = 0

def suggest(category, mood):
    """Mood match + score diye sera item khuje ber kore."""
    best = []
    best_points = -999
    for name, tags in DATA[category]:
        points = scores[name]
        if mood in tags:
            points += 5          # mood match hole beshi point
        points += random.random()  # ektu randomness
        if points > best_points:
            best_points = points
            best = name
    return best

print("=== AI SUGGESTION BOT ===")
print("I CAN SUGGEST YOU MOVIE, FOOD, BOOK AND GAME.\n")


while True:
    print("Category:", ", ".join (DATA.keys()),"| (IF YOU WANT TO GO OUT (QUIT)")
    categorys = input("Which suggestion do you want? ").strip().lower()

    if categorys == "quit":
        break
    if categorys not in DATA:
        print("This category isn't available.Try again 🥲\n")
        continue

    print("Mood options:", ", ".join(MOODS))
    mood = input("What's your mood/wishes? ").strip().lower()
    if mood not in MOODS:
        print("I couldn't quite identify the intended mood, so I had to make a random guess..")
        mood = ""

    # Ekta suggestion er jonno chhoto loop: "na" bolle abar suggest korbe
    tries = 0
    while tries < 3:
        pick = suggest(categorys, mood)
        print(f"\n My suggestion: {pick}")
        answer = input("Do you like it? (y/n): ").strip().lower()

        if answer == "y":
            scores[pick] += 2    # pochondo holo, score barlo
            print("Amazing😁. Do it enjoy \n ")
            break
        else:
            scores[pick] -= 3    # pochondo hoy ni, score kombe
            tries += 1
            print("ok, let's see another one...")
    else:
        print("\nI TRIED THREE TIMES, HOPEFULLY, IT HAS ANOTHER STEP\n")

    again = input("Do your need more suggestion? (y/n): ").strip().lower()

    if again != "y":
        running = False

print("THANKS.")