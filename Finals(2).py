import tkinter as tk
import random
from PIL import Image, ImageTk, ImageDraw

import pygame
from tkinter import messagebox
from tkinter import font



# --- Initialize sounds ---
pygame.mixer.init()

pygame.mixer.music.load(
    r"sounds for project\boba-date-cute-background-music-royalty_Media_kj1MDJXJ7-I_007_48k.mp3"
)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

correct_sound = pygame.mixer.Sound(
    r"sounds for project\AudioCutter_Correct Sound Effect.mp3")
wrong_sound = pygame.mixer.Sound(
    r"sounds for project\AudioCutter_Wrong Answer Sound effect.mp3")

# --- Fruits data ---
fruits_with_hints = {

    # EASY
    "apple": {"hint": "a p _ l _", "image": "Fruits/apple.jpg"},
    "banana": {"hint": "b _ n a _ a", "image": "Fruits/banana.jpg"},
    "orange": {"hint": "o r _ n _ e", "image": "Fruits/orange.jpg"},
    "mango": {"hint": "m _ n g _", "image": "Fruits/mango.jpg"},
    "pineapple": {"hint": "p _ n e a _ _ e", "image": "Fruits/pineapple.jpg"},
    "watermelon": {"hint": "w a _ e r m _ l _ n", "image": "Fruits/watermelon.jpg"},
    "grapes": {"hint": "g r _ p _ s", "image": "Fruits/grapes.jpg"},
    "strawberry": {"hint": "s t r _ w b _ r r _", "image": "Fruits/strawberry.jpg"},
    "lemon": {"hint": "l _ m o _", "image": "Fruits/lemon.jpg"},
    "papaya": {"hint": "p _ p a y _", "image": "Fruits/papaya.jpg"},
    "guava": {"hint": "g _ a v _", "image": "Fruits/guava.jpg"},
    "pear": {"hint": "p _ _ r", "image": "Fruits/pear.jpg"},
    "melon": {"hint": "m _ l _ n", "image": "Fruits/melon.jpg"},
    "blueberry": {"hint": "b _ u e _ e r r _", "image": "Fruits/blueberry.jpg"},
    "cherry": {"hint": "c h _ r r _", "image": "Fruits/cherry.jpg"},
    "coconut": {"hint": "c _ c _ n u _", "image": "Fruits/coconut.jpg"},
    "kiwi": {"hint": "k _ _ i", "image": "Fruits/kiwi.jpg"},
    "tomato": {"hint": "t _ m _ t _", "image": "Fruits/tomato.jpg"},
    "peach": {"hint": "p _ a _ h", "image": "Fruits/peach.jpg"},
    "plum": {"hint": "p _ u _", "image": "Fruits/plum.jpg"},
    "blackberry": {"hint": "b l _ c k b _ r r _", "image": "Fruits/blackberry.jpg"},
"raspberry": {"hint": "r a s _ b _ r r _", "image": "Fruits/raspberry.jpg"},
"avocado": {"hint": "a v _ c _ d _", "image": "Fruits/avocado.jpg"},
"lime": {"hint": "l _ m _", "image": "Fruits/lime.jpg"},
"cranberry": {"hint": "c r _ n b _ r r _", "image": "Fruits/cranberry.jpg"},
"orange melon": {"hint": "o r _ n g _  m _ l _ n", "image": "Fruits/orangemelon.jpg"},
"apricot": {"hint": "a p _ _ c _ t", "image": "Fruits/apricot.jpg"},
"pineberry": {"hint": "p _ n _ b _ r r _", "image": "Fruits/pineberry.jpg"},
"star apple": {"hint": "s t _ r  a p _ l _", "image": "Fruits/starapple.jpg"},
"honeydew": {"hint": "h _ n _ _ d _ w", "image": "Fruits/honeydew.jpg"},

    # MEDIUM
    "rambutan": {"hint": "r a _ _ u t _ n", "image": "Fruits/rambutan.jpg"},
    "lychee": {"hint": "l _ c h _ _", "image": "Fruits/lychee.jpg"},
    "dragonfruit": {"hint": "d r _ g _ n  f r _ _ t", "image": "Fruits/dragonfruit.jpg"},
    "passionfruit": {"hint": "p a _ _ i _ n  f r _ _ t", "image": "Fruits/passionfruit.jpg"},
    "starfruit": {"hint": "s t _ r f r _ _ t", "image": "Fruits/starfruit.jpg"},
    "pomegranate": {"hint": "p _ m _ g r _ n _ t _", "image": "Fruits/pomegranate.jpg"},
    "persimmon": {"hint": "p _ r s _ m m _ n", "image": "Fruits/persimmon.jpg"},
    "tamarind": {"hint": "t _ m a r _ n _", "image": "Fruits/tamarind.jpg"},
    "mulberry": {"hint": "m _ l b _ r r _", "image": "Fruits/mulberry.jpg"},
    "sapodilla": {"hint": "s _ p _ d _ l l _", "image": "Fruits/sapodilla.jpg"},
    "pomelo": {"hint": "p _ m _ l _", "image": "Fruits/pomelo.jpg"},
    "longan": {"hint": "l _ n g _ n", "image": "Fruits/longan.jpg"},
    "durian": {"hint": "d _ r _ _ n", "image": "Fruits/durian.jpg"},
    "fig": {"hint": "f _ _", "image": "Fruits/fig.jpg"},
    "jujube": {"hint": "j _ j _ _ e", "image": "Fruits/jujube.jpg"},
    "gooseberry": {"hint": "g _ _ s e b e r r _", "image": "Fruits/gooseberry.jpg"},
    "cucumber melon": {"hint": "c _ c u m _ _  m _ l _ n", "image": "Fruits/cucumbermelon.jpg"},
    "rose apple": {"hint": "r _ s _  a p p _ _", "image": "Fruits/roseapple.jpg"},
    "breadfruit": {"hint": "b r _ a d f r _ _ t", "image": "Fruits/breadfruit.jpg"},
    "sugar apple": {"hint": "s _ g a r  a _ _ l _", "image": "Fruits/sugarapple.jpg"},
    "quince": {"hint": "q u _ n _ _", "image": "Fruits/quince.jpg"},
"loquat": {"hint": "l o q _ _ t", "image": "Fruits/loquat.jpg"},
"mangaba": {"hint": "m _ n g _ b _", "image": "Fruits/mangaba.jpg"},
"sapote": {"hint": "s _ p _ t _", "image": "Fruits/sapote.jpg"},
"moonfruit": {"hint": "m _ _ n f r _ _ t", "image": "Fruits/moonfruit.jpg"},
"horned melon": {"hint": "h _ r n _ d  m _ l _ n", "image": "Fruits/hornedmelon.jpg"},
"water apple": {"hint": "w _ t _ r  a p p _ _", "image": "Fruits/waterapple.jpeg"},
"mamey": {"hint": "m _ m _ _", "image": "Fruits/mamey.jpg"},
"indian gooseberry": {"hint": "i n _ _ _ n  g _ _ s _ b _ r r _", "image": "Fruits/indiangooseberry.jpg"},
"ambarella": {"hint": "a m _ _ r _ l _", "image": "Fruits/ambarella.jpg"},

    # HARD
    "aratilis": {"hint": "a r _ _ _ l _ s", "image": "Fruits/aratilis.jpg"},
    "soursop": {"hint": "s _ u r _ _ p", "image": "Fruits/soursop.jpg"},
    "santol": {"hint": "s a _ t _ l", "image": "Fruits/santol.jpg"},
    "kamias": {"hint": "k _ m _ _ s", "image": "Fruits/kamias.jpg"},
    "salak": {"hint": "s _ l _ k", "image": "Fruits/salak.jpg"},
    "jaboticaba": {"hint": "j _ b _ t _ c _ b _", "image": "Fruits/jaboticaba.jpg"},
    "longkong": {"hint": "l _ n g k _ n _", "image": "Fruits/longkong.jpg"},
    "miracle fruit": {"hint": "m _ r _ c _ e  f r _ _ t", "image": "Fruits/miraclefruit.jpg"},
    "velvet apple": {"hint": "v _ l v _ t  a p p _ _", "image": "Fruits/velvetapple.jpg"},
    "langsat": {"hint": "l _ n g _ _ t", "image": "Fruits/langsat.jpg"},
    "custard apple": {"hint": "c _ s t _ r d  a _ _ _ e", "image": "Fruits/custard apple.jpg"},
    "feijoa": {"hint": "f _ _ j _ a", "image": "Fruits/feijoa.jpg"},
    "tamarillo": {"hint": "t _ m a r _ l _ _", "image": "Fruits/tamarillo.jpg"},
    "nance": {"hint": "n _ n _ _", "image": "Fruits/nance.jpg"},
    "bael fruit": {"hint": "b _ _ l  f r _ _ t", "image": "Fruits/baelfruit.jpg"},
    "black sapote": {"hint": "b l _ c k  s _ p _ t _", "image": "Fruits/blacksapote.jpg"},
    "cupuacu": {"hint": "c _ p _ _ c _", "image": "Fruits/cupuacu.jpg"},
    "breadnut": {"hint": "b r _ a d n _ t", "image": "Fruits/breadnut.jpg"},
    "medlar": {"hint": "m _ d _ _ r", "image": "Fruits/medlar.jpg"},
    "jungle jalebi": {"hint": "j _ n g _ _  j _ l _ b _", "image": "Fruits/junglejalebi.jpg"},
    "lucuma": {"hint": "l u _ u m _", "image": "Fruits/lucuma.jpg"},
"rambai": {"hint": "r _ m b _ _", "image": "Fruits/rambai.jpg"},
"kei apple": {"hint": "k _ _  a p p _ _", "image": "Fruits/keiapple.jpg"},
"langsad": {"hint": "l _ n g s _ d", "image": "Fruits/langsad.jpg"},
"marang": {"hint": "m a r _ n _", "image": "Fruits/marang.jpg"},
"pulasan": {"hint": "p _ l a s _ n", "image": "Fruits/pulasan.jpg"},
"kaffir lime": {"hint": "k a _ _ _ r l _ _ e", "image": "Fruits/kaffirlime.jpg"},
"jambul": {"hint": "j _ m b _ l", "image": "Fruits/jambul.png"},
"bayberry": {"hint": "b a y b _ r r _", "image": "Fruits/bayberry.jpg"},
"bacuri": {"hint": "b _ c _ r _", "image": "Fruits/bacuri.jpg"}

}

