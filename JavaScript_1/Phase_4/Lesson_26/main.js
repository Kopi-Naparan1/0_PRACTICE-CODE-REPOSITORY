// Simulating async actions using setTimeout + callbacks

function loginUser(username, callback) {
  setTimeout(() => {
    console.log(`✅ User ${username} logged in`);
    callback(username);
  }, 3000);
}

function loadDashboard(user, callback) {
  setTimeout(() => {
    console.log(`📂 Dashboard loaded for ${user}`);
    callback();
  }, 5000);
}

function fetchData(callback) {
  setTimeout(() => {
    console.log(`📊 Data fetched`);
    callback();
  }, 7000);
}

// Now execute them in sequence — CALLBACK HELL
loginUser("nyro", function (user) {
  loadDashboard(user, function () {
    fetchData(function () {
      console.log("🚀 All done!");
    });
  });
});
