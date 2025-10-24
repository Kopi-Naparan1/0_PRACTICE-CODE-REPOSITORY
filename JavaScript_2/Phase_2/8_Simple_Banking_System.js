function deposit(account, money) {
  account.remainingBalance += money;
  console.log(`${money} is deposited to ${account.name}`);
}

function withdraw(account, money) {
  account.remainingBalance -= money;
  console.log(`${money} is deposited to ${account.name}`);
}

function checkBalance(account) {
  console.log(`${account.name} Balance: ${account.remainingBalance}`);
}

function accountMaker(name, money = 0) {
  console.log(`${name} is created`);
  return {
    name: name,
    remainingBalance: money,
  };
}

function main() {
  const p1 = accountMaker("p1");
  const p2 = accountMaker("p2");
  const p3 = accountMaker("p3");

  checkBalance(p1);
  deposit(p1, 10000);
  withdraw(p1, 900);
  checkBalance(p1);
}

main();
