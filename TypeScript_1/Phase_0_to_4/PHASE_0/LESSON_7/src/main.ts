type ClientProfile = {
  name: string;
  email: string;
  avatarUrl?: string;
  bio?: string;
};

const clientA: ClientProfile = {
  name: "Nyro",
  email: "nyro@gmail.com",
  bio: "I am a disciplined person",
};

console.log(`${clientA.name} ${clientA.email} ${clientA.bio}`);