easy = [
    "apple", "banana", "orange", "mango", "pineapple", "watermelon", "grapes",
    "strawberry", "lemon", "papaya", "guava", "pear", "melon", "blueberry",
    "cherry", "coconut", "kiwi", "tomato", "peach", "plum", "blackberry",
    "raspberry", "avocado", "lime", "cranberry", "orange melon", "apricot",
    "pineberry", "star apple", "honeydew"
]

medium = [
    "rambutan", "lychee", "dragonfruit", "passionfruit", "starfruit",
    "pomegranate", "persimmon", "tamarind", "mulberry", "sapodilla", "pomelo",
    "longan", "durian", "fig", "jujube", "gooseberry", "cucumber melon",
    "rose apple", "breadfruit", "sugar apple", "quince", "loquat", "mangaba",
    "sapote", "moonfruit", "horned melon", "water apple", "mamey",
    "indian gooseberry", "ambarella"
]

hard = [
    "aratilis", "soursop", "santol", "kamias", "salak", "jaboticaba",
    "longkong", "miracle fruit", "velvet apple", "langsat", "custard apple",
    "feijoa", "tamarillo", "nance", "bael fruit", "black sapote", "cupuacu",
    "breadnut", "medlar", "jungle jalebi", "lucuma", "rambai", "kei apple",
    "langsad", "marang", "pulasan", "kaffir lime", "jambul", "bayberry",
    "bacuri"
]
# --- Game variables ---
selected_list = []
original_list = []
points = 0
rounds = 0
random_word = ""
fruit_image = None
hints_left = 2
lives = 5
timer_seconds = 20
timer_running = False

