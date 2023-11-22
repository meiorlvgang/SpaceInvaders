import pygame, sys, requests

screen_width = 600
screen_height = 600

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.menu_items = ["Play", "Quit"]
        self.selected_item = 0

    def draw(self):
        for i, item in enumerate(self.menu_items):
            color = (255, 255, 255) if i == self.selected_item else (150, 150, 150)
            text = self.font.render(item, True, color)
            text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + i * 50))
            self.screen.blit(text, text_rect)

    def handle_key_event(self, event):
        if event.key == pygame.K_UP:
            self.selected_item = (self.selected_item - 1) % len(self.menu_items)
        elif event.key == pygame.K_DOWN:
            self.selected_item = (self.selected_item + 1) % len(self.menu_items)
        elif event.key == pygame.K_RETURN:
            if self.selected_item == 0:  # Play
                return "Play"
            elif self.selected_item == 1:  # Quit
                pygame.quit()
                sys.exit()


    def login_or_register(self):
        # Placeholder API endpoint, replace it with your actual authentication API endpoint
        api_endpoint = "https://example.com/api/auth"

        # Get user input for login or registration
        choice = input("Do you want to (1) login or (2) register? ")

        if choice == "1":  # Login
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            # Make a request to the API for login
            response = requests.post(api_endpoint + "/login", json={"username": username, "password": password})

            if response.status_code == 200:
                print("Login successful!")
                return True
            else:
                print("Login failed. Please check your credentials.")
                return False

        elif choice == "2":  # Register
            username = input("Choose a username: ")
            password = input("Choose a password: ")

            # Make a request to the API for registration
            response = requests.post(api_endpoint + "/register", json={"username": username, "password": password})

            if response.status_code == 201:
                print("Registration successful!")
                return True
            else:
                print("Registration failed. Please choose a different username.")
                return False

        else:
            print("Invalid choice. Please enter 1 for login or 2 for registration.")
            return False
