const results = [];

function check(label, condition) {
  results.push({ label, ok: Boolean(condition) });
}

function greetPerson(name) {
  console.log(`Hello, ${name}!`);
}

function double(number) {
  return number * 2;
}

function isShortName(name) {
  return name.length <= 4;
}

function triple(x) {
  return x * 3;
}

greetPerson("Sam");
greetPerson("Dana");
greetPerson("Dylan");

const four = double(4);
console.log(four);
console.log(double(0));

console.log(isShortName("Sam"));
console.log(isShortName("Dana"));

const nine = triple(3);
console.log(nine);

check("4.2 double(4) returns 8", four === 8);
check("4.2 double(0) returns 0", double(0) === 0);
check("4.3 isShortName(Sam) is true", isShortName("Sam") === true);
check("4.3 isShortName(Dana) is true", isShortName("Dana") === true);
check("4.3 isShortName(Margaret) is false", isShortName("Margaret") === false);
check("4.4 triple hands a value back (return, not console.log)", nine === 9);

if (results.every((r) => r.ok)) {
  console.log("chapter 04 exercises: all checks ok");
} else {
  console.error(results.filter((r) => !r.ok));
  process.exit(1);
}