# --- High score ---
HIGH_SCORE_FILE = "highscore.txt"

def get_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            return int(f.read())
    except:
        return 0

def save_high_score(score):
    current_high = get_high_score()
    if score > current_high:
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(str(score))

# --- Difficulty selection ---
def choose_easy():
    start_difficulty(easy)

def choose_medium():
    start_difficulty(medium)

def choose_hard():
    start_difficulty(hard)

def start_difficulty(list_choice):
    global selected_list, original_list
    original_list = list_choice.copy()
    selected_list = list_choice.copy()
    easy_button.pack_forget()
    medium_button.pack_forget()
    hard_button.pack_forget()
    start_button.pack()

# --- Game start ---
def start_game():
    global points, rounds, hints_left, lives, timer_running, timer_seconds, selected_list, fruit_image

    points = 0
    rounds = 0
    hints_left = 3
    lives = 5
    timer_running = False
    timer_seconds = 20

    # Reset list for current difficulty
    selected_list = original_list.copy()

    guess_button.config(state="normal")
    use_hint_button.config(state="normal")
    start_button.pack_forget()

    fruit_image = None
    image_label.config(image="")

    update_hearts()

    hearts_label.pack()
    timer_label.pack(pady=5)
    guess_entry.pack(pady=5)
    guess_button.pack()
    hint_label.pack()
    image_label.pack()
    result_label.pack()
    score_label.pack()
    use_hint_button.pack(pady=5)
    try_again_button.pack_forget()
    menu_button.pack_forget()

    score_label.config(text=f"Score: {points}")
    use_hint_button.config(text=f"Use Hint ({hints_left} left)", state="normal")

    next_word()

