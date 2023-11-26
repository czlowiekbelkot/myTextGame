import pygame
import sys
import json

# Initialization
pygame.init()
pygame.mixer.init()

# Sounds
clickSound = pygame.mixer.Sound("sound/click.wav")
pygame.mixer.music.load("sound/music.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.5)

# FPS
clock = pygame.time.Clock()

# Screen options
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Vault 28")

# Colors
white = (255, 255, 255)
grey = (190, 190, 190)

# Current state ;)
current_state = "main_menu"
current_location_id = 1

# Images
button_image = pygame.image.load("buttons/button.jpg")
# Background
background = pygame.image.load("images/background.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))

# Drawing text + drawin new lines form JSON file
def draw_text(text, font, color, surface, x, y):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y + i * font.get_height())
        surface.blit(text_surface, text_rect)

# For creating buttons from JSON file
def buttons(action, data):
    global current_state, current_location_id

    location_number = int(action.split("_")[-1])
    location_data = data["locations"][location_number - 1]

    current_location_id = location_number
    current_state = "play"

    clickSound.play()

# Main Menu 
def main_menu():
    global current_state

    while True:
              
        # Background
        screen.blit(background, (0, 0))

        # Title
        title_font = pygame.font.Font(None, 90)
        draw_text("Vault 28", title_font, white, screen, (screen_width // 2) - 125, 50)

        # Buttons
        button_font = pygame.font.Font(None, 36)

        play_button = pygame.Rect((screen_width // 2) - 60, 200, 120, 50)
        options_button = pygame.Rect((screen_width // 2) - 60, 270, 120, 50)
        credits_button = pygame.Rect((screen_width // 2) - 60, 340, 120, 50)
        exit_button = pygame.Rect((screen_width // 2) - 60, 410, 120, 50)

        # Drawing image of buttons
        screen.blit(button_image,
                    (play_button.x + (play_button.width - button_image.get_width()) // 2,
                     play_button.y + (play_button.height - button_image.get_height()) // 2))
        screen.blit(button_image,
                    (options_button.x + (options_button.width - button_image.get_width()) // 2,
                     options_button.y + (options_button.height - button_image.get_height()) // 2))
        screen.blit(button_image,
                    (credits_button.x + (credits_button.width - button_image.get_width()) // 2,
                     credits_button.y + (credits_button.height - button_image.get_height()) // 2))
        screen.blit(button_image,
                    (exit_button.x + (exit_button.width - button_image.get_width()) // 2,
                     exit_button.y + (exit_button.height - button_image.get_height()) // 2))

        # Drawing text for buttons
        draw_text("Play", button_font, grey, screen,
                  play_button.x + (play_button.width - button_font.size("Play")[0]) // 2,
                  play_button.y + (play_button.height - button_font.size("Play")[1]) // 2)
        draw_text("Options", button_font, grey, screen,
                  options_button.x + (options_button.width - button_font.size("Options")[0]) // 2,
                  options_button.y + (options_button.height - button_font.size("Options")[1]) // 2)
        draw_text("Credits", button_font, grey, screen,
                  credits_button.x + (credits_button.width - button_font.size("Credits")[0]) // 2,
                  credits_button.y + (credits_button.height - button_font.size("Credits")[1]) // 2)
        draw_text("Exit", button_font, grey, screen,
                  exit_button.x + (exit_button.width - button_font.size("Exit")[0]) // 2,
                  exit_button.y + (exit_button.height - button_font.size("Exit")[1]) // 2)

        # Refresh screen
        pygame.display.update()

        # For clicking on buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clickSound.play()
                if play_button.collidepoint(event.pos):
                    current_state = "play"
                    return
                elif options_button.collidepoint(event.pos):
                    current_state = "options"
                    return
                elif credits_button.collidepoint(event.pos):
                    current_state = "credits"
                    return
                elif exit_button.collidepoint(event.pos):
                    sys.exit(0)
                    return
            # For exit event (ESC and X button)
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

# Credits
def show_credits():
    credits_text = [
        "Autor: Człowiek Bełkot",
        "Grafika: Człowiek Bełkot",
        "Scenariusz: Człowiek Bełkot & Syn and ChatGPT",
        "Muzyka: pixabay.com",
        "Dźwięki: z nielegalnych źródeł",
        "Podziękowania:",
        "Dziękuję @babcia_would_to_hug_you", 
        "za cierpliwość i rady,",
        "bogu za nie danie mi siły,",
        "bo gdyby dał mi siłę, to bym to rozpierdolił!!!"
    ]

    while True:
        
        screen.blit(background, (0, 0))

        title_font = pygame.font.Font(None, 50)
        draw_text("Credits", title_font, white, screen, (screen_width // 2) - 70, 50)

        text_font = pygame.font.Font(None, 36)
        y = 150

        for line in credits_text:
            draw_text(line, text_font, white, screen, 50, y)
            y += 40

        # Drawing Back button
        back_button = pygame.Rect(20, 20, 150, 36)
        screen.blit(button_image, (back_button.x, back_button.y))
        draw_text("Back", text_font, grey, screen,
                  back_button.x + (back_button.width - text_font.size("Back")[0]) // 2,
                  back_button.y + (back_button.height - text_font.size("Back")[1]) // 2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clickSound.play()
                if back_button.collidepoint(event.pos):
                    clickSound.play()
                    return "main_menu"
            # For exit event (ESC and X button)
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "main_menu"
        
# Options
def options():
    options_text = [
        "You don't have any options."
    ]

    while True:
        
        screen.blit(background, (0, 0))

        title_font = pygame.font.Font(None, 50)
        draw_text("Options", title_font, white, screen, (screen_width // 2) - 70, 50)

        text_font = pygame.font.Font(None, 36)
        y = 150

        for line in options_text:
            draw_text(line, text_font, white, screen, 50, y)
            y += 40

        back_button = pygame.Rect(20, 20, 150, 36)
        screen.blit(button_image, (back_button.x, back_button.y))
        draw_text("Back", text_font, grey, screen,
                  back_button.x + (back_button.width - text_font.size("Back")[0]) // 2,
                  back_button.y + (back_button.height - text_font.size("Back")[1]) // 2)
        pygame.display.update()

        # For clicking on buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clickSound.play()
                if back_button.collidepoint(event.pos):
                    clickSound.play()
                    return "main_menu"
            # For exit event (ESC and X button)
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "main_menu"

# Play
def play():
    global current_state, current_location_id

    # Loading storyline from JSON file
    with open("lokacje/main_game.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    while True:
        
        screen.blit(background, (0, 0))

        # Find current location in JSON file
        current_location = next((loc for loc in data["locations"] if loc["location_id"] == current_location_id), None)

        if current_location:
            text_font = pygame.font.Font(None, 36)
            draw_text(current_location["text"], text_font, white, screen, 50, 70)

            # Check image in current location
            if "image" in current_location:
                image_path = current_location["image"]
                original_image = pygame.image.load(image_path)

                # Set the image setting
                width = 150
                height = int(original_image.get_height() * (width / original_image.get_width()))
                scaled_image = pygame.transform.scale(original_image, (width, height))

                # Set coordinates of the image
                image_rect = scaled_image.get_rect()
                image_rect.center = (screen_width // 2, screen_height // 2)
                screen.blit(scaled_image, image_rect)

            # Drawing buttons
            button_font = pygame.font.Font(None, 36)
            for button in current_location["buttons"]:
                button_rect = pygame.Rect(button["position"][0], button["position"][1], 150, 36)

                # Draw button
                screen.blit(button_image, (button_rect.x, button_rect.y))

                # Centering text on the button
                text_width, text_height = button_font.size(button["text"])

                # Set the image setting
                width = max(150, text_width + 20)
                height = 36

                # Scaling button to the length of text
                scaled_image = pygame.transform.scale(button_image, (width, height))
                button_rect.width = width

                text_x = button_rect.x + (button_rect.width - text_width) // 2
                text_y = button_rect.y + (button_rect.height - text_height) // 2

                # Drawing scaled button image
                screen.blit(scaled_image, (button_rect.x, button_rect.y))

                # Drawing text on the button
                draw_text(button["text"], button_font, grey, screen, text_x, text_y)

            # Drawing Main Menu button
            back_button = pygame.Rect(20, 20, 150, 36)
            screen.blit(button_image, (back_button.x, back_button.y))
            draw_text("Main menu", button_font, grey, screen,
                      back_button.x + (back_button.width - button_font.size("Main Menu")[0]) // 2,
                      back_button.y + (back_button.height - button_font.size("Main Menu")[1]) // 2)

            pygame.display.update()

            # For clicking on buttons
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    clickSound.play()
                    if back_button.collidepoint(event.pos):
                        return "main_menu"
                    for button in current_location["buttons"]:
                        button_rect = pygame.Rect(button["position"][0], button["position"][1], 150, 36)
                        if button_rect.collidepoint(event.pos):
                            buttons(button["action"], data)
                            return current_state
                # For exit event (ESC and X button)
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "main_menu"

# Main loop
while True:
    clock.tick(30) # FPS

    if current_state == "main_menu":
        main_menu()
    elif current_state == "play":
        current_state = play()
    elif current_state == "options":
        current_state = options()
    elif current_state == "credits":
        current_state = show_credits()
