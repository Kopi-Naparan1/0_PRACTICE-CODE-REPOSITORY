async function orderBurger() {
  return Promise.resolve("Pizza ");
}

async function awaitHelper() {
  const burger = await orderBurger();
  console.log(burger);
}

awaitHelper();