# --- Update hearts ---
def update_hearts():
    hearts_label.config(text="❤️ " * lives)

# --- Timer system ---
def start_timer():
    global timer_running, timer_seconds
    timer_running = False
    timer_seconds = 20
    timer_running = True
    update_timer()

def update_timer():
    global timer_seconds, timer_running

    if not timer_running:
        return

    timer_label.config(text=f"⏳ Time: {timer_seconds}s")

    if timer_seconds <= 0:
        timer_running = False
        lose_life("⏳ Time's up!")
        return

    timer_seconds -= 1
    window.after(1000, update_timer)

# --- Next word ---
def next_word():
    global random_word, fruit_image, timer_running, rounds, selected_list

    if rounds >= 10:
        timer_running = False
        save_high_score(points)
        high_score_label.config(text=f"High Score: {get_high_score()}")
        messagebox.showinfo("Game Finished", f"🎉 YOU FINISHED {rounds} ROUNDS!\nFinal Score: {points}")
        result_label.config(text=f"🎉 YOU FINISHED {rounds} ROUNDS!\nFinal Score: {points}", fg="purple")
        guess_button.config(state="disabled")
        use_hint_button.config(state="disabled")
        try_again_button.pack(pady=10)
        menu_button.pack()
        return

    if not selected_list:
        selected_list = original_list.copy()

    random_word = random.choice(selected_list)
    selected_list.remove(random_word)

    hint_label.config(text="")
    result_label.config(text="")
    guess_entry.delete(0, tk.END)

    if hints_left > 0:
        use_hint_button.config(state="normal")
    else:
        use_hint_button.config(state="disabled")

    img_path = fruits_with_hints[random_word]["image"]
    if img_path:
        img = Image.open(img_path)
        img = img.resize((200, 200))
        fruit_image = ImageTk.PhotoImage(img)
        image_label.config(image=fruit_image)
        image_label.image = fruit_image
    else:
        image_label.config(image="")
        fruit_image = None

    timer_seconds = 20
    timer_label.config(text=f"⏳ Time: {timer_seconds}s")
    start_timer()

    rounds += 1

# --- Use hint ---
def use_hint():
    global hints_left

    if hints_left > 0:
        hint_label.config(text=f"Hint: {fruits_with_hints[random_word]['hint']}")
        hints_left -= 1
        use_hint_button.config(text=f"Use Hint ({hints_left} left)")

        # Disable hint for the current round
        use_hint_button.config(state="disabled")

    # If no hints left at all, disable permanently
    if hints_left == 0:
        use_hint_button.config(state="disabled")


# --- Check guess ---
def check_guess():
    global points, timer_running
    guess = guess_entry.get().lower().strip()
    if guess == "":
        return

    guess_entry.delete(0, tk.END)
    timer_running = False

    if guess == random_word:
        points += 20
        score_label.config(text=f"Score: {points}")
        result_label.config(text="✅ Correct! +20 points!", fg="green")
        correct_sound.play()
    else:
        lose_life("❌ Wrong guess!")
        return

    window.after(1200, next_word)

# --- Lose life ---
def lose_life(message):
    global lives, timer_running
    timer_running = False
    lives -= 1
    update_hearts()

    result_label.config(
        text=f"{message}\nThe word was '{random_word}'",
        fg="red",
        font=("UrbanBright-Regular", 14, "")  # Example: font-family, size, style
    )


    wrong_sound.play()

    if lives <= 0:
        save_high_score(points)
        high_score_label.config(text=f"High Score: {get_high_score()}")
        messagebox.showinfo("Game Over", f"💀 GAME OVER! You ran out of lives!\nFinal Score: {points}")
        guess_button.config(state="disabled")
        use_hint_button.config(state="disabled")
        try_again_button.pack(pady=10)
        menu_button.pack()
        return

    window.after(1500, next_word)

