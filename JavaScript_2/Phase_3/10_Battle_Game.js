function characterMaker(name) {
  return {
    name: name,
    health: 100,
    attack: 1,
    defense: 20,
  };
}

function randomAttack() {
  let damage = Math.floor(Math.random() * 20) + 1;
  return damage;
}

function game(player1, player2, damage, stats) {
  let finalDamage1 = player1.attack * damage();
  let finalDamage2 = player2.attack * damage();

  if (player2.defense > 0) {
    player2.defense -= finalDamage1;
    console.log(`${player1.name} dealth ${finalDamage1} to ${player2.name}.`);
    if (player2.defense < 0) {
      player2.health += player2.defense;
      player2.defense = 0;
    }
  } else {
    player2.health -= finalDamage1;
    console.log(`${player1.name} dealth ${finalDamage1} to ${player2.name}.`);
  }

  if (player1.defense > 0) {
    player1.defense -= finalDamage2;
    console.log(`${player2.name} dealth ${finalDamage2} to ${player1.name}.`);
    if (player1.defense < 0) {
      player1.health += player1.defense;
      player1.defense = 0;
    }
  } else {
    player1.health -= finalDamage1;
    console.log(`${player2.name} dealth ${finalDamage2} to ${player1.name}.`);
  }

  if (player1.health <= 0) {
    console.log(`${player2.name} won!!!`);
    return null;
  } else if (player2.health <= 0) {
    console.log(`${player1.name} won!!!`);
    return null;
  } else if (player1.health <= 0 && player2.health <= 0) {
    console.log("ITS A TIE");
  }

  stats(player1, player2);
}

function showStats(player1, player2) {
  const players = [player1, player2];

  for (let i = 0; i < players.length; i++) {
    console.log("\n");
    console.log(`Name: ${players[i].name}`);
    console.log(`Health: ${players[i].health}`);
    console.log(`Defense: ${players[i].defense}`);
    console.log("\n");
  }
}

function main() {
  let player1 = characterMaker("Nyro");
  let player2 = characterMaker("Khuf");

  let interval = setInterval(() => {
    const gameResult = game(player1, player2, randomAttack, showStats);
    if (gameResult === null) {
      isOn = false;
    }
  }, 3000);
}

main();
