from abc import ABC, abstractmethod


# Base abstract class for extensibility
class SocialMediaSystem(ABC):
    @abstractmethod
    def display(self):
        pass


# User class (can post, comment, like)
class User:
    def __init__(self, name, username):
        self.name = name
        self.username = f"@{username}"
        self.posts = []

    def create_post(self, content):
        post = Post(self, content)
        self.posts.append(post)
        return post

    def comment_on_post(self, post, comment_text):
        comment = Comment(self, comment_text)
        post.add_comment(comment)

    def like_post(self, post):
        post.add_like(self)

    def __str__(self):
        return f"{self.name} ({self.username})"


# Post class (belongs to a User)
class Post(SocialMediaSystem):
    def __init__(self, user, content):
        self.author = user
        self.content = content
        self.__likes = []
        self.__comments = []

    def add_like(self, user):
        if user not in self.__likes:
            self.__likes.append(user)

    def add_comment(self, comment):
        self.__comments.append(comment)

    def display(self):
        print(f"{self.author.username} posted:")
        print(f"\t{self.content}")
        print(f"\tLikes: {len(self.__likes)} | Comments: {len(self.__comments)}")
        if self.__comments:
            print("\n\t--- Comments ---")
            for comment in self.__comments:
                print(f"\t{comment}")
        print("-" * 40)

    def __str__(self):
        return f"{self.author.username}: {self.content}"


# Comment class (belongs to a User)
class Comment:
    def __init__(self, user, text):
        self.user = user
        self.text = text

    def __str__(self):
        return f"{self.user.username}: {self.text}"


# Main App to manage everything
class SocialMediaApp:
    def __init__(self):
        self.users = []
        self.posts = []

    def register_user(self, name, username):
        user = User(name, username)
        self.users.append(user)
        return user

    def add_post(self, post):
        self.posts.append(post)

    def show_feed(self):
        print("=== SOCIAL MEDIA FEED ===")
        for post in self.posts:
            post.display()


# === Test run ===
app = SocialMediaApp()

# Register users
alice = app.register_user("Alice", "alice_01")
bob = app.register_user("Bob", "bob_the_builder")
carla = app.register_user("Carla", "carla.cool")

# Alice posts something
post1 = alice.create_post("Hello everyone! This is my first post.")
app.add_post(post1)

# Bob and Carla interact with Alice's post
bob.like_post(post1)
carla.like_post(post1)
carla.comment_on_post(post1, "Welcome to the platform!")
bob.comment_on_post(post1, "Nice to see you here!")

# Carla posts something
post2 = carla.create_post("Today I learned Python OOP. Feels great!")
app.add_post(post2)

# Alice interacts with Carla's post
alice.like_post(post2)
alice.comment_on_post(post2, "Good job Carla!")

# Show full feed
app.show_feed()