# --- Menu / Retry ---
def try_again():
    start_game()

def back_to_menu():
    guess_entry.pack_forget()
    guess_button.pack_forget()
    hint_label.pack_forget()
    image_label.pack_forget()
    result_label.pack_forget()
    score_label.pack_forget()
    use_hint_button.pack_forget()
    try_again_button.pack_forget()
    menu_button.pack_forget()
    hearts_label.pack_forget()
    timer_label.pack_forget()

    easy_button.pack(pady=5)
    medium_button.pack(pady=5)
    hard_button.pack(pady=5)

    score_label.config(text="Score: 0")
    image_label.config(image="")
    result_label.config(text="")

def show_high_score():
    score = get_high_score()
    result_label.config(text=f"🏆 High Score: {score}", fg="blue")
    result_label.pack()



# --- UI Setup ---
window = tk.Tk()
window.title("🍇 Guess The Fruit Game")
window.geometry("360x550")
window.config(bg="#fff7dc")

screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()


bg_path = r"photo\Backround.jpg"
bg_image = Image.open(bg_path)
bg_image = bg_image.resize((screen_w, screen_h))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)



title_label = tk.Label(
    window,
    text="🍎 GUESS THE FRUIT 🍌",
    font=("PickyGirls-Regular", 20, "bold"),  # playful and jolly
    bg="#F8E4A6",
    fg="#ff7f50"
)

title_label.pack(pady=10)

high_score_label = tk.Label(window, text=f"High Score: {get_high_score()}",
                            font=("UrbanBright-Regular", 15, ""), bg="#F8E4A6", fg="blue")
high_score_label.pack(pady=5)

# Difficulty buttons
# Common button style
button_font = ("UrbanBright-Regular", 14, "")  # bigger, bold, kid-friendly font

# Easy button
easy_button = tk.Button(window, text="EASY", bg="#a3ffb3", font=button_font, width=20, command=choose_easy)
easy_button.pack(pady=8)  # pady controls spacing between buttons

# Medium button
medium_button = tk.Button(window, text="MEDIUM", bg="#ffd27f", font=button_font, width=20, command=choose_medium)
medium_button.pack(pady=8)

# Hard button
hard_button = tk.Button(window, text="HARD", bg="#ff9999", font=button_font, width=20, command=choose_hard)
hard_button.pack(pady=8)

start_button = tk.Button(window, text="Start Game", font=("UrbanBright-Regular", 13, ""),
                         bg="#ffcc70", fg="black", command=start_game)

use_hint_button = tk.Button(window, text="Use Hint", bg="#87CEFA",
                            font=("UrbanBright-Regular", 13, ""), command=use_hint)

hint_label = tk.Label(window, text="", font=("UrbanBright-Regular", 13, ""), bg="#fff7dc")
image_label = tk.Label(window, bg="#fff7dc")
guess_entry = tk.Entry(window, font=("Arial", 12), justify="center")
guess_button = tk.Button(window, text="SUBMIT GUESS", bg="#98fb98",
                         font=("UrbanBright-Regular", 11, ""), command=check_guess)
result_label = tk.Label(window, text="", font=("Arial", 12), bg="#fff7dc")
score_label = tk.Label(window, text="SCORE: 0", font=("UrbanBright-Regular", 15, ""),
                       bg="#F8E4A6", fg="#ff6347")
try_again_button = tk.Button(window, text="TRY AGAIN", font=("UrbanBright-Regular", 13, ""),
                             bg="#ffcc70", fg="black", command=try_again)
menu_button = tk.Button(window, text="MENU", font=("UrbanBright-Regular", 12, ""),
                        bg="#f7a4a4", fg="black", command=back_to_menu)
hearts_label = tk.Label(window, text="", font=("Arial", 17), fg="red", bg="#F8E4A6")
timer_label = tk.Label(window, text="", font=("UrbanBright-Regular", 13, ""), bg="#F8E4A6", fg="#6B8A7A")

update_hearts()
window.mainloop()
