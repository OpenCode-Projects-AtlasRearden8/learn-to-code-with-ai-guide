const results = [];

function check(label, condition) {
  results.push({ label, ok: Boolean(condition) });
}

console.log("Hello, world!");
console.log("My name is Sam");
console.log(25 + 75);
console.log("25 + 75");

check("exercise 1.1: prints something to the console", typeof console.log === "function");
check("exercise 1.2: unquoted math computes", 25 + 75 === 100);
check("exercise 1.2: quoted text stays text", "25 + 75" === "25 + 75");
check("exercise 1.3: quotes change behavior", String(2 + 2) !== "2 + 2");

if (results.every((r) => r.ok)) {
  console.log("chapter 01 exercises: all checks ok");
} else {
  console.error(results.filter((r) => !r.ok));
  process.exit(1);
}
